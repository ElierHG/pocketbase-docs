This is the older PocketBase <= 0.22.x version of the website. For the latest PocketBase v0.23+ docs please [click here](https://pocketbase.io/). 

[![PocketBase logo](./js-routing_files/logo.svg) Pocket **Base** v0.22.31](https://pocketbase.io/old/)

__

Extend with JavaScript - Routing

You can register custom routes and middlewares by using the top-level `routerAdd()` and `routerUse()` functions.

  * [Routes](./js-routing.md#routes)
    * [Registering new routes](./js-routing.md#registering-new-routes)
    * [Request context store](./js-routing.md#request-context-store)
    * [Retrieving the current auth state](./js-routing.md#retrieving-the-current-auth-state)
    * [Reading path parameters](./js-routing.md#reading-path-parameters)
    * [Reading query parameters](./js-routing.md#reading-query-parameters)
    * [Reading request headers](./js-routing.md#reading-request-headers)
    * [Writing response headers](./js-routing.md#writing-response-headers)
    * [Reading request body](./js-routing.md#reading-request-body)
    * [Writing response body](./js-routing.md#writing-response-body)
  * [Middlewares](./js-routing.md#middlewares)
    * [Builtin middlewares](./js-routing.md#builtin-middlewares)
    * [Custom middlewares](./js-routing.md#custom-middlewares)
  * [Error response](./js-routing.md#error-response)
  * [Helpers](./js-routing.md#helpers)
    * [Auth response](./js-routing.md#auth-response)
    * [Enrich record(s)](./js-routing.md#enrich-records)
    * [Serving static files](./js-routing.md#serving-static-files)
  * [Sending request to custom routes using the SDKs](./js-routing.md#sending-request-to-custom-routes-using-the-sdks)

### [ Routes ](./js-routing.md#routes)

##### [ Registering new routes ](./js-routing.md#registering-new-routes)

Each route consists of at least a path and a handler function. For example, the below code registers `GET /hello/:name` route that responds with a json body:

```javascript
routerAdd("GET", "// hello// :name", (c) => {
            let name = c.pathParam("name") return c.json(200, {
                "message": "Hello " + name
            })
        }, // * optional middlewares *// );
```

__

To avoid collisions with future internal routes you should avoid using the `/api/...` base path or consider combining it with a unique prefix like `/api/myapp/...`.

Each handler function receives a **request context** argument (usually named `c`).   
The request context is also accessible in the event request hooks under the `httpContext` key.   
Below you can find common request context operations.

##### [ Request context store ](./js-routing.md#request-context-store)

The request context comes with a local store that you can use to share data related only to the current request between routes and middlewares.

```javascript
/ store for the duration of the request c.set("someKey", 123) / / retrieve later
const val = c.get("someKey") // 123;
```

##### [ Retrieving the current auth state ](./js-routing.md#retrieving-the-current-auth-state)

We also use the store to manage the current auth state with the `admin` and `authRecord` special keys.

```javascript
const admin = c.get("admin") // empty if not authenticated as admin const;
record = c.get("authRecord") // empty if not authenticated as regular auth record // alternatively, you can also read the auth state from the cached request info const;
info = $apis.requestInfo(c);
const admin = info.admin;
// empty if not authenticated as admin const record = info.authRecord;
// empty if not authenticated as regular auth record const isGuest = !admin && !record;
```

##### [ Reading path parameters ](./js-routing.md#reading-path-parameters)

Path parameters are defined with `:paramName` placeholder and can be retrieved using `c.pathParam("paramName")`.

```javascript
const id = c.pathParam("id");
```

##### [ Reading query parameters ](./js-routing.md#reading-query-parameters)

```javascript
const search = c.queryParam("search") // or via the cached request object const;
search = $apis.requestInfo(c).query.search;
```

##### [ Reading request headers ](./js-routing.md#reading-request-headers)

```javascript
const token = c.request().header.get("Some-Header") // or via the cached request object (the header value is always normalized) const;
token = $apis.requestInfo(c).headers["some_header"];
```

##### [ Writing response headers ](./js-routing.md#writing-response-headers)

```
c.response().header().set("Some-Header", "123")
```

##### [ Reading request body ](./js-routing.md#reading-request-body)

```javascript
/ read the body via the cached request object / / (this method is commonly used in hook handlers because it allows reading the body more than once) const data = $apis.requestInfo(c).data console.log(data.title) // read// scan the request body fields into a typed object // (note that a body cannot be read twice with "bind" because it is a stream) const;
data = new DynamicModel({ // describe the fields to read (used also as initial values) someTextField: "", someNumberField: 0, someBoolField: false, someArrayField: [], someObjectField: {}, // object props are accessible via .get(key) }) c.bind(data) console.log(data.sometextField) // read single multipart// form-data field const;
            title = c.formValue("title") // read single multipart// form-data file const;
            doc = c.formFile("document");
```

##### [ Writing response body ](./js-routing.md#writing-response-body)

```
/ send response with json body c.json(200, {"name": "John"}) / send response with string body c.string(200, "Lorem ipsum...") / send response with html body / (check also the "Rendering templates" section) c.html(200, "<h1>Hello!</h1>") / redirect c.redirect(307, "https://example.com") / send response with no body c.noContent(204)
```

### [ Middlewares ](./js-routing.md#middlewares)

Middlewares could be used to apply a shared behavior or to intercept and modify route requests.   
Middlewares can be registered both to a single route (by passing them after the handler) and globally usually by using `routerUse(someMiddlereFunc)`.

```javascript
/ attach a middleware globally to all routes routerUse(someMiddlereFunc) / / attach multiple middlewares to a single route // each route will execute their own middlewares + the global ones routerAdd("GET", "// hello", (c) => { return c.string(200, "Hello world!") }, $apis.activityLogger($app), $apis.requireAdminAuth())
```

##### [ Builtin middlewares ](./js-routing.md#builtin-middlewares)

```javascript
/ logs the request in the Admin UI > Logs $apis.activityLogger($app) / / requires the request client to be unauthenticated, aka.guest $apis.requireGuestOnly() // requires the request client to be authenticated as an auth record $apis.requireRecordAuth(optCollectionNames...) // require the request client to be authenticated as admin $apis.requireAdminAuth() // require the request client to be authenticated as admin OR auth record $apis.requireAdminOrRecordAuth(optCollectionNames...) // require the request client to be authenticated as admin OR auth record // that matches the ownerIdParam path parameter $apis.requireAdminOrOwnerAuth(ownerIdParam = "id") // compresses HTTP response using gzip $apis.gzip() // sets the maximum allowed size (in bytes) for a request body $apis.bodyLimit(bytes);
```

##### [ Custom middlewares ](./js-routing.md#custom-middlewares)

```javascript
function myCustomMiddleware(next) {
    return (c) => { // eg. inspect some header value before processing the request const header = c.request().header.get("Some-Header") if (!header) { // throw or return an error throw new BadRequestError("Invalid request") } return next(c) // proceed with the request chain } } routerUse(myCustomMiddleware);
```

### [ Error response ](./js-routing.md#error-response)

PocketBase has a global error handler and every returned or thrown `Error` from a route or middleware will be safely converted by default to a generic HTTP 400 error to avoid accidentally leaking sensitive information (the original error will be visible only in the _Admin UI > Logs_ or when in `--dev` mode).

To make it easier returning formatted json error responses, PocketBase provides `ApiError` constructor that can be instantiated directly or using the builtin factories.   
`ApiError.data` will be returned in the response only if it is a map of `ValidationError` items.

```javascript
/ construct ApiError with custom status code and validation data error throw new ApiError(500, "something went wrong", { "title": new ValidationError("invalid_title", "Invalid or missing title"), }) / /
if message is empty string, a
default one will be set throw new BadRequestError(optMessage, optData) // 400 ApiError throw new UnauthorizedError(optMessage, optData) // 401 ApiError throw new ForbiddenError(optMessage, optData) // 403 ApiError throw new NotFoundError(optMessage, optData) // 404 ApiError
```

### [ Helpers ](./js-routing.md#helpers)

The global `$apis` namespace expose several helpers you can use as part of your route hooks.

##### [ Auth response ](./js-routing.md#auth-response)

`$apis.recordAuthResponse()` writes standardised json record auth response (aka. token + record data) into the specified request context. Could be used as a return result from a custom auth route.

```javascript
routerAdd("GET", "// phone-login", (c) => {
    const data = new DynamicModel({
        phone: "",
        password: "",
    }) c.bind(data) const;
    record = $app.dao().findFirstRecordByData("users", "phone", data.phone) if (!record.validatePassword(data.password)) {
        throw new BadRequestError("invalid credentials")
    }
    return $apis.recordAuthResponse($app, c, record)
}, $apis.activityLogger($app));
```

##### [ Enrich record(s) ](./js-routing.md#enrich-records)

`$apis.enrichRecord()` and `$apis.enrichRecords()` helpers parses the request context and enrich the provided record(s) by:

  * expands relations (if `defaultExpands` and/or `?expand` query parameter is set)
  * ensures that the emails of the auth record and its expanded auth relations are visible only for the current logged admin, record owner or record with manage access

```javascript
routerAdd("GET", "// custom-article", (c) => {
            const records = $app.dao().findRecordsByFilter("article", "status = 'active'", '-created', 40) // enrich the records with the "categories" relation as default expand $apis.enrichRecords(c, $app.dao(), records, "categories") return c.json(200, records) }, $apis.activityLogger($app));
```

##### [ Serving static files ](./js-routing.md#serving-static-files)

```
routerAdd("GET", "/*", $apis.staticDirectoryHandler("/path/to/public", false))
```

### [ Sending request to custom routes using the SDKs ](./js-routing.md#sending-request-to-custom-routes-using-the-sdks)

The official PocketBase SDKs expose the internal `send()` method that could be used to send requests to your custom route(s).

JavaScript

Dart

```javascript
import PocketBase from 'pocketbase';
const pb = new PocketBase('http://127.0.0.1:8090');
await pb.send("// old// hello", { // for all possible options check // https://developer.mozilla.org// en-US// docs// Web// API// fetch#options query: { "abc": 123 }, });
```

```
import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); await pb.send("/old/hello", query: { "abc": 123 })
```

[FAQ](https://pocketbase.io/old/faq) [Discussions](https://github.com/pocketbase/pocketbase/discussions) [Documentation](https://pocketbase.io/old/docs) [JavaScript SDK](https://github.com/pocketbase/js-sdk) [Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket **Base**

[__](mailto:support@pocketbase.io)[__](https://twitter.com/pocketbase)[__](https://github.com/pocketbase/pocketbase)

© 2023-2025 Pocket **Base** The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)

__

Extend with JavaScript - Routing - Docs - PocketBase
