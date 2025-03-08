This is the older PocketBase <= 0.22.x version of the website. For the latest PocketBase v0.23+ docs please [click here](https://pocketbase.io/). 

[![PocketBase logo](./js-logging_files/logo.svg) Pocket **Base** v0.22.31](https://pocketbase.io/old/)

__

Extend with JavaScript - Logging

`$app.logger()` could be used to writes any logs into the database so that they can be later explored from the PocketBase _Admin UI > Logs_ section.

__

For better performance and to minimize blocking on hot paths, note that logs are written with debounce and on batches:

  * 3 seconds after the last debounced log write
  * when the batch threshold is reached (currently 200)
  * right before app termination to attempt saving everything from the existing logs queue

  * [Logger methods](./js-logging.md#logger-methods)
    * [debug(message, attrs...)](./js-logging.md#debugmessage-attrs-)
    * [info(message, attrs...)](./js-logging.md#infomessage-attrs-)
    * [warn(message, attrs...)](./js-logging.md#warnmessage-attrs-)
    * [error(message, attrs...)](./js-logging.md#errormessage-attrs-)
    * [with(attrs...)](./js-logging.md#withattrs-)
    * [withGroup(name)](./js-logging.md#withgroupname)
  * [Logs settings](./js-logging.md#logs-settings)

### [ Logger methods ](./js-logging.md#logger-methods)

All standard [`slog.Logger`](https://pocketbase.io/docs/jsvm/) methods are available but below is a list with some of the most notable ones. Note that attributes are represented as key-value pair arguments.

##### [ debug(message, attrs...) ](./js-logging.md#debugmessage-attrs-)

```javascript
$app.logger().debug("Debug message!") $app.logger().debug("Debug message with attributes!", "name", "John Doe", "id", 123, )
```

##### [ info(message, attrs...) ](./js-logging.md#infomessage-attrs-)

```javascript
$app.logger().info("Info message!") $app.logger().info("Info message with attributes!", "name", "John Doe", "id", 123, )
```

##### [ warn(message, attrs...) ](./js-logging.md#warnmessage-attrs-)

```javascript
$app.logger().warn("Warning message!") $app.logger().warn("Warning message with attributes!", "name", "John Doe", "id", 123, )
```

##### [ error(message, attrs...) ](./js-logging.md#errormessage-attrs-)

```javascript
$app.logger().error("Error message!") $app.logger().error("Error message with attributes!", "id", 123, "error", err, )
```

##### [ with(attrs...) ](./js-logging.md#withattrs-)

`with(atrs...)` creates a new local logger that will "inject" the specified attributes with each following log.

```javascript
const l = $app.logger().with("total", 123) // results in log with data {"total": 123} l.info("message A") // results in log with data {"total": 123, "name": "john"} l.info("message B", "name", "john");
```

##### [ withGroup(name) ](./js-logging.md#withgroupname)

`withGroup(name)` creates a new local logger that wraps all logs attributes under the specified group name.

```javascript
const l = $app.logger().withGroup("sub") // results in log with data {"sub": { "total": 123 }} l.info("message A", "total", 123);
```

### [ Logs settings ](./js-logging.md#logs-settings)

You can control various log settings like logs retention period, minimal log level, request IP logging, etc. from the logs settings panel:

![Logs settings screenshot](./js-logging_files/logs.png)

[FAQ](https://pocketbase.io/old/faq) [Discussions](https://github.com/pocketbase/pocketbase/discussions) [Documentation](https://pocketbase.io/old/docs) [JavaScript SDK](https://github.com/pocketbase/js-sdk) [Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket **Base**

[__](mailto:support@pocketbase.io)[__](https://twitter.com/pocketbase)[__](https://github.com/pocketbase/pocketbase)

© 2023-2025 Pocket **Base** The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)

__

Extend with JavaScript - Logging - Docs - PocketBase
