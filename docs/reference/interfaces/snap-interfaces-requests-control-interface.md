(interfaces-snap-interfaces-requests-control)=
# The snap-interfaces-requests-control interface

The `snap_interfaces_requests_control` interface enables the prompting API and its access to prompting-related notice types. This is used internally by snapd to request and manage system resource access.

```{tip}

See [Interface management](/) and [Supported interfaces](/interfaces/index) for further details on how interfaces are used.

```

---

<h2 id='heading--dev-details'>Developer details </h2>

**Auto-connect**: no

<h3 id='heading--endpoint-access'>Endpoint access permissions</h3>
<ul>
<li>/v2/system-info</li>
<li>/v2/icons/{name}/icon</li>
<li>/v2/notices</li>
<li>/v2/notices/{id}</li>
<li>/v2/snaps/{name}</li>
<li>/v2/interfaces/requests/prompts</li>
<li>/v2/interfaces/requests/prompts/{id}</li>
<li>/v2/interfaces/requests/rules</li>
<li>/v2/interfaces/requests/rules/{id}</li>
</ul>

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/snapcore/snapd/blob/master/interfaces/builtin/snap_interfaces_requests_control_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/snapcore/snapd/blob/master/interfaces/builtin/snap_interfaces_requests_control.go

