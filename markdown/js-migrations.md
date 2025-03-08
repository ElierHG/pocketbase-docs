This is the older PocketBase <= 0.22.x version of the website. For the latest PocketBase v0.23+ docs please [click here](https://pocketbase.io/). 

[![PocketBase logo](./js-migrations_files/logo.svg) Pocket **Base** v0.22.31](https://pocketbase.io/old/)

__

Extend with JavaScript - Migrations

PocketBase comes with a builtin DB and data migration utility, allowing you to version your DB structure, create collections programmatically, initialize default settings and/or run anything that needs to be executed only once.

The user defined migrations are located in `pb_migrations` directory (it can be changed using the `--migrationsDir` flag) and each unapplied migration inside it will be executed automatically in a transaction on `serve` (or on `migrate up`).

The generated migrations are safe to be commited to version control and can be shared with your other team members.

  * [Automigrate](./js-migrations.md#automigrate)
  * [Creating migrations](./js-migrations.md#creating-migrations)
    * [Migration file](./js-migrations.md#migration-file)
  * [Collections snapshot](./js-migrations.md#collections-snapshot)
  * [Migrations history](./js-migrations.md#migrations-history)
  * [Examples](./js-migrations.md#examples)
    * [Running raw SQL statements](./js-migrations.md#running-raw-sql-statements)
    * [Initialize default application settings](./js-migrations.md#initialize-default-application-settings)
    * [Creating new admin](./js-migrations.md#creating-new-admin)
    * [Creating new auth record](./js-migrations.md#creating-new-auth-record)

### [ Automigrate ](./js-migrations.md#automigrate)

The prebuilt executable has the `--automigrate` flag enabled by default, meaning that every collection configuration change from the Admin UI will generate the related migration file automatically for you.

### [ Creating migrations ](./js-migrations.md#creating-migrations)

To create a new blank migration you can run `migrate create`.

```sql
[root@dev app]$ ./pocketbase migrate create "your_new_migration"
```

```javascript
/ pb_migrations/ / 1687801097_ your_new_migration.js migrate((db) => { // add up queries... }, (db) => { // add down queries... })
```

New migrations are applied automatically on `serve`.

Optionally, you could apply new migrations manually by running `migrate up`.

To revert the last applied migration(s), you could run `migrate down [number]`.

##### [ Migration file ](./js-migrations.md#migration-file)

Each migration file should have a single `migrate(upFunc, downFunc)` call.

In the migration file, you are expected to write your "upgrade" code in the `upFunc` callback.   
The `downFunc` is optional and it should contains the "downgrade" operations to revert the changes made by the `upFunc`.

Both callbacks accept a single `db` argument (`dbx.Builder`) that you can use directly or create a `Dao` instance and use its available helpers. You can explore the [Database guide](./js-database.md) for more details how to operate with the `db` object and its available methods.

### [ Collections snapshot ](./js-migrations.md#collections-snapshot)

PocketBase comes also with a `migrate collections` command that will generate a full snapshot of your current Collections configuration without having to type it manually:

```javascript
[root @dev app] $. // pocketbase migrate collections
```

Similar to the `migrate create` command, this will generate a new migration file in the `pb_migrations` directory.

It is safe to run the command multiple times and generate multiple snapshot migration files.

### [ Migrations history ](./js-migrations.md#migrations-history)

All applied migration filenames are stored in the internal `_migrations` table.   
During local development often you might end up making various collection changes to test different approaches.   
When `--automigrate` is enabled ( _which is the default_ ) this could lead in a migration history with unnecessary intermediate steps that may not be wanted in the final migration history.

To avoid the clutter and to prevent applying the intermediate steps in production, you can remove (or squash) the unnecessary migration files manually and then update the local migrations history by running:

```
[root@dev app]$ ./pocketbase migrate history-sync
```

The above command will remove any entry from the `_migrations` table that doesn't have a related migration file associated with it.

### [ Examples ](./js-migrations.md#examples)

##### [ Running raw SQL statements ](./js-migrations.md#running-raw-sql-statements)

```javascript
/ pb_migrations/ / 1687801090_ set_pending_status.js / // set a default "pending" status to all empty status articles migrate((db) => { db.newQuery("UPDATE articles SET status = 'pending' WHERE;
    status = ''
") .execute() });
```

##### [ Initialize default application settings ](./js-migrations.md#initialize-default-application-settings)

```javascript
/ pb_migrations/ / 1687801090_ initial_settings.js migrate((db) => {
    const dao = new Dao(db);
    const settings = dao.findSettings() settings.meta.appName = "test"
    settings.logs.maxDays = 2 dao.saveSettings(settings)
});
```

##### [ Creating new admin ](./js-migrations.md#creating-new-admin)

```javascript
/ pb_migrations/ / 1687801090_ initial_admin.js migrate((db) => {
            const dao = new Dao(db);
            const admin = new Admin();
            admin.email = "test@example.com"
            admin.setPassword("1234567890") dao.saveAdmin(admin)
        }, (db) => { // optional revert const;
            dao = new Dao(db);
            try {
                const admin = dao.findAdminByEmail("test@example.com") dao.deleteAdmin(admin)
            } catch (_) { // * most likely already deleted *// } });
```

##### [ Creating new auth record ](./js-migrations.md#creating-new-auth-record)

```javascript
/ pb_migrations/ / 1687801090_n ew_users_record.js migrate((db) => {
            const dao = new Dao(db);
            const collection = dao.findCollectionByNameOrId("users") const;
            record = new Record(collection) record.setUsername("u_" + $security.randomStringWithAlphabet(5, "123456789")) record.setPassword("1234567890") record.set("name", "John Doe") record.set("email", "test@example.com") dao.saveRecord(record)
        }, (db) => { // optional revert const;
            dao = new Dao(db);
            try {
                const record = dao.findAuthRecordByEmail("users", "test@example.com") dao.deleteRecord(record)
            } catch (_) { // * most likely already deleted *// } });
```

[FAQ](https://pocketbase.io/old/faq) [Discussions](https://github.com/pocketbase/pocketbase/discussions) [Documentation](https://pocketbase.io/old/docs) [JavaScript SDK](https://github.com/pocketbase/js-sdk) [Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket **Base**

[__](mailto:support@pocketbase.io)[__](https://twitter.com/pocketbase)[__](https://github.com/pocketbase/pocketbase)

© 2023-2025 Pocket **Base** The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)

__

Extend with JavaScript - Migrations - Docs - PocketBase
