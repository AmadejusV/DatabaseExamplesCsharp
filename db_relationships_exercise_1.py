from database import DatabaseContextManager


def create_t_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    amount_spent FLOAT
    )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_t_products():
    query = """CREATE TABLE IF NOT EXISTS Products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price FLOAT,
    description TEXT
    )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_t_customers_products():
    query = """CREATE TABLE IF NOT EXISTS Customers_Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY(product_id) REFERENCES Products(product_id),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
    )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_customer1(first_name: str, last_name: str, amount_spent: float):
    query = """INSERT INTO Customers(first_name, last_name, amount_spent) VALUES(?,?,?)"""
    parameters = [first_name, last_name, amount_spent]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def create_product(name: str, price: float, description: str):
    query = """INSERT INTO Products(name, price, description) VALUES(?,?,?)"""
    parameters = [name, price, description]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customers_products():
    query = """SELECT * FROM Customers_Products"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def get_customers_products_info():
    query = """SELECT * FROM Customers, Products
            LEFT JOIN Customers_Products
            WHERE Customers.customer_id = Customers_Products.customer_id
            AND Products.product_id = Customers_Products.product_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")



def drop_table():
    query = """DROP TABLE none"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def join_customer_product(customer_id: int, product_id: int):
    query = """INSERT INTO Customers_Products(customer_id, product_id) VALUES(?,?)"""
    parameters = [customer_id, product_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)




#drop_table()
#create_t_customers()
#create_t_products()
#create_t_customers_products()

#create_product("pienas1", 1.10, "geras")
#create_product("miltai1", 1.50, "birus")
#create_product("kava1", 3.50, "juoda")

#create_customer1("vardenis1", "pavardenis", 5.10)
#create_customer1("vardene1", "pavardene", 4.10)
#create_customer1("varde1", "pavarde", 3.10)

#join_customer_product(1, 4)
#join_customer_product(1, 3)
#join_customer_product(2, 4)
#join_customer_product(3, 2)
#join_customer_product(4, 3)

get_customers_products()

get_customers_products_info()