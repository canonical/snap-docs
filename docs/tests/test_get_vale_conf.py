import sys
import tempfile
import unittest
from pathlib import Path
from subprocess import CalledProcessError
from types import SimpleNamespace
from unittest.mock import patch


SPHINX_SCRIPTS = Path(__file__).resolve().parents[1] / ".sphinx"
sys.path.insert(0, str(SPHINX_SCRIPTS))

import get_vale_conf


class CopyFilesToPathTests(unittest.TestCase):
    def test_missing_source_returns_false(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing_source = Path(temp_dir) / "missing"
            destination = Path(temp_dir) / "destination"

            self.assertFalse(
                get_vale_conf.copy_files_to_path(str(missing_source), str(destination))
            )
            self.assertFalse(destination.exists())

    def test_existing_file_is_preserved_without_overwrite(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.txt"
            destination = Path(temp_dir) / "destination.txt"
            source.write_text("new content")
            destination.write_text("existing content")

            self.assertTrue(
                get_vale_conf.copy_files_to_path(str(source), str(destination))
            )

            self.assertEqual(destination.read_text(), "existing content")

    def test_existing_file_is_replaced_with_overwrite(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.txt"
            destination = Path(temp_dir) / "destination.txt"
            source.write_text("new content")
            destination.write_text("existing content")

            self.assertTrue(
                get_vale_conf.copy_files_to_path(
                    str(source), str(destination), overwrite=True
                )
            )

            self.assertEqual(destination.read_text(), "new content")

    def test_existing_directory_is_preserved_without_overwrite(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source"
            destination = Path(temp_dir) / "destination"
            source.mkdir()
            destination.mkdir()
            (source / "new.txt").write_text("new")
            (destination / "existing.txt").write_text("existing")

            self.assertTrue(
                get_vale_conf.copy_files_to_path(str(source), str(destination))
            )

            self.assertTrue((destination / "existing.txt").exists())
            self.assertFalse((destination / "new.txt").exists())

    def test_existing_directory_is_replaced_with_overwrite(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source"
            destination = Path(temp_dir) / "destination"
            source.mkdir()
            destination.mkdir()
            (source / "new.txt").write_text("new")
            (destination / "existing.txt").write_text("existing")

            self.assertTrue(
                get_vale_conf.copy_files_to_path(
                    str(source), str(destination), overwrite=True
                )
            )

            self.assertEqual((destination / "new.txt").read_text(), "new")
            self.assertFalse((destination / "existing.txt").exists())

    def test_copy_error_returns_false(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.txt"
            destination = Path(temp_dir) / "destination.txt"
            source.write_text("content")

            with patch.object(
                get_vale_conf.shutil, "copy2", side_effect=OSError("copy failed")
            ):
                self.assertFalse(
                    get_vale_conf.copy_files_to_path(str(source), str(destination))
                )


class CloneAndCopyTests(unittest.TestCase):
    def test_empty_mapping_does_not_clone(self):
        with patch.object(get_vale_conf.subprocess, "run") as run:
            self.assertFalse(get_vale_conf.clone_repo_and_copy_paths({}))

        run.assert_not_called()

    def test_clone_failure_returns_false(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch.object(
                get_vale_conf.tempfile, "mkdtemp", return_value=temp_dir
            ), patch.object(
                get_vale_conf.subprocess,
                "run",
                side_effect=CalledProcessError(1, ["git", "clone"], stderr="failed"),
            ):
                self.assertFalse(
                    get_vale_conf.clone_repo_and_copy_paths(
                        {"vale.ini": str(Path(temp_dir) / "destination.ini")}
                    )
                )

    def test_clone_copies_requested_files_and_cleans_up(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            clone_dir = Path(temp_dir) / "clone"
            destination = Path(temp_dir) / "destination.ini"

            def create_clone(_command, **_kwargs):
                clone_dir.mkdir()
                (clone_dir / "vale.ini").write_text("cloned configuration")
                return SimpleNamespace(stdout="")

            with patch.object(
                get_vale_conf.tempfile, "mkdtemp", return_value=str(clone_dir)
            ), patch.object(
                get_vale_conf.subprocess, "run", side_effect=create_clone
            ):
                result = get_vale_conf.clone_repo_and_copy_paths(
                    {"vale.ini": str(destination)}
                )

            self.assertTrue(result)
            self.assertEqual(destination.read_text(), "cloned configuration")
            self.assertFalse(clone_dir.exists())

    def test_clone_reports_missing_requested_source_and_cleans_up(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            clone_dir = Path(temp_dir) / "clone"

            def create_clone(_command, **_kwargs):
                clone_dir.mkdir()
                return SimpleNamespace(stdout="")

            with patch.object(
                get_vale_conf.tempfile, "mkdtemp", return_value=str(clone_dir)
            ), patch.object(
                get_vale_conf.subprocess, "run", side_effect=create_clone
            ):
                result = get_vale_conf.clone_repo_and_copy_paths(
                    {"missing.ini": str(Path(temp_dir) / "destination.ini")}
                )

            self.assertFalse(result)
            self.assertFalse(clone_dir.exists())


class MainTests(unittest.TestCase):
    def test_overwrite_is_enabled_by_default(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch.object(get_vale_conf, "SPHINX_DIR", temp_dir), patch.object(
                get_vale_conf,
                "clone_repo_and_copy_paths",
                return_value=True,
            ) as clone, patch.object(sys, "argv", ["get_vale_conf.py"]):
                self.assertEqual(get_vale_conf.main(), 0)

            clone.assert_called_once()
            self.assertTrue(clone.call_args.kwargs["overwrite"])

    def test_no_overwrite_flag_is_passed_to_clone_operation(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch.object(get_vale_conf, "SPHINX_DIR", temp_dir), patch.object(
                get_vale_conf,
                "clone_repo_and_copy_paths",
                return_value=True,
            ) as clone, patch.object(
                sys, "argv", ["get_vale_conf.py", "--no-overwrite"]
            ):
                self.assertEqual(get_vale_conf.main(), 0)

            clone.assert_called_once()
            self.assertFalse(clone.call_args.kwargs["overwrite"])

    def test_failed_clone_returns_nonzero(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch.object(get_vale_conf, "SPHINX_DIR", temp_dir), patch.object(
                get_vale_conf,
                "clone_repo_and_copy_paths",
                return_value=False,
            ), patch.object(sys, "argv", ["get_vale_conf.py"]):
                self.assertEqual(get_vale_conf.main(), 1)


if __name__ == "__main__":
    unittest.main()
