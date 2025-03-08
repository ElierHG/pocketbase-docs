This is the older PocketBase <= 0.22.x version of the website. For the latest PocketBase v0.23+ docs please [click here](https://pocketbase.io/). 

[![PocketBase logo](./js-rendering-templates_files/logo.svg) Pocket **Base** v0.22.31](https://pocketbase.io/old/)

__

Extend with JavaScript - Rendering templates

  * [Overview](./js-rendering-templates.md#overview)
  * [Example HTML page with layout](./js-rendering-templates.md#example-html-page-with-layout)

### [ Overview ](./js-rendering-templates.md#overview)

A common task when creating custom routes or emails is the need of generating HTML output. To assist with this, PocketBase provides the global `$template` helper for parsing and rendering HTML templates.

`const html = $template.loadFiles( `${__hooks}/views/base.html`, `${__hooks}/views/partial1.html`, `${__hooks}/views/partial2.html
```
, ).render(data)
```

The general flow when working with composed and nested templates is that you create "base" template(s) that defines various placeholders using the `{{template "placeholderName" .}}` or `{{block "placeholderName" .}}default...{{end}}` actions.

Then in the partials, you define the content for those placeholders using the `{{define "placeholderName"}}custom...{{end}}` action.

The dot object (`.`) in the above represents the data passed to the templates via the `render(data)` method.

By default the templates apply contextual (HTML, JS, CSS, URI) auto escaping so the generated template content should be injection-safe. To render raw/verbatim trusted content in the templates you can use the builtin `raw` function (eg. `{{.content|raw}}`).

__

For more information about the template syntax please refer to the [_html/template_](https://pkg.go.dev/html/template#hdr-A_fuller_picture) and [_text/template_](https://pkg.go.dev/text/template) package godocs. **Another great resource is also the Hashicorp's[Learn Go Template Syntax](https://developer.hashicorp.com/nomad/tutorials/templates/go-template-syntax) tutorial.**

### [ Example HTML page with layout ](./js-rendering-templates.md#example-html-page-with-layout)

Consider the following app directory structure:

```
myapp/ pb_hooks/ views/ layout.html hello.html main.pb.js pocketbase
```

We define the content for `layout.html` as:

```html
<!DOCTYPE html> <html lang="en"> <head> <title>{{block "title" .}}Default app title{{end}}</title> </head> <body> Header... {{block "body" .}} Default app body... {{end}} Footer... </body> </html>
```

We define the content for `hello.html` as:

```html
{{define "title"}} Page 1 {{end}} {{define "body"}} <p>Hello from {{.name}}</p> {{end}}
```

Then to output the final page, we'll register a custom `/hello/:name` route:

`routerAdd("get", "/hello/:name", (c) => { const name = c.pathParam("name") const html = $template.loadFiles( `${__hooks}/views/layout.html`, `${__hooks}/views/hello.html
```
, ).render({ "name": name, }) return c.html(200, html) })
```

[FAQ](https://pocketbase.io/old/faq) [Discussions](https://github.com/pocketbase/pocketbase/discussions) [Documentation](https://pocketbase.io/old/docs) [JavaScript SDK](https://github.com/pocketbase/js-sdk) [Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket **Base**

[__](mailto:support@pocketbase.io)[__](https://twitter.com/pocketbase)[__](https://github.com/pocketbase/pocketbase)

© 2023-2025 Pocket **Base** The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)

__

Extend with JavaScript - Rendering templates - Docs - PocketBase
