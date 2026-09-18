import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        department_name VARCHAR(100)
    )
""")
cursor.execute("""
    INSERT OR IGNORE INTO departments (id, department_name)
    VALUES (10, 'Engineering'),
           (20, 'HR'),
           (30, 'Finance');
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100),
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments (id)
    )
""")
cursor.execute("""
    INSERT OR IGNORE INTO employees (id, name, department_id)
    VALUES (1, 'Rahul', 10),
           (2, 'Priya', 20),
           (3, 'Anu', 10),
           (4, 'Ravi', 30);
""")
cursor.execute("""
    SELECT employees.name, departments.department_name
    FROM employees
    INNER JOIN departments ON employees.department_id = departments.id;
""")
cursor.execute("""
            SELECT employees.name, departments.department_name
            FROM employees
            INNER JOIN departments
            ON employees.department_id = departments.id
            WHERE employees.department_id = 10;
""")

cursor.execute("""
    SELECT employees.name, departments.department_name
    FROM employees
    LEFT JOIN departments 
    ON employees.department_id = departments.id
""")
print(cursor.fetchall())
connection.commit()
cursor.execute("SELECT * FROM departments;")

connection.close()