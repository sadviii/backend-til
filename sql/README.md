
# Relational Databases & SQL

## Topics Covered

* Relational databases

  * Tables, rows, columns, and records
  * Relationship between tables
* SQL

  * `SELECT`
  * `WHERE`
  * Comparison operators
  * `INSERT`
  * `UPDATE`
  * `CREATE TABLE`
* SQL JOINs

  * `INNER JOIN`
  * `LEFT JOIN`
  * `RIGHT JOIN`
  * `ON` clause
* Keys

  * Primary Keys
  * Foreign Keys
  * Referential integrity
* Normalization

  * Reducing duplicate data
  * Separating related data into tables
* Python + SQLite

  * Connecting to a database using `sqlite3`
  * Executing SQL queries from Python
  * Committing database changes

## Hands-on Practice

Created a SQLite database called `company.db` and built:

### `departments`

```text
id | department_name
10 | Engineering
20 | HR
30 | Finance
```

### `employees`

```text
id | name  | department_id
1  | Rahul | 10
2  | Priya | 20
3  | Anu   | 10
4  | Ravi  | 30
```

Created a foreign-key relationship:

```text
employees.department_id → departments.id
```

Practiced SQL queries including:

```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;
```

and:

```sql
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.id;
```

Also practiced filtering joined data using `WHERE`.

## Key Takeaways

* A relational database stores data in related tables.
* A Primary Key uniquely identifies a record.
* A Foreign Key connects records between tables.
* `INNER JOIN` returns matching records.
* `LEFT JOIN` preserves every row from the left table.
* `RIGHT JOIN` preserves every row from the right table.
* The left/right table depends on the table's position in the SQL query.
* Normalization reduces unnecessary duplication and helps maintain consistent data.
* SQL can be executed from Python using SQLite.

## Final Competency

Built and queried a relational SQLite database using Python and demonstrated the ability to:

* Design related tables
* Define Primary and Foreign Keys
* Insert and update data
* Write raw SQL JOINs
* Filter query results
* Apply normalization principles
* Execute and verify SQL against a real database


