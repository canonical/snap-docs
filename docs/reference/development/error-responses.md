(reference-development-rest-api-error-responses)=
# Error responses

When {ref}`Using the snapd REST API <how-to-guides-manage-snaps-use-the-rest-api>`, requests sent to the {ref}`snapd REST API <reference-development-snapd-rest-api>` can return both standard HTTP error responses, and a snapd-specific _error kind_, in the body of the response. These are detailed below.

## Status codes

The REST API returns standard HTTP error response status ranges and codes, such as _4xx_ for client errors and _5xx_ for server side issues, with descriptions. For example:

| Code | Status                | Example description                         |
|------|-----------------------|---------------------------------------------|
| 400  | Bad request           | Snap is already installed                   |
| 400  | Bad request           | Snap is not installed / unknown action      |
| 401  | Unauthorized          | Access denied. Login required.              |
| 403  | Forbidden             | Access denied. Login required.              |
| 404  | Not found             | Channel not available / snap does not exist |
| 409  | Conflict              |     Snap *snap* has *change-kind* change in progress  |
| 500  | Internal server error | *many unexpected errors* |                           |

Conflict errors (409) may be temporary. They are often returned when a new operation on an entity cannot be initiated because a previous operation is still in progress. This might cause new operations on one or more snaps to see errors with the `snap-change-conflict` error kind, for example.  When a conflicting operation completes, new operations may be retried and should later succeed, assuming the completed operation didn't break any dependent state for the new operation.

## Error kinds

The following error `kind` values provide extra context on an error response:

* `app-not-found`: the requested app couldn't be found.
* `assertion-not-found`: assertion can not be found.
* `auth-cancelled`: authentication was cancelled by the user.
* `bad-query`: a bad query was provided.
* `dns-failure`: DNS not responding.
* `insufficient-disk-space`: returned when {ref}`disk space awareness <how-to-guides-manage-snaps-disk-space-awareness>` is enabled and either an install, remove or refresh operation fails due to insufficient free disk space. The error `value`  is an object that contains `snap-names`, an array of affected snaps, and a `change-kind` string with the failed operation.
* `interfaces-unchanged`: the requested interfaces' operation would have no effect.
* `invalid-auth-data`: the authentication data provided failed to validate (e.g. a malformed email address). The `value` of the error is an object with a key per failed field and a list of the failures on each field.
* `login-required`: the requested operation cannot be performed without an authenticated user. This is the kind of any other 401 Unauthorized response.
* `network-timeout`: a timeout occurred during the request.
* `option-not-found`: the given configuration option does not exist.
* `password-policy`: provided password doesn't meet system policy.
* `snap-already-installed`: the requested snap is already installed.
* `snap-architecture-not-available`: no snap revision on specified architecture. Value has the same format as for `snap-channel-not-available`.
* `snap-change-conflict`: the requested operation would conflict with currently ongoing change. This is a temporary error. The error `value` is an object with optional fields `snap-name`, `change-kind` of the ongoing change.
* `snap-channel-not-available`: no snap revision on specified channel. The `value` of the error is a rich object with requested `snap-name`, `action`, `channel`, `architecture`, and actually available `releases` as list of `{"architecture":... , "channel": ...}` objects.
* `snap-local`: cannot perform operation on local snap.
* `snap-needs-classic`: the requested snap needs classic confinement to be installed.
* `snap-needs-classic-system`: the requested snap can't be installed on the current non-classic system.
* `snap-needs-devmode`: the requested snap needs devmode to be installed.
* `snap-no-update-available`: the requested snap does not have an update available.
* `snap-not-a-snap`: the given snap or directory does not look like a snap.
* `snap-not-classic`: snap not compatible with classic mode.
* `snap-not-found`: the requested snap couldn't be found.
* `snap-not-installed`: the requested snap is not installed.
* `snap-revision-not-available`: no snap revision available as specified.
* `two-factor-failed`: the OTP provided wasn't recognised.
* `two-factor-required`: the client needs to retry the `login` command including an OTP.
* `unsuccessful`: snapctl command was unsuccessful.
* `validation-set-not-found`: the validation set cannot be found.
* `apparmor-prompting-not-running`: AppArmor prompting is not running.
* `interfaces-requests-*`: errors specific to AppArmor prompting client interactions (e.g., so no such rule, rule already exists, etc).

## <h3 id='heading--maint-errors'>Maintenance error kinds</h3>

These are used only inside the `maintenance` field of responses.

* `daemon-restart`: daemon is restarting.
* `system-restart`: system is restarting.

