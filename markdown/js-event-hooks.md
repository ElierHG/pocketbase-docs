This is the older PocketBase <= 0.22.x version of the website. For the latest PocketBase v0.23+ docs please [click here](https://pocketbase.io/). 

[![PocketBase logo](./js-event-hooks_files/logo.svg) Pocket **Base** v0.22.31](https://pocketbase.io/old/)

__

Extend with JavaScript - Event hooks

You can extend the default PocketBase behavior with custom server-side code using the exposed JavaScript app level hooks.

Throwing an error or returning `false` inside a hook handler function stops the hook execution chain.

  * [App hooks](./js-event-hooks.md#app-hooks)
  * [DB hooks](./js-event-hooks.md#db-hooks)
  * [Mailer hooks](./js-event-hooks.md#mailer-hooks)
  * [Record CRUD API hooks](./js-event-hooks.md#record-crud-api-hooks)
  * [Record Auth API hooks](./js-event-hooks.md#record-auth-api-hooks)
  * [Realtime API hooks](./js-event-hooks.md#realtime-api-hooks)
  * [File API hooks](./js-event-hooks.md#file-api-hooks)
  * [Collection API hooks](./js-event-hooks.md#collection-api-hooks)
  * [Settings API hooks](./js-event-hooks.md#settings-api-hooks)
  * [Admin CRUD API hooks](./js-event-hooks.md#admin-crud-api-hooks)
  * [Admin Auth API hooks](./js-event-hooks.md#admin-auth-api-hooks)

### [ App hooks ](./js-event-hooks.md#app-hooks)

**[onBeforeBootstrap](./js-event-hooks.md#onbeforebootstrap)**

`onBeforeBootstrap` hook is triggered before initializing the main application resources (eg. before db open and initial settings load). 

```javascript
onBeforeBootstrap((e) => {
    console.log(e.app)
})
```

 **[onAfterBootstrap](./js-event-hooks.md#onafterbootstrap)**

`onAfterBootstrap` hook is triggered after initializing the main application resources (eg. after db open and initial settings load). 

```javascript
onAfterBootstrap((e) => {
    console.log(e.app)
})
```

 **[onBeforeApiError](./js-event-hooks.md#onbeforeapierror)**

`onBeforeApiError` hook is triggered right before sending an error API response to the client, allowing you to further modify the error data or to return a completely different API response. 

```javascript
onBeforeApiError((e) => {
    console.log(e.httpContext) console.log(e.error)
})
```

 **[onAfterApiError](./js-event-hooks.md#onafterapierror)**

`onAfterApiError` hook is triggered right after sending an error API response to the client. It could be used for example to log the final API error in external services. 

```javascript
onAfterApiError((e) => {
    console.log(e.httpContext) console.log(e.error)
})
```

 **[onTerminate](./js-event-hooks.md#onterminate)**

`onTerminate` hook is triggered when the app is in the process of being terminated (eg. on `SIGTERM` signal).   
Note that the app could be terminated abruptly without awaiting the hook completion. 

```javascript
onTerminate((e) => {
    console.log("terminating...")
})
```

### [ DB hooks ](./js-event-hooks.md#db-hooks)

**[onModelBeforeCreate](./js-event-hooks.md#onmodelbeforecreate)**

`onModelBeforeCreate` hook is triggered before inserting a new model in the DB, allowing you to modify or validate the stored data. 

If the optional "tags" list (table names and/or the Collection id for Record models) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every db model onModelBeforeCreate((e) => { console.log(e.model.tableName()) console.log(e.model.id) }) / / fires only
for "users"
and "members"
onModelBeforeCreate((e) => {
    console.log(e.model.tableName()) console.log(e.model.id)
}, "users", "members")
```

 **[onModelAfterCreate](./js-event-hooks.md#onmodelaftercreate)**

`onModelAfterCreate` hook is triggered after successfully inserting a new model in the DB. 

If the optional "tags" list (table names and/or the Collection id for Record models) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every db model onModelAfterCreate((e) => { console.log(e.model.tableName()) console.log(e.model.id) }) / / fires only
for "users"
and "members"
onModelAfterCreate((e) => {
    console.log(e.model.tableName()) console.log(e.model.id)
}, "users", "members")
```

 **[onModelBeforeUpdate](./js-event-hooks.md#onmodelbeforeupdate)**

`onModelBeforeUpdate` hook is triggered before updating existing model in the DB, allowing you to modify or validate the stored data. 

If the optional "tags" list (table names and/or the Collection id for Record models) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every db model onModelBeforeUpdate((e) => { console.log(e.model.tableName()) console.log(e.model.id) }) / / fires only
for "users"
and "members"
onModelBeforeUpdate((e) => {
    console.log(e.model.tableName()) console.log(e.model.id)
}, "users", "members")
```

 **[onModelAfterUpdate](./js-event-hooks.md#onmodelafterupdate)**

`onModelAfterUpdate` hook is triggered after successfully updating existing model in the DB. 

If the optional "tags" list (table names and/or the Collection id for Record models) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every db model onModelAfterUpdate((e) => { console.log(e.model.tableName()) console.log(e.model.id) }) / / fires only
for "users"
and "members"
onModelAfterUpdate((e) => {
    console.log(e.model.tableName()) console.log(e.model.id)
}, "users", "members")
```

 **[onModelBeforeDelete](./js-event-hooks.md#onmodelbeforedelete)**

`onModelBeforeDelete` hook is triggered before deleting an existing model from the DB. 

If the optional "tags" list (table names and/or the Collection id for Record models) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every db model onModelBeforeDelete((e) => { console.log(e.model.tableName()) console.log(e.model.id) }) / / fires only
for "users"
and "members"
onModelBeforeDelete((e) => {
    console.log(e.model.tableName()) console.log(e.model.id)
}, "users", "members")
```

 **[onModelAfterDelete](./js-event-hooks.md#onmodelafterdelete)**

`onModelAfterDelete` hook is triggered after successfully deleting an existing model from the DB. 

If the optional "tags" list (table names and/or the Collection id for Record models) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every db model onModelAfterDelete((e) => { console.log(e.model.tableName()) console.log(e.model.id) }) / / fires only
for "users"
and "members"
onModelAfterDelete((e) => {
    console.log(e.model.tableName()) console.log(e.model.id)
}, "users", "members")
```

### [ Mailer hooks ](./js-event-hooks.md#mailer-hooks)

**[onMailerBeforeAdminResetPasswordSend](./js-event-hooks.md#onmailerbeforeadminresetpasswordsend)**

`onMailerBeforeAdminResetPasswordSend` hook is triggered right before sending a password reset email to an admin, allowing you to inspect and customize the email message that is being sent. 

```javascript
onMailerBeforeAdminResetPasswordSend((e) => {
            console.log(e.mailClient) console.log(e.message) console.log(e.admin) console.log(e.meta) // change the mail subject e.message.subject = "new subject" });
```

 **[onMailerAfterAdminResetPasswordSend](./js-event-hooks.md#onmailerafteradminresetpasswordsend)**

`onMailerAfterAdminResetPasswordSend` hook is triggered after admin password reset email was successfully sent. 

```javascript
onMailerAfterAdminResetPasswordSend((e) => {
    console.log(e.mailClient) console.log(e.message) console.log(e.admin) console.log(e.meta)
})
```

 **[onMailerBeforeRecordResetPasswordSend](./js-event-hooks.md#onmailerbeforerecordresetpasswordsend)**

`onMailerBeforeRecordResetPasswordSend` hook is triggered right before sending a password reset email to an auth record, allowing you to inspect and customize the email message that is being sent. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
onMailerBeforeRecordResetPasswordSend((e) => {
            console.log(e.mailClient) console.log(e.message) console.log(e.record) console.log(e.meta) // change the mail subject e.message.subject = "new subject" });
```

 **[onMailerAfterRecordResetPasswordSend](./js-event-hooks.md#onmailerafterrecordresetpasswordsend)**

`onMailerAfterRecordResetPasswordSend` hook is triggered after an auth record password reset email was successfully sent. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
onMailerAfterRecordResetPasswordSend((e) => {
    console.log(e.mailClient) console.log(e.message) console.log(e.record) console.log(e.meta)
})
```

 **[onMailerBeforeRecordVerificationSend](./js-event-hooks.md#onmailerbeforerecordverificationsend)**

`onMailerBeforeRecordVerificationSend` hook is triggered right before sending a verification email to an auth record, allowing you to inspect and customize the email message that is being sent. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
onMailerBeforeRecordVerificationSend((e) => {
            console.log(e.mailClient) console.log(e.message) console.log(e.record) console.log(e.meta) // change the mail subject e.message.subject = "new subject" });
```

 **[onMailerAfterRecordVerificationSend](./js-event-hooks.md#onmailerafterrecordverificationsend)**

`onMailerAfterRecordVerificationSend` hook is triggered after a verification email was successfully sent to an auth record. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
onMailerAfterRecordVerificationSend((e) => {
    console.log(e.mailClient) console.log(e.message) console.log(e.record) console.log(e.meta)
})
```

 **[onMailerBeforeRecordChangeEmailSend](./js-event-hooks.md#onmailerbeforerecordchangeemailsend)**

`onMailerBeforeRecordChangeEmailSend` hook is triggered right before sending a confirmation new address email to an auth record, allowing you to inspect and customize the email message that is being sent. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
onMailerBeforeRecordChangeEmailSend((e) => {
            console.log(e.mailClient) console.log(e.message) console.log(e.record) console.log(e.meta) // change the mail subject e.message.subject = "new subject" });
```

 **[onMailerAfterRecordChangeEmailSend](./js-event-hooks.md#onmailerafterrecordchangeemailsend)**

`onMailerAfterRecordChangeEmailSend` hook is triggered after a verification email was successfully sent to an auth record. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
onMailerAfterRecordChangeEmailSend((e) => {
    console.log(e.mailClient) console.log(e.message) console.log(e.record) console.log(e.meta)
})
```

### [ Record CRUD API hooks ](./js-event-hooks.md#record-crud-api-hooks)

**[onRecordsListRequest](./js-event-hooks.md#onrecordslistrequest)**

`onRecordsListRequest` hook is triggered on each API Records list request. Could be used to validate or modify the response before returning it to the client. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every collection onRecordsListRequest((e) => { console.log(e.httpContext) console.log(e.result) }) / / fires only
for "users"
and "articles"
collections onRecordsListRequest((e) => {
    console.log(e.httpContext) console.log(e.result)
}, "users", "articles")
```

 **[onRecordViewRequest](./js-event-hooks.md#onrecordviewrequest)**

`onRecordViewRequest` hook is triggered on each API Record view request. Could be used to validate or modify the response before returning it to the client. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every collection onRecordViewRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "articles"
collections onRecordViewRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "articles")
```

 **[onRecordBeforeCreateRequest](./js-event-hooks.md#onrecordbeforecreaterequest)**

`onRecordBeforeCreateRequest` hook is triggered before each API Record create request (after request data load and before model persistence).   
Could be used to additionally validate the request data or implement completely different persistence behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every collection onRecordBeforeCreateRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.uploadedFiles) }) / / fires only
for "users"
and "articles"
collections onRecordBeforeCreateRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.uploadedFiles)
}, "users", "articles")
```

 **[onRecordAfterCreateRequest](./js-event-hooks.md#onrecordaftercreaterequest)**

`onRecordAfterCreateRequest` hook is triggered after each successful API Record create request.   
Could be used to additionally validate the request data or implement completely different persistence behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every collection onRecordAfterCreateRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.uploadedFiles) }) / / fires only
for "users"
and "articles"
collections onRecordAfterCreateRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.uploadedFiles)
}, "users", "articles")
```

 **[onRecordBeforeUpdateRequest](./js-event-hooks.md#onrecordbeforeupdaterequest)**

`onRecordBeforeUpdateRequest` hook is triggered before each API Record update request (after request data load and before model persistence).   
Could be used to additionally validate the request data or implement completely different persistence behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every collection onRecordBeforeUpdateRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.uploadedFiles) }) / / fires only
for "users"
and "articles"
collections onRecordBeforeUpdateRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.uploadedFiles)
}, "users", "articles")
```

 **[onRecordAfterUpdateRequest](./js-event-hooks.md#onrecordafterupdaterequest)**

`onRecordAfterUpdateRequest` hook is triggered after each successful API Record update request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every collection onRecordAfterUpdateRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.uploadedFiles) }) / / fires only
for "users"
and "articles"
collections onRecordAfterUpdateRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.uploadedFiles)
}, "users", "articles")
```

 **[onRecordBeforeDeleteRequest](./js-event-hooks.md#onrecordbeforedeleterequest)**

`onRecordBeforeDeleteRequest` hook is triggered before each API Record delete request (after model load and before actual deletion).   
Could be used to additionally validate the request data or implement completely different delete behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every collection onRecordBeforeDeleteRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "articles"
collections onRecordBeforeDeleteRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "articles")
```

 **[onRecordAfterDeleteRequest](./js-event-hooks.md#onrecordafterdeleterequest)**

`onRecordAfterDeleteRequest` hook is triggered after each successful API Record delete request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every collection onRecordAfterDeleteRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "articles"
collections onRecordAfterDeleteRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "articles")
```

### [ Record Auth API hooks ](./js-event-hooks.md#record-auth-api-hooks)

**[onRecordAuthRequest](./js-event-hooks.md#onrecordauthrequest)**

`onRecordAuthRequest` hook is triggered on each successful API record authentication request (sign-in, token refresh, etc.). Could be used to additionally validate or modify the authenticated record data and token. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAuthRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.token) console.log(e.meta) }) / / fires only
for "users"
and "managers"
auth collections onRecordAuthRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.token) console.log(e.meta)
}, "users", "managers")
```

 **[onRecordBeforeAuthWithPasswordRequest](./js-event-hooks.md#onrecordbeforeauthwithpasswordrequest)**

`onRecordBeforeAuthWithPasswordRequest` hook is triggered before each Record auth with password API request (after request data load and before password validation). Could be used to implement for example a custom password validation or to locate a different Record model (by reassigning `RecordAuthWithPasswordEvent.Record`). 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordBeforeAuthWithPasswordRequest((e) => { console.log(e.httpContext) console.log(e.record) / / could be null console.log(e.identity) console.log(e.password)
}) // fires only for "users" and "managers" auth collections onRecordBeforeAuthWithPasswordRequest((e) => { console.log(e.httpContext) console.log(e.record) // could be null console.log(e.identity) console.log(e.password) }, "users", "managers")
```

 **[onRecordAfterAuthWithPasswordRequest](./js-event-hooks.md#onrecordafterauthwithpasswordrequest)**

`onRecordAfterAuthWithPasswordRequest` hook is triggered after each successful Record auth with password API request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterAuthWithPasswordRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.identity) console.log(e.password) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterAuthWithPasswordRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.identity) console.log(e.password)
}, "users", "managers")
```

 **[onRecordBeforeAuthWithOAuth2Request](./js-event-hooks.md#onrecordbeforeauthwithoauth2request)**

`onRecordBeforeAuthWithOAuth2Request` hook is triggered before each Record OAuth2 sign-in/sign-up API request (after token exchange and before external provider linking). 

If the `RecordAuthWithOAuth2Event.Record` is not set, then the OAuth2 request will try to create a new auth Record. 

To assign or link a different existing record model you can change the `RecordAuthWithOAuth2Event.Record` field. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordBeforeAuthWithOAuth2Request((e) => { console.log(e.httpContext) console.log(e.providerName) console.log(e.providerClient) console.log(e.record) / / could be null console.log(e.oAuth2User) console.log(e.isNewRecord)
}) // fires only for "users" and "managers" auth collections onRecordBeforeAuthWithOAuth2Request((e) => { console.log(e.httpContext) console.log(e.providerName) console.log(e.providerClient) console.log(e.record) // could be null console.log(e.oAuth2User) console.log(e.isNewRecord) }, "users", "managers")
```

 **[onRecordAfterAuthWithOAuth2Request](./js-event-hooks.md#onrecordafterauthwithoauth2request)**

`onRecordAfterAuthWithOAuth2Request` hook is triggered after each successful Record OAuth2 API request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterAuthWithOAuth2Request((e) => { console.log(e.httpContext) console.log(e.providerName) console.log(e.providerClient) console.log(e.record) console.log(e.oAuth2User) console.log(e.isNewRecord) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterAuthWithOAuth2Request((e) => {
    console.log(e.httpContext) console.log(e.providerName) console.log(e.providerClient) console.log(e.record) console.log(e.oAuth2User) console.log(e.isNewRecord)
}, "users", "managers")
```

 **[onRecordBeforeAuthRefreshRequest](./js-event-hooks.md#onrecordbeforeauthrefreshrequest)**

`onRecordBeforeAuthRefreshRequest` hook is triggered before each Record auth refresh API request (right before generating a new auth token). Could be used to additionally validate the request data or implement completely different auth refresh behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordBeforeAuthRefreshRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordBeforeAuthRefreshRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordAfterAuthRefreshRequest](./js-event-hooks.md#onrecordafterauthrefreshrequest)**

`onRecordAfterAuthRefreshRequest` hook is triggered after each successful auth refresh API request (right after generating a new auth token). 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterAuthRefreshRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterAuthRefreshRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordListExternalAuthsRequest](./js-event-hooks.md#onrecordlistexternalauthsrequest)**

`onRecordListExternalAuthsRequest` hook is triggered on each API record external auths list request. Could be used to validate or modify the response before returning it to the client. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordListExternalAuthsRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.externalAuths) }) / / fires only
for "users"
and "managers"
auth collections onRecordListExternalAuthsRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.externalAuths)
}, "users", "managers")
```

 **[onRecordBeforeUnlinkExternalAuthRequest](./js-event-hooks.md#onrecordbeforeunlinkexternalauthrequest)**

`onRecordBeforeUnlinkExternalAuthRequest` hook is triggered before each API record external auth unlink request (after models load and before the actual relation deletion). Could be used to additionally validate the request data or implement completely different delete behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterUnlinkExternalAuthRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.externalAuth) }) / / fires only
for "users"
and "managers"
auth collections onRecordBeforeUnlinkExternalAuthRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.externalAuth)
}, "users", "managers")
```

 **[onRecordAfterUnlinkExternalAuthRequest](./js-event-hooks.md#onrecordafterunlinkexternalauthrequest)**

`onRecordAfterUnlinkExternalAuthRequest` hook is triggered after each successful API record external auth unlink request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterUnlinkExternalAuthRequest((e) => { console.log(e.httpContext) console.log(e.record) console.log(e.externalAuth) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterUnlinkExternalAuthRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.externalAuth)
}, "users", "managers")
```

 **[onRecordBeforeRequestPasswordResetRequest](./js-event-hooks.md#onrecordbeforerequestpasswordresetrequest)**

`onRecordBeforeRequestPasswordResetRequest` hook is triggered before each Record request password reset API request (after request data load and before sending the reset email). Could be used to additionally validate the request data or implement completely different password reset behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordBeforeRequestPasswordResetRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordBeforeRequestPasswordResetRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordAfterRequestPasswordResetRequest](./js-event-hooks.md#onrecordafterrequestpasswordresetrequest)**

`onRecordAfterRequestPasswordResetRequest` hook is triggered after each successful request password reset API request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterRequestPasswordResetRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterRequestPasswordResetRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordBeforeConfirmPasswordResetRequest](./js-event-hooks.md#onrecordbeforeconfirmpasswordresetrequest)**

`onRecordBeforeConfirmPasswordResetRequest` hook is triggered before each Record confirm password reset API request (after request data load and before persistence). Could be used to additionally validate the request data or implement completely different persistence behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordBeforeConfirmPasswordResetRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordBeforeConfirmPasswordResetRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordAfterConfirmPasswordResetRequest](./js-event-hooks.md#onrecordafterconfirmpasswordresetrequest)**

`onRecordAfterConfirmPasswordResetRequest` hook is triggered after each successful confirm password reset API request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterConfirmPasswordResetRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterConfirmPasswordResetRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordBeforeRequestVerificationRequest](./js-event-hooks.md#onrecordbeforerequestverificationrequest)**

`onRecordBeforeRequestVerificationRequest` hook is triggered before each Record request verification API request (after request data load and before sending the verification email). Could be used to additionally validate the loaded request data or implement completely different verification behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordBeforeRequestVerificationRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordBeforeRequestVerificationRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordAfterRequestVerificationRequest](./js-event-hooks.md#onrecordafterrequestverificationrequest)**

`onRecordAfterRequestVerificationRequest` hook is triggered after each successful request verification API request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterRequestVerificationRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterRequestVerificationRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordBeforeConfirmVerificationRequest](./js-event-hooks.md#onrecordbeforeconfirmverificationrequest)**

`onRecordBeforeConfirmVerificationRequest` hook is triggered before each Record confirm verification API request (after request data load and before persistence). Could be used to additionally validate the request data or implement completely different persistence behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordBeforeConfirmVerificationRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordBeforeConfirmVerificationRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordAfterConfirmVerificationRequest](./js-event-hooks.md#onrecordafterconfirmverificationrequest)**

`onRecordAfterConfirmVerificationRequest` hook is triggered after each successful confirm verification API request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterConfirmVerificationRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterConfirmVerificationRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordBeforeRequestEmailChangeRequest](./js-event-hooks.md#onrecordbeforerequestemailchangerequest)**

`onRecordBeforeRequestEmailChangeRequest` hook is triggered before each Record request email change API request (after request data load and before sending the email link to confirm the change). Could be used to additionally validate the request data or implement completely different request email change behavior. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordBeforeRequestEmailChangeRequest((e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordBeforeRequestEmailChangeRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

 **[onRecordAfterRequestEmailChangeRequest](./js-event-hooks.md#onrecordafterrequestemailchangerequest)**

`onRecordAfterRequestEmailChangeRequest` hook is triggered after each successful request email change API request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth collection onRecordAfterRequestEmailChangeRequest(e) => { console.log(e.httpContext) console.log(e.record) }) / / fires only
for "users"
and "managers"
auth collections onRecordAfterRequestEmailChangeRequest((e) => {
    console.log(e.httpContext) console.log(e.record)
}, "users", "managers")
```

### [ Realtime API hooks ](./js-event-hooks.md#realtime-api-hooks)

**[onRealtimeConnectRequest](./js-event-hooks.md#onrealtimeconnectrequest)**

`onRealtimeConnectRequest` hook is triggered right before establishing the SSE client connection. 

```javascript
onRealtimeConnectRequest((e) => {
            console.log(e.httpContext) console.log(e.client.id()) console.log(e.idleTimeout) // in nanosec })
```

 **[onRealtimeDisconnectRequest](./js-event-hooks.md#onrealtimedisconnectrequest)**

`onRealtimeDisconnectRequest` hook is triggered on disconnected/interrupted SSE client connection. 

```javascript
onRealtimeDisconnectRequest((e) => {
    console.log(e.httpContext) console.log(e.client.id())
})
```

 **[onRealtimeBeforeMessageSend](./js-event-hooks.md#onrealtimebeforemessagesend)**

`onRealtimeBeforeMessageSend` hook is triggered right before sending an SSE message to a client. 

Returning `false` will prevent sending the message. Returning any other error will close the realtime connection. 

```javascript
onRealtimeBeforeMessageSend((e) => {
    console.log(e.httpContext) console.log(e.client.id()) console.log(e.message)
})
```

 **[onRealtimeAfterMessageSend](./js-event-hooks.md#onrealtimeaftermessagesend)**

`onRealtimeAfterMessageSend` hook is triggered right after sending an SSE message to a client. 

```javascript
onRealtimeAfterMessageSend((e) => {
    console.log(e.httpContext) console.log(e.client.id()) console.log(e.message)
})
```

 **[onRealtimeBeforeSubscribeRequest](./js-event-hooks.md#onrealtimebeforesubscriberequest)**

`onRealtimeBeforeSubscribeRequest` hook is triggered before changing the client subscriptions, allowing you to further validate and modify the submitted change. 

```javascript
onRealtimeBeforeSubscribeRequest((e) => {
    console.log(e.httpContext) console.log(e.client.id()) console.log(e.subscriptions)
})
```

 **[onRealtimeAfterSubscribeRequest](./js-event-hooks.md#onrealtimeaftersubscriberequest)**

`onRealtimeAfterSubscribeRequest` hook is triggered after the client subscriptions were successfully changed. 

```javascript
onRealtimeAfterSubscribeRequest((e) => {
    console.log(e.httpContext) console.log(e.client.id()) console.log(e.subscriptions)
})
```

### [ File API hooks ](./js-event-hooks.md#file-api-hooks)

**[onFileDownloadRequest](./js-event-hooks.md#onfiledownloadrequest)**

`onFileDownloadRequest` hook is triggered before each API File download request. Could be used to validate or modify the file response before returning it to the client. 

```javascript
onFileDownloadRequest((e) => {
    console.log(e.httpContext) console.log(e.record) console.log(e.fileField) console.log(e.servedPath) console.log(e.servedName)
})
```

 **[onFileBeforeTokenRequest](./js-event-hooks.md#onfilebeforetokenrequest)**

`onFileBeforeTokenRequest` hook is triggered before each file token API request. 

If no token or model was submitted, e.Model and e.Token will be empty, allowing you to implement your own custom model file auth implementation. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth model onFileBeforeTokenRequest((e) => { console.log(e.httpContext) console.log(e.token) }) / / fires only
for "users"
onFileBeforeTokenRequest((e) => {
    console.log(e.httpContext) console.log(e.token)
}, "users")
```

 **[onFileAfterTokenRequest](./js-event-hooks.md#onfileaftertokenrequest)**

`onFileAfterTokenRequest` hook is triggered after each successful file token API request. 

If the optional "tags" list (Collection ids or names) is specified, then all event handlers registered via the created hook will be triggered and called only if their event data origin matches the tags. 

```javascript
/ fires for every auth model onFileAfterTokenRequest((e) => { console.log(e.httpContext) console.log(e.token) }) / / fires only
for "users"
onFileAfterTokenRequest((e) => {
    console.log(e.httpContext) console.log(e.token)
}, "users")
```

### [ Collection API hooks ](./js-event-hooks.md#collection-api-hooks)

**[onCollectionsListRequest](./js-event-hooks.md#oncollectionslistrequest)**

`onCollectionsListRequest` hook is triggered on each API Collections list request. Could be used to validate or modify the response before returning it to the client. 

```javascript
onCollectionsListRequest((e) => {
    console.log(e.httpContext) console.log(e.collections) console.log(e.result)
})
```

 **[onCollectionViewRequest](./js-event-hooks.md#oncollectionviewrequest)**

`onCollectionViewRequest` hook is triggered on each API Collection view request. Could be used to validate or modify the response before returning it to the client. 

```javascript
onCollectionViewRequest((e) => {
    console.log(e.httpContext) console.log(e.collection)
})
```

 **[onCollectionBeforeCreateRequest](./js-event-hooks.md#oncollectionbeforecreaterequest)**

`onCollectionBeforeCreateRequest` hook is triggered before each API Collection create request (after request data load and before model persistence).   
Could be used to additionally validate the request data or implement completely different persistence behavior. 

```javascript
onCollectionBeforeCreateRequest((e) => {
    console.log(e.httpContext) console.log(e.collection)
})
```

 **[onCollectionAfterCreateRequest](./js-event-hooks.md#oncollectionaftercreaterequest)**

`onCollectionAfterCreateRequest` hook is triggered after each successful API Collection create request. 

```javascript
onCollectionAfterCreateRequest((e) => {
    console.log(e.httpContext) console.log(e.collection)
})
```

 **[onCollectionBeforeUpdateRequest](./js-event-hooks.md#oncollectionbeforeupdaterequest)**

`onCollectionBeforeUpdateRequest` hook is triggered before each API Collection update request (after request data load and before model persistence).   
Could be used to additionally validate the request data or implement completely different persistence behavior. 

```javascript
onCollectionBeforeUpdateRequest((e) => {
    console.log(e.httpContext) console.log(e.collection)
})
```

 **[onCollectionAfterUpdateRequest](./js-event-hooks.md#oncollectionafterupdaterequest)**

`onCollectionAfterUpdateRequest` hook is triggered after each successful API Collection update request. 

```javascript
onCollectionAfterUpdateRequest((e) => {
    console.log(e.httpContext) console.log(e.collection)
})
```

 **[onCollectionBeforeDeleteRequest](./js-event-hooks.md#oncollectionbeforedeleterequest)**

`onCollectionBeforeDeleteRequest` hook is triggered before each API Collection delete request (after model load and before actual deletion).   
Could be used to additionally validate the request data or implement completely different delete behavior. 

```javascript
onCollectionBeforeDeleteRequest((e) => {
    console.log(e.httpContext) console.log(e.collection)
})
```

 **[onCollectionAfterDeleteRequest](./js-event-hooks.md#oncollectionafterdeleterequest)**

`onCollectionAfterDeleteRequest` hook is triggered after each successful API Collection delete request. 

```javascript
onCollectionAfterDeleteRequest((e) => {
    console.log(e.httpContext) console.log(e.collection)
})
```

 **[onCollectionsBeforeImportRequest](./js-event-hooks.md#oncollectionsbeforeimportrequest)**

`onCollectionsBeforeImportRequest` hook is triggered before each API collections import request (after request data load and before the actual import).   
Could be used to additionally validate the imported collections or to implement completely different import behavior. 

```javascript
onCollectionsBeforeImportRequest((e) => {
    console.log(e.httpContext) console.log(e.collections)
})
```

 **[onCollectionsAfterImportRequest](./js-event-hooks.md#oncollectionsafterimportrequest)**

`onCollectionsAfterImportRequest` hook is triggered after each successful API collections import request. 

```javascript
onCollectionsAfterImportRequest((e) => {
    console.log(e.httpContext) console.log(e.collections)
})
```

### [ Settings API hooks ](./js-event-hooks.md#settings-api-hooks)

**[onSettingsListRequest](./js-event-hooks.md#onsettingslistrequest)**

`onSettingsListRequest` hook is triggered on each successful API Settings list request.   
Could be used to validate or modify the response before returning it to the client. 

```javascript
onSettingsListRequest((e) => {
    console.log(e.httpContext) console.log(e.redactedSettings)
})
```

 **[onSettingsBeforeUpdateRequest](./js-event-hooks.md#onsettingsbeforeupdaterequest)**

`onSettingsBeforeUpdateRequest` hook is triggered on each successful API Settings list request.   
Could be used to validate or modify the response before returning it to the client. 

```javascript
onSettingsBeforeUpdateRequest((e) => {
    console.log(e.httpContext) console.log(e.oldSettings) console.log(e.newSettings)
})
```

 **[onSettingsAfterUpdateRequest](./js-event-hooks.md#onsettingsafterupdaterequest)**

`onSettingsAfterUpdateRequest` hook is triggered after each successful API Settings update request. 

```javascript
onSettingsAfterUpdateRequest((e) => {
    console.log(e.httpContext) console.log(e.oldSettings) console.log(e.newSettings)
})
```

### [ Admin CRUD API hooks ](./js-event-hooks.md#admin-crud-api-hooks)

**[onAdminsListRequest](./js-event-hooks.md#onadminslistrequest)**

`onAdminsListRequest` hook is triggered on each API Admins list request.   
Could be used to validate or modify the response before returning it to the client. 

```javascript
onAdminsListRequest((e) => {
    console.log(e.httpContext) console.log(e.admins) console.log(e.result)
})
```

 **[onAdminViewRequest](./js-event-hooks.md#onadminviewrequest)**

`onAdminViewRequest` hook is triggered on each API Admin view request.   
Could be used to validate or modify the response before returning it to the client. 

```javascript
onAdminViewRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminBeforeCreateRequest](./js-event-hooks.md#onadminbeforecreaterequest)**

`onAdminBeforeCreateRequest` hook is triggered before each API Admin create request (after request data load and before model persistence).   
Could be used to additionally validate the request data or implement completely different persistence behavior. 

```javascript
onAdminBeforeCreateRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminAfterCreateRequest](./js-event-hooks.md#onadminaftercreaterequest)**

`onAdminAfterCreateRequest` hook is triggered after each successful API Admin create request. 

```javascript
onAdminAfterCreateRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminBeforeUpdateRequest](./js-event-hooks.md#onadminbeforeupdaterequest)**

`onAdminBeforeUpdateRequest` hook is triggered before each API Admin update request (after request data load and before model persistence).   
Could be used to additionally validate the request data or implement completely different persistence behavior. 

```javascript
onAdminBeforeUpdateRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminAfterUpdateRequest](./js-event-hooks.md#onadminafterupdaterequest)**

`onAdminAfterUpdateRequest` hook is triggered after each successful API Admin update request. 

```javascript
onAdminAfterUpdateRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminBeforeDeleteRequest](./js-event-hooks.md#onadminbeforedeleterequest)**

`onAdminBeforeDeleteRequest` hook is triggered before each API Admin delete request (after model load and before actual deletion).   
Could be used to additionally validate the request data or implement completely different delete behavior. 

```javascript
onAdminBeforeDeleteRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminAfterDeleteRequest](./js-event-hooks.md#onadminafterdeleterequest)**

`onAdminAfterDeleteRequest` hook is triggered after each successful API Admin delete request. 

```javascript
onAdminAfterDeleteRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

### [ Admin Auth API hooks ](./js-event-hooks.md#admin-auth-api-hooks)

**[onAdminAuthRequest](./js-event-hooks.md#onadminauthrequest)**

`onAdminAuthRequest` hook is triggered on each successful API Admin authentication request (sign-in, token refresh, etc.).   
Could be used to additionally validate or modify the authenticated admin data and token. 

```javascript
onAdminAuthRequest((e) => {
    console.log(e.httpContext) console.log(e.admin) console.log(e.token)
})
```

 **[onAdminBeforeAuthWithPasswordRequest](./js-event-hooks.md#onadminbeforeauthwithpasswordrequest)**

`onAdminBeforeAuthWithPasswordRequest` hook is triggered before each Admin auth with password API request (after request data load and before password validation).   
Could be used to implement for example a custom password validation or to locate a different Admin identity (by assigning `AdminAuthWithPasswordEvent.Admin`). 

```javascript
onAdminBeforeAuthWithPasswordRequest((e) => {
    console.log(e.httpContext) console.log(e.admin) console.log(e.identity) console.log(e.password)
})
```

 **[onAdminAfterAuthWithPasswordRequest](./js-event-hooks.md#onadminafterauthwithpasswordrequest)**

`onAdminAfterAuthWithPasswordRequest` hook is triggered after each successful Admin auth with password API request. 

```javascript
onAdminAfterAuthWithPasswordRequest((e) => {
    console.log(e.httpContext) console.log(e.admin) console.log(e.identity) console.log(e.password)
})
```

 **[onAdminBeforeAuthRefreshRequest](./js-event-hooks.md#onadminbeforeauthrefreshrequest)**

`onAdminBeforeAuthRefreshRequest` hook is triggered before each Admin auth refresh API request (right before generating a new auth token).   
Could be used to additionally validate the request data or implement completely different auth refresh behavior. 

```javascript
onAdminBeforeAuthRefreshRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminAfterAuthRefreshRequest](./js-event-hooks.md#onadminafterauthrefreshrequest)**

`onAdminAfterAuthRefreshRequest` hook is triggered after each successful auth refresh API request (right after generating a new auth token). 

```javascript
onAdminAfterAuthRefreshRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminBeforeRequestPasswordResetRequest](./js-event-hooks.md#onadminbeforerequestpasswordresetrequest)**

`onAdminBeforeRequestPasswordResetRequest` hook is triggered before each Admin request password reset API request (after request data load and before sending the reset email).   
Could be used to additionally validate the request data or implement completely different password reset behavior. 

```javascript
onAdminBeforeRequestPasswordResetRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminAfterRequestPasswordResetRequest](./js-event-hooks.md#onadminafterrequestpasswordresetrequest)**

`onAdminAfterRequestPasswordResetRequest` hook is triggered after each successful request password reset API request. 

```javascript
onAdminBeforeRequestPasswordResetRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminBeforeConfirmPasswordResetRequest](./js-event-hooks.md#onadminbeforeconfirmpasswordresetrequest)**

`onAdminBeforeConfirmPasswordResetRequest` hook is triggered before each Admin confirm password reset API request (after request data load and before persistence).   
Could be used to additionally validate the request data or implement completely different persistence behavior. 

```javascript
onAdminBeforeConfirmPasswordResetRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

 **[onAdminAfterConfirmPasswordResetRequest](./js-event-hooks.md#onadminafterconfirmpasswordresetrequest)**

`onAdminAfterConfirmPasswordResetRequest` hook is triggered after each successful confirm password reset API request. 

```javascript
onAdminAfterConfirmPasswordResetRequest((e) => {
    console.log(e.httpContext) console.log(e.admin)
})
```

[FAQ](https://pocketbase.io/old/faq) [Discussions](https://github.com/pocketbase/pocketbase/discussions) [Documentation](https://pocketbase.io/old/docs) [JavaScript SDK](https://github.com/pocketbase/js-sdk) [Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket **Base**

[__](mailto:support@pocketbase.io)[__](https://twitter.com/pocketbase)[__](https://github.com/pocketbase/pocketbase)

© 2023-2025 Pocket **Base** The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)

__

Extend with JavaScript - Event hooks - Docs - PocketBase
