This is the older PocketBase <= 0.22.x version of the website. For the latest PocketBase v0.23+ docs please [click here](https://pocketbase.io/). 

[![PocketBase logo](./js-sending-emails_files/logo.svg) Pocket **Base** v0.22.31](https://pocketbase.io/old/)

__

Extend with JavaScript - Sending emails

PocketBase provides a simple abstraction for sending emails via the `$app.newMailClient()` helper.

Depending on your configured mail settings ( _Admin UI > Settings > Mail settings_) it will use the `sendmail` command or a SMTP client.

  * [Send custom email](./js-sending-emails.md#send-custom-email)
  * [Intercept system emails](./js-sending-emails.md#intercept-system-emails)

### [ Send custom email ](./js-sending-emails.md#send-custom-email)

You can send your own custom emails from everywhere within your app (hooks, middlewares, routes, etc.) by using `$app.newMailClient().send(message)`. Here is an example of sending a custom email after user registration:

```javascript
onRecordAfterCreateRequest((e) => {
            const message = new MailerMessage({
                        from: {
                            address: $app.settings().meta.senderAddress,
                            name: $app.settings().meta.senderName,
                        },
                        to: [{
                            address: e.record.email()
                        }],
                        subject: "YOUR_SUBJECT...",
                        html: "YOUR_HTML_BODY...", // bcc, cc and custom headers are also supported... }) $app.newMailClient().send(message) }, "users");
```

### [ Intercept system emails ](./js-sending-emails.md#intercept-system-emails)

If you want to change the default system emails for forgotten password, verification, etc., you can adjust the default templates from the _Admin UI > Settings > Mail settings_.

Alternatively, you can also apply individual changes by binding to one of the [mailer hooks](./js-event-hooks.md#mailer-hooks). Here is an example of appending a Record field value to the subject using the `onMailerBeforeRecordResetPasswordSend` hook:

```javascript
onMailerBeforeRecordResetPasswordSend().add((e) => { // modify the subject e.message.subject += (" " + e.record.get("name")) })
```

[FAQ](https://pocketbase.io/old/faq) [Discussions](https://github.com/pocketbase/pocketbase/discussions) [Documentation](https://pocketbase.io/old/docs) [JavaScript SDK](https://github.com/pocketbase/js-sdk) [Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket **Base**

[__](mailto:support@pocketbase.io)[__](https://twitter.com/pocketbase)[__](https://github.com/pocketbase/pocketbase)

© 2023-2025 Pocket **Base** The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)

__

Extend with JavaScript - Sending emails - Docs - PocketBase
