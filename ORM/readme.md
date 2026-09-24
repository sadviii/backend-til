# ORM — SQLAlchemy

## Topics Covered

* ORM (Object-Relational Mapping)
* SQLAlchemy Engine
* Declarative Base
* ORM Models
* `Mapped` and `mapped_column`
* Primary Keys
* Foreign Keys
* `Base.metadata.create_all()`
* SQLAlchemy Sessions
* CRUD Operations

  * Create
  * Read
  * Update
  * Delete
* ORM Relationships using `relationship()`
* Querying with `query()` and `filter_by()`
* `session.add()`
* `session.commit()`
* `session.delete()`

## Hands-on Practice

Built an Employee–Department database using Python, SQLAlchemy, and SQLite.

Implemented:

* `Employee` ORM model
* `Department` ORM model
* Foreign-key relationship between employees and departments
* Creating database tables through SQLAlchemy
* Creating and saving records using ORM
* Reading records using queries
* Updating existing records
* Deleting records
* Accessing related department data using:
  `employee.department.department_name`

## Key Takeaways

* ORM maps Python classes to database tables.
* Python objects represent database rows.
* `Mapped` attributes represent database columns.
* A `ForeignKey` connects related database tables.
* `relationship()` allows related objects to be accessed through Python.
* A `Session` manages communication between Python objects and the database.
* `commit()` permanently saves pending changes.
* ORM allows database operations using Python instead of writing raw SQL for every operation.

## Final Competency

Successfully built and tested an SQLAlchemy ORM workflow that:

1. Created Department and Employee models.
2. Created tables in SQLite.
3. Created HR department and an employee.
4. Read employee data using ORM queries.
5. Accessed related department information through an ORM relationship.
6. Updated employee information.
7. Deleted an employee.
8. Verified the deletion.
