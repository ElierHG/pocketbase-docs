This is the older PocketBase <= 0.22.x version of the website. For the latest PocketBase v0.23+ docs please [click here](https://pocketbase.io/). 

[![PocketBase logo](./js-database_files/logo.svg) Pocket **Base** v0.22.31](https://pocketbase.io/old/)

__

Extend with JavaScript - Database

The main interface to interact with your application database is via `$app.dao()`.

`$app.dao()` provides read and write helpers (see [Collection operations](./js-collections.md) and [Record operations](./js-records.md)) and it is responsible for triggering the `onModel*` event hooks.

It also exposes `$app.dao().db()` builder that allows executing various SQL statements (including raw queries).

  * [Executing queries](./js-database.md#executing-queries)
  * [Binding parameters](./js-database.md#binding-parameters)
  * [Query builder](./js-database.md#query-builder)
    * [select(), andSelect(), distinct()](./js-database.md#select-andselect-distinct)
    * [from()](./js-database.md#from)
    * [join()](./js-database.md#join)
    * [where(), andWhere(), orWhere()](./js-database.md#where-andwhere-orwhere)
    * [orderBy(), andOrderBy()](./js-database.md#orderby-andorderby)
    * [groupBy(), andGroupBy()](./js-database.md#groupby-andgroupby)
    * [having(), andHaving(), orHaving()](./js-database.md#having-andhaving-orhaving)
    * [limit()](./js-database.md#limit)
    * [offset()](./js-database.md#offset)
  * [Transaction](./js-database.md#transaction)
  * [Dao without event hooks](./js-database.md#dao-without-event-hooks)

### [ Executing queries ](./js-database.md#executing-queries)

To execute DB queries you can start with the `newQuery("...")` statement and then call one of:

  * `[ execute() ](./js-database.md#execute)` \- for any query statement that is not meant to retrieve data:

```javascript
$app.dao().db().newQuery("CREATE INDEX name_idx ON users (name)").execute() // throw an error on db failure
```

  * `[ one() ](./js-database.md#execute-one)` \- to populate a single row into `DynamicModel` object:

```javascript
const result = new DynamicModel({ // describe the shape of the data (used also as initial values) "id": "", "status": false, "age": 0, "roles": [], // serialized json db arrays are decoded as plain arrays }) $app.dao().db() .newQuery("SELECT id, status, age, roles FROM users WHERE;
            id = 1 ") .one(result) // throw an error on db failure or missing row console.log(result.id);
```

  * `[ all() ](./js-database.md#execute-all)` \- to populate multiple rows into an array of objects (note that the array must be created with `arrayOf`):

```javascript
const result = arrayOf(new DynamicModel({ // describe the shape of the data (used also as initial values) "id": "", "status": false, "age": 0, "roles": [], // serialized json db arrays are decoded as plain arrays })) $app.dao().db() .newQuery("SELECT id, status, age, roles FROM users LIMIT 100") .all(result) // throw an error on db failure if (result.length > 0) { console.log(result[0].id) };
```

### [ Binding parameters ](./js-database.md#binding-parameters)

To prevent SQL injection attacks, you should use named parameters for any expression value that comes from user input. This could be done using the named `{:paramName}` placeholders in your SQL statement and then define the parameter values for the query with `bind(params)`. For example:

```javascript
const result = arrayOf(new DynamicModel({
    "name": "",
    "created": "",
})) $app.dao().db().newQuery("SELECT name, created FROM posts WHERE created >= {:from} and created <= {:to}").bind({
    "from": "2023-06-25 00:00:00.000Z",
    "to": "2023-06-28 23:59:59.999Z",
}).all(result) console.log(result.length);
```

### [ Query builder ](./js-database.md#query-builder)

Instead of writting plain SQLs, you can also compose SQL statements programmatically using the db query builder.   
Every SQL keyword has a corresponding query building method. For example, `SELECT` corresponds to `select()`, `FROM` corresponds to `from()`, `WHERE` corresponds to `where()`, and so on.

```javascript
const result = arrayOf(new DynamicModel({
    "id": "",
    "email": "",
})) $app.dao().db().select("id", "email").from("users").andWhere($dbx.like("email", "example.com")).limit(100).orderBy("created ASC").all(result);
```

##### [ select(), andSelect(), distinct() ](./js-database.md#select-andselect-distinct)

The `select(...cols)` method initializes a `SELECT` query builder. It accepts a list of the column names to be selected.   
To add additional columns to an existing select query, you can call `andSelect()`.   
To select distinct rows, you can call `distinct()`.

```javascript
$app.dao().db().select("id", "avatar as image").andSelect("(firstName || ' ' || lastName) as fullName").distinct()...
```

##### [ from() ](./js-database.md#from)

The `from(...tables)` method specifies which tables to select from (plain table names are automatically quoted).

```javascript
$app.dao().db().select("table1.id", "table2.name").from("table1", "table2")...
```

##### [ join() ](./js-database.md#join)

The `join(type, table, on)` method specifies a `JOIN` clause. It takes 3 parameters:

  * `type` \- join type string like `INNER JOIN`, `LEFT JOIN`, etc.
  * `table` \- the name of the table to be joined
  * `on` \- optional `dbx.Expression` as an `ON` clause

For convenience, you can also use the shortcuts `innerJoin(table, on)`, `leftJoin(table, on)`, `rightJoin(table, on)` to specify `INNER JOIN`, `LEFT JOIN` and `RIGHT JOIN`, respectively.

```javascript
$app.dao().db().select("users.*").from("users").innerJoin("profiles", $dbx.exp("profiles.user_id = users.id")).join("FULL OUTER JOIN", "department", $dbx.exp("department.id = {:id}", {
    id: "someId"
}))...;
```

##### [ where(), andWhere(), orWhere() ](./js-database.md#where-andwhere-orwhere)

The `where(exp)` method specifies the `WHERE` condition of the query.   
You can also use `andWhere(exp)` or `orWhere(exp)` to append additional one or more conditions to an existing `WHERE` clause.   
Each where condition accepts a single `dbx.Expression` (see below for full list).

```javascript
/* SELECT users.* FROM users WHERE id = "someId" AND;
 status = "public" AND name like "%john%" OR (;
 role = "manager" AND fullTime IS TRUE AND experience > 10 ) */
/ $app.dao().db() .select("users.*") .from("users") .where($dbx.exp("id = {:id}", { id: "someId" })) .andWhere($dbx.hashExp({ status: "public" })) .andWhere($dbx.like("name", "john")) .orWhere($dbx.and( $dbx.hashExp({ role: "manager", fullTime: true, }), $dbx.exp("experience > {:exp}", { exp: 10 }) )) ...;
```

The following `dbx.Expression` methods are available:

  * `[ $dbx.exp(raw, optParams) ](./js-database.md#dbx-expraw-optparams)`   
Generates an expression with the specified raw query fragment. Use the `optParams` to bind parameters to the expression. 

```
$dbx.exp("status = 'public'") $dbx.exp("total > {:min} AND total < {:max}", { min: 10, max: 30 })
```

  * `[ $dbx.hashExp(pairs) ](./js-database.md#dbx-hashexppairs)`   
Generates a hash expression from a map whose keys are DB column names which need to be filtered according to the corresponding values. 

```javascript
/ slug = "example" AND active IS TRUE AND tags in ("tag1", "tag2", "tag3") AND parent IS NULL $dbx.hashExp({ slug: "example", active: true, tags: ["tag1", "tag2", "tag3"], parent: null, });
```

  * `[ $dbx.not(exp) ](./js-database.md#dbx-notexp)`   
Negates a single expression by wrapping it with `NOT()`. 

```
/ NOT(status = 1) $dbx.not($dbx.exp("status = 1"))
```

  * `[ $dbx.and(...exps) ](./js-database.md#dbx-and-exps)`   
Creates a new expression by concatenating the specified ones with `AND`. 

```
/ (status = 1 AND username like "%john%") $dbx.and($dbx.exp("status = 1"), $dbx.like("username", "john"))
```

  * `[ $dbx.or(...exps) ](./js-database.md#dbx-or-exps)`   
Creates a new expression by concatenating the specified ones with `OR`. 

```
/ (status = 1 OR username like "%john%") $dbx.or($dbx.exp("status = 1"), $dbx.like("username", "john"))
```

  * `[ $dbx.in(col, ...values) ](./js-database.md#dbx-incol-values)`   
Generates an `IN` expression for the specified column and the list of allowed values. 

```
/ status IN ("public", "reviewed") $dbx.in("status", "public", "reviewed")
```

  * `[ $dbx.notIn(col, ...values) ](./js-database.md#dbx-notincol-values)`   
Generates an `NOT IN` expression for the specified column and the list of allowed values. 

```
/ status NOT IN ("public", "reviewed") $dbx.notIn("status", "public", "reviewed")
```

  * `[ $dbx.like(col, ...values) ](./js-database.md#dbx-likecol-values)`   
Generates a `LIKE` expression for the specified column and the possible strings that the column should be like. If multiple values are present, the column should be like **all** of them.   
By default, each value will be surrounded by _"%"_ to enable partial matching. Special characters like _"%"_ , _"\"_ , _"_"_ will also be properly escaped. You may call `escape(...pairs)` and/or `match(left, right)` to change the default behavior. 

```javascript
/ name LIKE "%test1%" AND name LIKE "%test2%" $dbx.like("name", "test1", "test2") / / name LIKE "test1%"
$dbx.like("name", "test1").match(false, true)
```

  * `[ $dbx.notLike(col, ...values) ](./js-database.md#dbx-notlikecol-values)`   
Generates a `NOT LIKE` expression in similar manner as `like()`. 

```javascript
/ name NOT LIKE "%test1%" AND name NOT LIKE "%test2%" $dbx.notLike("name", "test1", "test2") / / name NOT LIKE "test1%"
$dbx.notLike("name", "test1").match(false, true)
```

  * `[ $dbx.orLike(col, ...values) ](./js-database.md#dbx-orlikecol-values)`   
This is similar to `like()` except that the column must be one of the provided values, aka. multiple values are concatenated with `OR` instead of `AND`. 

```javascript
/ name LIKE "%test1%" OR name LIKE "%test2%" $dbx.orLike("name", "test1", "test2") / / name LIKE "test1%"
OR name LIKE "test2%"
$dbx.orLike("name", "test1", "test2").match(false, true)
```

  * `[ $dbx.orNotLike(col, ...values) ](./js-database.md#dbx-ornotlikecol-values)`   
This is similar to `notLike()` except that the column must not be one of the provided values, aka. multiple values are concatenated with `OR` instead of `AND`. 

```javascript
/ name NOT LIKE "%test1%" OR name NOT LIKE "%test2%" $dbx.orNotLike("name", "test1", "test2") / / name NOT LIKE "test1%"
OR name NOT LIKE "test2%"
$dbx.orNotLike("name", "test1", "test2").match(false, true)
```

  * `[ $dbx.exists(exp) ](./js-database.md#dbx-existsexp)`   
Prefix with `EXISTS` the specified expression (usually a subquery). 

```sql
/ EXISTS (SELECT 1 FROM users WHERE status = 'active') $dbx.exists(dbx.exp("SELECT 1 FROM users WHERE status = 'active'"))
```

  * `[ $dbx.notExists(exp) ](./js-database.md#dbx-notexistsexp)`   
Prefix with `NOT EXISTS` the specified expression (usually a subquery). 

```sql
/ NOT EXISTS (SELECT 1 FROM users WHERE status = 'active') $dbx.notExists(dbx.exp("SELECT 1 FROM users WHERE status = 'active'"))
```

  * `[ $dbx.between(col, from, to) ](./js-database.md#dbx-betweencol-from-to)`   
Generates a `BETWEEN` expression with the specified range. 

```
/ age BETWEEN 3 and 99 $dbx.between("age", 3, 99)
```

  * `[ $dbx.notBetween(col, from, to) ](./js-database.md#dbx-notbetweencol-from-to)`   
Generates a `NOT BETWEEN` expression with the specified range. 

```
/ age NOT BETWEEN 3 and 99 $dbx.notBetween("age", 3, 99)
```

##### [ orderBy(), andOrderBy() ](./js-database.md#orderby-andorderby)

The `orderBy(...cols)` specifies the `ORDER BY` clause of the query.   
A column name can contain _"ASC"_ or _"DESC"_ to indicate its ordering direction.   
You can also use `andOrderBy(...cols)` to append additional columns to an existing `ORDER BY` clause.

```javascript
$app.dao().db().select("users.*").from("users").orderBy("created ASC", "updated DESC").andOrderBy("title ASC")...
```

##### [ groupBy(), andGroupBy() ](./js-database.md#groupby-andgroupby)

The `groupBy(...cols)` specifies the `GROUP BY` clause of the query.   
You can also use `andGroupBy(...cols)` to append additional columns to an existing `GROUP BY` clause.

```javascript
$app.dao().db().select("users.*").from("users").groupBy("department", "level")...
```

##### [ having(), andHaving(), orHaving() ](./js-database.md#having-andhaving-orhaving)

The `having(exp)` specifies the `HAVING` clause of the query.   
Similarly to `where(exp)`, it accept a single `dbx.Expression` (see all available expressions listed above).   
You can also use `andHaving(exp)` or `orHaving(exp)` to append additional one or more conditions to an existing `HAVING` clause.

```javascript
$app.dao().db().select("users.*").from("users").groupBy("department", "level").having($dbx.exp("sum(level) > {:sum}", {
    sum: 10
}))...
```

##### [ limit() ](./js-database.md#limit)

The `limit(number)` method specifies the `LIMIT` clause of the query.

```javascript
$app.dao().db().select("users.*").from("users").limit(30)...
```

##### [ offset() ](./js-database.md#offset)

The `offset(number)` method specifies the `OFFSET` clause of the query. Usually used together with `limit(number)`.

```javascript
$app.dao().db().select("users.*").from("users").offset(5).limit(30)...
```

### [ Transaction ](./js-database.md#transaction)

To execute multiple queries in a transaction you can use `$app.dao().runInTransaction()`

You can nest `Dao.runInTransaction()` as many times as you want.

**The transaction will be committed only if there are no errors.**

```javascript
$app.dao().runInTransaction((txDao) => { // update a record const record = txDao.findRecordById("articles", "RECORD_ID") record.set("status", "active") txDao.saveRecord(record) // run some custom raw query txDao.db().newQuery("DELETE FROM articles WHERE;
            status = 'pending'
            ").execute() });
```

### [ Dao without event hooks ](./js-database.md#dao-without-event-hooks)

By default all Dao write operations (create, update, delete) trigger the `onModel*` event hooks.   
If you don't want this behavior, you can create a new Dao without hooks from an existing one by calling `Dao.withoutHooks()` or instantiate a new one with `new Dao(db, [nonconcurrentDB])`:

```javascript
const record = $app.dao().findRecordById("articles", "RECORD_ID") // the below WILL fire the onModelBeforeUpdate and onModelAfterUpdate hooks $app.dao().saveRecord(record) // the below WILL NOT fire the onModelBeforeUpdate and onModelAfterUpdate hooks const;
dao = $app.dao().withoutHooks() // or new Dao($app.dao().db()) dao.saveRecord(record);
```

[FAQ](https://pocketbase.io/old/faq) [Discussions](https://github.com/pocketbase/pocketbase/discussions) [Documentation](https://pocketbase.io/old/docs) [JavaScript SDK](https://github.com/pocketbase/js-sdk) [Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket **Base**

[__](mailto:support@pocketbase.io)[__](https://twitter.com/pocketbase)[__](https://github.com/pocketbase/pocketbase)

© 2023-2025 Pocket **Base** The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)

__

Extend with JavaScript - Database - Docs - PocketBase
