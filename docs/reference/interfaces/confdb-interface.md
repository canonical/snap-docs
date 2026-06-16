(interfaces-confdb)=
#  confdb interface

The `confdb` interface enables snaps to access to specific  {ref}`confdb <ref-confdb-configuration-mechanism_confdb-views>` views.

There are two fields that together identify the view being accessed: `account` and `view`. There is also an optional `role` field which may only take the value of "custodian", if the snap is a custodian for the confdb-schema being accessed.

See the {ref}`Confdb configuration mechanism <explanation-how-snaps-work-confdb-configuration-mechanism>` for implementation details, and {ref}`Configure snaps with confdb <how-to-guides-manage-snaps-configure-snaps-with-confdb>` to use confdb with your own snaps.

```
[...]
 sensors-sensor1-state:
  interface: confdb
  account: acme
  view: sensors/sensor1-state
```

```{warning}
 Confdb is currently considered an {ref}`Experimental feature <ref-experimental-features_experimental-features>` and implementation details may change as development progresses.
```

## Developer details

**Auto-connect**: no, but plugs are auto-connected if the confdb's account is the same as the snap's publisher.

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/confdb_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/confdb.go

