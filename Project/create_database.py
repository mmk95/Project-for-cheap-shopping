import mysql.connector

config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost'
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

cursor.execute("DROP DATABASE IF EXISTS mydatabase")
cursor.execute("CREATE DATABASE mydatabase")
cursor.execute("USE mydatabase")

table_creation_statements = [
    "DROP TABLE IF EXISTS prodGroups",
    """
    CREATE TABLE prodGroups (
        groupName VARCHAR(50) PRIMARY KEY
    )
    """,
    "DROP TABLE IF EXISTS prodCategories",
    """
    CREATE TABLE prodCategories (
        categoryName VARCHAR(50) PRIMARY KEY,
        groupName VARCHAR(50),
        FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
    )
    """,
    "DROP TABLE IF EXISTS prodName",
    """
    CREATE TABLE prodName (
        prodName VARCHAR(50) PRIMARY KEY,
        categoryName VARCHAR(50),
        groupName VARCHAR(50),
        FOREIGN KEY (categoryName) REFERENCES prodCategories(categoryName),
        FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
    )
    """,
    "DROP TABLE IF EXISTS milks",
    """
    CREATE TABLE milks (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        product VARCHAR(100),
        shop VARCHAR(50),
        price BIGINT,
        prodName VARCHAR(50),
        categoryName VARCHAR(50),
        groupName VARCHAR(50),
        FOREIGN KEY (prodName) REFERENCES prodName(prodName),
        FOREIGN KEY (categoryName) REFERENCES prodCategories(categoryName),
        FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
    )
    """,
    "DROP TABLE IF EXISTS meats",
    """
    CREATE TABLE meats (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        product VARCHAR(100),
        shop VARCHAR(50),
        price BIGINT,
        prodName VARCHAR(50),
        categoryName VARCHAR(50),
        groupName VARCHAR(50),
        FOREIGN KEY (prodName) REFERENCES prodName(prodName),
        FOREIGN KEY (categoryName) REFERENCES prodCategories(categoryName),
        FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
    )
    """,
    "DROP TABLE IF EXISTS breads",
    """
    CREATE TABLE breads (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        product VARCHAR(100),
        shop VARCHAR(50),
        price BIGINT,
        prodName VARCHAR(50),
        categoryName VARCHAR(50),
        groupName VARCHAR(50),
        FOREIGN KEY (prodName) REFERENCES prodName(prodName),
        FOREIGN KEY (categoryName) REFERENCES prodCategories(categoryName),
        FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
    )
    """,
    "DROP TABLE IF EXISTS durabels",
    """
    CREATE TABLE durabels (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        product VARCHAR(100),
        shop VARCHAR(50),
        price BIGINT,
        prodName VARCHAR(50),
        categoryName VARCHAR(50),
        groupName VARCHAR(50),
        FOREIGN KEY (prodName) REFERENCES prodName(prodName),
        FOREIGN KEY (categoryName) REFERENCES prodCategories(categoryName),
        FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
    )
    """,
    "DROP TABLE IF EXISTS fruits",
    """
    CREATE TABLE fruits (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        product VARCHAR(150),
        shop VARCHAR(50),
        price BIGINT,
        prodName VARCHAR(50),
        categoryName VARCHAR(50),
        groupName VARCHAR(50),
        FOREIGN KEY (prodName) REFERENCES prodName(prodName),
        FOREIGN KEY (categoryName) REFERENCES prodCategories(categoryName),
        FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
    )
    """,
    "DROP TABLE IF EXISTS specials",
    """
    CREATE TABLE specials (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        product VARCHAR(100),
        shop VARCHAR(50),
        price BIGINT,
        prodName VARCHAR(50),
        categoryName VARCHAR(50),
        groupName VARCHAR(50),
        FOREIGN KEY (prodName) REFERENCES prodName(prodName),
        FOREIGN KEY (categoryName) REFERENCES prodCategories(categoryName),
        FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
    )
    """
]

for statement in table_creation_statements:
    cursor.execute(statement)

connection.commit()
cursor.close()
connection.close()
