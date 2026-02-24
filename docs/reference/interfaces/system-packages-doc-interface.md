(interfaces-system-packages-doc)=
#  system-packages-doc interface

The `system-packages-doc` interface permits access file system locations used to store system documentation. These include the following

* `/usr/{,local/}share/doc/`
* `/usr/share/cups/doc-root/`
* `/usr/share/gimp/2.0/help/`
* `/usr/share/gtk-doc/`
* `/usr/share/javascript/`
* `/usr/share/libreoffice/help/`
* `/usr/share/sphinx_rtd_theme/`
* `/usr/share/xubuntu-docs/	`

After the interface has been connected, the host’s `/usr/share/doc` directory replaces the `/usr/share/doc` for the context of the snap.

This interface is helpful for *web browsers*, for example, because it enables them to open and view the host’s HTML system documentation.

## Developer details

**Auto-connect**: no

The interface it is not connected automatically because the listed documentation can be used to infer which packages are installed on the host system.

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/system_packages_doc_test.go

The source code for the interface is in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/system_packages_doc.go

