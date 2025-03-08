This is the older PocketBase <= 0.22.x version of the website. For the latest PocketBase v0.23+ docs please [click here](https://pocketbase.io/). 

[![PocketBase logo](./js-job-scheduling_files/logo.svg) Pocket **Base** v0.22.31](https://pocketbase.io/old/)

__

Extend with JavaScript - Jobs scheduling

If you have tasks that need to be performed periodically, you could setup crontab-like jobs with `cronAdd(name, expr, handler)`.

Each scheduled job runs in its own goroutine as part of the `serve` command process and must have:

  * name - identifier for the scheduled job; could be used to replace or remove an existing job
  * cron expression like `0 0 * * *` ( _supports numeric list, steps, ranges or macros _)
  * handler - the function that will be executed everytime when the job runs

Here is an example:

```javascript
/ prints "Hello!" every 2 minutes cronAdd("hello", "*/ / 2 * * * * ", () => { console.log("
Hello!") })
```

To remove a single registered cron job you can call `cronRemove(name)`.

[FAQ](https://pocketbase.io/old/faq) [Discussions](https://github.com/pocketbase/pocketbase/discussions) [Documentation](https://pocketbase.io/old/docs) [JavaScript SDK](https://github.com/pocketbase/js-sdk) [Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket **Base**

[__](mailto:support@pocketbase.io)[__](https://twitter.com/pocketbase)[__](https://github.com/pocketbase/pocketbase)

© 2023-2025 Pocket **Base** The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)

__

Extend with JavaScript - Jobs scheduling - Docs - PocketBase
