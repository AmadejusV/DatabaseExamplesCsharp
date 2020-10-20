from database import DatabaseContextManager

def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER, 
    company_id INTEGER
    )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

def drop_table():
    query = """DROP TABLE Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count INTEGER,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES Companies(company_id)
    )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)



def create_customer(first_name: str, last_name: str, age: int, company_id: int):
    query = """INSERT INTO Customers(first_name, last_name, age) VALUES(?,?,?,?)"""
    parameters = [first_name, last_name, age, company_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def create_company(company_name: str, employee_count: int):
    query = """INSERT INTO Companies(company_name, employee_count) VALUES(?,?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def get_companies_customers():
    query = """SELECT * FROM Customers JOIN Companies
    ON (customer_id = company_id)
    WHERE customer_id > 0"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")

def update_customer_name(old_fname: str, new_fname: str):
    query = """UPDATE Customers
                SET first_name = ?
                WHERE first_name = ?"""
    parameters = [new_fname, old_fname]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def update_customer_last_name(old_lname: str, new_lname: str):
    query = """UPDATE Customers
                SET last_name = ?
                WHERE last_name =?"""
    parameters = [old_lname, new_lname]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def update_customer_age(old_age: str, new_age: str):
    query = """UPDATE Customers
                SET age = ?
                WHERE age =?"""
    parameters = [old_age, new_age]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_customer(first_name: str):
    query = """DELETE FROM Customers
                WHERE first_name = ?"""
    parameters = [first_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)



