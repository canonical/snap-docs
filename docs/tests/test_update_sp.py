import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch


SPHINX_SCRIPTS = Path(__file__).resolve().parents[1] / ".sphinx"
sys.path.insert(0, str(SPHINX_SCRIPTS))

import update_sp


class FakeResponse:
    def __init__(self, *, json_data=None, text="", content=b""):
        self._json_data = json_data
        self.text = text
        self.content = content

    def json(self):
        return self._json_data


class ApiAndDownloadTests(unittest.TestCase):
    def test_query_api_uses_timeout_and_returns_response(self):
        response = FakeResponse()
        with patch.object(update_sp.requests, "get", return_value=response) as get:
            self.assertIs(update_sp.query_api("https://example.test/data"), response)

        get.assert_called_once_with("https://example.test/data", timeout=update_sp.TIMEOUT)

    def test_query_api_wraps_request_errors(self):
        with patch.object(
            update_sp.requests,
            "get",
            side_effect=update_sp.RequestException("network unavailable"),
        ):
            with self.assertRaisesRegex(
                RuntimeError, "Failed query_api\\(\\): https://example.test/data"
            ):
                update_sp.query_api("https://example.test/data")

    def test_download_writes_bytes_and_creates_parent_directories(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            destination = Path(temp_dir) / "nested" / "download.bin"
            with patch.object(
                update_sp,
                "query_api",
                return_value=FakeResponse(content=b"\x00configuration"),
            ):
                update_sp.download_file("https://example.test/file", str(destination))

            self.assertEqual(destination.read_bytes(), b"\x00configuration")

    def test_download_wraps_failures_with_source_url(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            destination = Path(temp_dir) / "download.bin"
            with patch.object(
                update_sp,
                "query_api",
                side_effect=RuntimeError("network unavailable"),
            ):
                with self.assertRaisesRegex(
                    RuntimeError, "Failed download_file\\(\\): https://example.test/file"
                ):
                    update_sp.download_file(
                        "https://example.test/file", str(destination)
                    )


class StaticFileUpdateTests(unittest.TestCase):
    @staticmethod
    def make_item(name, item_type, sha="remote-sha", download_url=None):
        return {
            "name": name,
            "type": item_type,
            "sha": sha,
            "download_url": download_url or f"https://example.test/{name}",
        }

    def test_updates_changed_and_new_files_and_writes_new_file_manifest(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            sphinx_dir = Path(temp_dir) / ".sphinx"
            update_dir = sphinx_dir / "update"
            sphinx_dir.mkdir()
            root_items = [
                self.make_item("changed.txt", "file"),
                self.make_item("update_sp.py", "file"),
                self.make_item("new.txt", "file"),
                self.make_item("version", "file"),
                self.make_item("nested", "dir"),
            ]
            nested_items = [
                self.make_item("nested-changed.txt", "file"),
                self.make_item("nested-new.txt", "file"),
                self.make_item("nested-same.txt", "file", sha="local-sha"),
            ]
            responses = [
                FakeResponse(json_data=root_items),
                FakeResponse(json_data=nested_items),
            ]
            local_files = [
                "changed.txt",
                "update_sp.py",
                "nested-changed.txt",
                "nested-same.txt",
            ]
            local_paths = [str(sphinx_dir / name) for name in local_files]

            def record_download(url, output_path):
                path = Path(output_path)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(url)

            with patch.object(update_sp, "SPHINX_DIR", str(sphinx_dir)), patch.object(
                update_sp, "SPHINX_UPDATE_DIR", str(update_dir)
            ), patch.object(
                update_sp,
                "get_local_files_and_paths",
                return_value=(local_files, local_paths),
            ), patch.object(
                update_sp, "get_git_revision_hash", return_value="local-sha"
            ), patch.object(
                update_sp, "query_api", side_effect=responses
            ) as query, patch.object(
                update_sp, "download_file", side_effect=record_download
            ) as download:
                updated, new_files = update_sp.update_static_files()

            self.assertTrue(updated)
            self.assertTrue(new_files)
            self.assertEqual(
                (sphinx_dir / "NEWFILES.txt").read_text(),
                "new.txt\nnested-new.txt\n",
            )
            self.assertEqual(
                [Path(item.args[1]).relative_to(sphinx_dir).as_posix()
                 for item in download.call_args_list],
                [
                    "update/changed.txt",
                    "update/update_sp.py",
                    "update/new.txt",
                    "update/version",
                    "update/nested/nested-changed.txt",
                    "update/nested/nested-new.txt",
                ],
            )
            query.assert_has_calls(
                [
                    call(update_sp.GITHUB_API_SPHINX_DIR),
                    call(f"{update_sp.GITHUB_API_SPHINX_DIR}/nested"),
                ]
            )

    def test_unchanged_files_report_no_updates(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            sphinx_dir = Path(temp_dir) / ".sphinx"
            sphinx_dir.mkdir()
            item = self.make_item("same.txt", "file", sha="local-sha")

            with patch.object(update_sp, "SPHINX_DIR", str(sphinx_dir)), patch.object(
                update_sp,
                "get_local_files_and_paths",
                return_value=(["same.txt"], [str(sphinx_dir / "same.txt")]),
            ), patch.object(
                update_sp, "get_git_revision_hash", return_value="local-sha"
            ), patch.object(
                update_sp, "query_api", return_value=FakeResponse(json_data=[item])
            ), patch.object(update_sp, "download_file") as download:
                self.assertEqual(update_sp.update_static_files(), (False, False))

            download.assert_not_called()
            self.assertFalse((sphinx_dir / "NEWFILES.txt").exists())

    def test_git_hash_uses_git_hash_object(self):
        with patch.object(
            update_sp.subprocess, "check_output", return_value=b"abc123\n"
        ) as check_output:
            self.assertEqual(update_sp.get_git_revision_hash("config.ini"), "abc123")

        check_output.assert_called_once_with(["git", "hash-object", "config.ini"])

    def test_local_file_discovery_returns_names_and_matching_paths(self):
        first_path = str(Path("docs") / ".sphinx" / ".config")
        second_path = str(Path("docs") / ".sphinx" / "nested" / "rules.yml")
        with patch.object(update_sp, "SPHINX_DIR", "docs/.sphinx"), patch.object(
            update_sp.glob,
            "iglob",
            side_effect=[iter([first_path]), iter([second_path])],
        ) as iglob:
            files, paths = update_sp.get_local_files_and_paths()

        self.assertEqual(files, [".config", "rules.yml"])
        self.assertEqual(paths, [first_path, second_path])
        self.assertEqual(iglob.call_count, 2)


class MainTests(unittest.TestCase):
    def run_main_with_mocked_api(self, temp_dir, local_version, latest_version):
        sphinx_dir = Path(temp_dir) / ".sphinx"
        sphinx_dir.mkdir()
        (sphinx_dir / "version").write_text(local_version)
        requirements = Path(temp_dir) / "requirements.txt"
        requirements.write_text("shared-package\nlocal-only\n")
        responses = {
            update_sp.GITHUB_API_BASE + "/releases/latest": FakeResponse(
                json_data={"tag_name": latest_version}
            ),
            update_sp.GITHUB_RAW_BASE + "/CHANGELOG.md": FakeResponse(
                text=f"# {latest_version}\nLatest changes\n# {local_version}\nOlder changes"
            ),
            update_sp.GITHUB_RAW_BASE + "/docs/requirements.txt": FakeResponse(
                text="shared-package\nremote-only\n"
            ),
        }
        return sphinx_dir, requirements, responses

    def test_outdated_version_downloads_updates_and_reports_new_requirements(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            sphinx_dir, requirements, responses = self.run_main_with_mocked_api(
                temp_dir, "1.0.0", "2.0.0"
            )

            def response_for(url):
                return responses[url]

            with patch.object(update_sp, "SPHINX_DIR", str(sphinx_dir)), patch.object(
                update_sp, "REQUIREMENTS", str(requirements)
            ), patch.object(
                update_sp, "query_api", side_effect=response_for
            ) as query, patch.object(
                update_sp, "update_static_files", return_value=(True, True)
            ) as update_static, patch.object(update_sp, "download_file") as download:
                with patch("builtins.print") as print_output:
                    update_sp.main()

            update_static.assert_called_once_with()
            download.assert_called_once_with(
                update_sp.GITHUB_RAW_BASE + "/docs/.sphinx/version",
                str(sphinx_dir / "update" / "version"),
            )
            self.assertEqual(query.call_count, 3)
            printed = "\n".join(
                " ".join(str(arg) for arg in item.args)
                for item in print_output.call_args_list
            )
            self.assertIn("Latest changes", printed)
            self.assertIn("remote-only", printed)
            self.assertNotIn("Older changes", printed)
            self.assertIn("New files have been downloaded", printed)

    def test_current_version_skips_static_updates_but_checks_requirements(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            sphinx_dir, requirements, responses = self.run_main_with_mocked_api(
                temp_dir, "2.0.0", "2.0.0"
            )

            with patch.object(update_sp, "SPHINX_DIR", str(sphinx_dir)), patch.object(
                update_sp, "REQUIREMENTS", str(requirements)
            ), patch.object(
                update_sp, "query_api", side_effect=lambda url: responses[url]
            ), patch.object(
                update_sp, "update_static_files"
            ) as update_static:
                with patch("builtins.print") as print_output:
                    update_sp.main()

            update_static.assert_not_called()
            output = "\n".join(
                " ".join(str(arg) for arg in item.args)
                for item in print_output.call_args_list
            )
            self.assertIn("This version is up to date.", output)
            self.assertIn("remote-only", output)

    def test_missing_requirements_file_is_reported_without_aborting(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            sphinx_dir, requirements, responses = self.run_main_with_mocked_api(
                temp_dir, "2.0.0", "2.0.0"
            )
            requirements.unlink()

            with patch.object(update_sp, "SPHINX_DIR", str(sphinx_dir)), patch.object(
                update_sp, "REQUIREMENTS", str(requirements)
            ), patch.object(
                update_sp, "query_api", side_effect=lambda url: responses[url]
            ):
                with patch("builtins.print") as print_output:
                    update_sp.main()

            output = "\n".join(
                " ".join(str(arg) for arg in item.args)
                for item in print_output.call_args_list
            )
            self.assertIn("requirements.txt not found", output)
            self.assertIn("not checked", output)


if __name__ == "__main__":
    unittest.main()
