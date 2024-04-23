# SQLAlchemy CRUD Operations

This project demonstrates how to perform CRUD (Create, Read, Update, Delete) operations using SQLAlchemy's Object-Relational Mapping (ORM) with a PostgreSQL database.

## Prerequisites
- Python 3.x
- PostgreSQL database
- SQLAlchemy library

## Getting Started

### Create the Database Connection:
- The code creates a database engine using `create_engine()` and connects to the "chinook" database.
- The `declarative_base()` function is used to create a base class for the ORM models.

### Define the ORM Models:
- The `Programmer` class is defined as an ORM model, representing the "Programmer" table in the database.
- The table name is specified using the `__tablename__` attribute, and the column definitions are made using `Column` objects.

### Perform CRUD Operations:

#### Create:
- New programmer records are created and added to the session.
- The changes are committed to the database using `session.commit()`.

#### Read:
- Queries are executed using the `session.query()` method to retrieve data from the "Programmer" table.
- The results are printed to the console.

#### Update:
- A single record is updated by modifying the `famous_for` attribute.
- Multiple records are updated by changing the `gender` attribute based on the existing value.

#### Delete:
- A single record is deleted by prompting the user for the first and last name, and then deleting the corresponding record.
- All records can be deleted by iterating through the `Programmer` objects and deleting them one by one.

### Error Handling:
- The code handles the case where the "Gender not defined" message is printed when updating the gender attribute.
- The issue is related to the case-sensitivity of the gender variable, and the solution is to ensure that the case matches the way the variable was defined.

### Optimization:
- When deleting multiple/all records, the code is updated to use a batch-based approach to improve efficiency and maintain data consistency.

## Additional Approaches
In addition to the SQLAlchemy ORM approach, we have also covered the following ways to interact with the PostgreSQL database:
- SQL-CRUD: Using raw SQL queries and the psycopg2 library to perform CRUD operations.
- SQL-Expression: Using the SQLAlchemy Expression Language to write SQL-like queries in Python.
- SQL-psycopg2: Using the psycopg2 library directly to execute SQL queries, without an ORM.
Each approach has its own advantages and use cases, and the choice depends on the specific requirements of your project, the complexity of the database schema, and your team's familiarity with the different tools and libraries.

## Running the Script
- Ensure that you have a PostgreSQL database named "chinook" set up and accessible.
- Run the `sql-crud.py` script using Python:  

python3 sql-crud.py

This will execute the CRUD operations and display the results in the console.

## Conclusion
This project demonstrates how to use SQLAlchemy's ORM to perform CRUD operations on a PostgreSQL database. It covers various aspects of working with SQLAlchemy, including model definition, querying, updating, and deleting records. The code also includes examples of handling case-sensitivity issues and optimizing the deletion process.
