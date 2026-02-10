(how-to-guides-manage-snaps-use-the-rest-api)=
# Use the REST API

The REST API provides access to snapd's state and many of its key functions.

See below for details on accessing the API,  authentication, JSON elements and error types, and see the [API reference](reference/api/redoc-static) for which actions can be performed and which elements can be requested.

## Accessing the API

The `/run/snapd.socket` UNIX socket is used to connect a client to the API.

To send a **POST** request with _curl_, for example, the following will ask snapd to install the [hello](https://snapcraft.io/hello) snap from the _edge_ channel:

```bash
sudo curl -sS --unix-socket /run/snapd.socket \
http://localhost/v2/snaps/hello \
-X POST -d '{"action": "install", "channel": "edge"}'
```

Similarly, the following curl command will remove a [quota group](/how-to-guides/manage-snaps/use-resource-quotas) called _allquotas_:

```bash
sudo curl -sS --unix-socket /run/snapd.socket \
http://localhost/v2/quotas \
-X POST -d '{"action": "remove", "group-name": "allquotas"}'
```

A request will return a JSON-formatted object. The following example uses _curl_ to **GET** request the list of installed snaps, piped through _jq_ for formatting:

```bash
$ sudo curl -sS --unix-socket /run/snapd.socket http://localhost/v2/apps \
| jq
{
  "type": "sync",
  "status-code": 200,
  "status": "OK",
  "result": [
    {
      "snap": "anbox-installer",
      "name": "anbox-installer"
    }
  ]
}
```

```{caution}
HTTPS connections over a TCP socket are under consideration for a future release.
```

## Authentication

The API incorporates three levels of access:
- **open**: API requests will succeed without authorisation
- **authenticated**: requires suitable authorisation to be provided with each request
- **root**: root user gains authenticated access without sending authorisation

If an app or client is already running as root, it _does not_ require the use of macaroons or any further authentication. The API will by default allow access to anything that needs to be authenticated.

Authorisation is provided by sending a Macaroon with the HTTP authorisation header. For example:

```no-highlight
Authorization: Macaroon root="serialized-store-macaroon",discharge="discharge-for-macaroon-authentication"
```

If available, [Polkit](https://www.freedesktop.org/wiki/Software/polkit/) can also be used for authentication. The client may choose to allow user interaction for authentication, e.g. showing a graphical dialogue. This is done by setting an HTTP header (defaults to false):

```no-highlight
X-Allow-Interaction: true
```

## Responses

For each request, the following JSON object is returned:

Example:

```json
{
    "type": "sync",
    "status-code": 200,
    "status": "OK",
    "maintenance": { 
        "kind": "system-restart", 
        "message": "system is restarting" 
    }
}
```

#### Fields

* `type`: One of `sync`, `async` or `error`
* `status-code`: HTTP status code matching the HTTP status line
* `status`: HTTP reason phrase matching the HTTP status line
* `maintenance`: JSON object containing maintenance information (_optional_)

#### Maintenance Fields

* `kind`: Kind of maintenance restart, one of `system-restart` or `daemon-restart`
* `message`: Text to show to user

### Synchronous response

For a standard synchronous operation, the following JSON object is returned:

Example:
```javascript
{
    "type": "sync",
    "status-code": 200,
    "status": "OK",
    "result": { "name": "value" }，
}
```

#### Fields

In addition to the standard response fields, the following can also be present:

* `result`: Result from the request. This can be any JSON structure and is commonly either an object or an array.

### Asynchronous Response

When a request takes time to complete, an asynchronous response is returned.

The request is assigned a change id, which can be checked by requesting `GET /v2/changes/[id]`.

Example:
```javascript
{
    "type": "async",
    "status-code": 202,
    "status": "Accepted",
    "change": "401",
}
```

#### Fields

In addition to the standard response fields the following can be present:

* `change`: identifier for the change in progress

## Error response

If a request cannot be completed, an error response is returned.

Example:

```javascript
{
    "type": "error",
    "status-code": 401,
    "status": "Unauthorized",
    "result": {
        "message": "access denied",
        "kind": "login-required",
    }
}
```

#### Fields

In addition to the standard response fields the following can be present:

* `result`: Error information

#### Result Fields

* `message`: Description of the error, suitable for displaying to a user
* `kind`: Unique code for the error, to enable a snapd client to display appropriate behaviour (_optional_)
* `value`: extra information on the error, typically a string for the snap name or an object with fields dependent on the kind (_optional_)

