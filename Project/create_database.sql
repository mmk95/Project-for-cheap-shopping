DROP DATABASE IF EXISTS mydatabase;
CREATE DATABASE mydatabase;
USE mydatabase;

DROP TABLE IF EXISTS prodGroups;
CREATE TABLE prodGroups (
    groupName VARCHAR(50) PRIMARY KEY
);

DROP TABLE IF EXISTS prodCategories;
CREATE TABLE prodCategories (
    categoryName VARCHAR(50) PRIMARY KEY,
    groupName VARCHAR(50),
    FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
);

DROP TABLE IF EXISTS prodName;
CREATE TABLE prodName (
    prodName VARCHAR(50) PRIMARY KEY,
    categoryName VARCHAR(50),
    groupName VARCHAR(50),
    FOREIGN KEY (categoryName) REFERENCES prodCategories(categoryName),
    FOREIGN KEY (groupName) REFERENCES prodGroups(groupName)
);

DROP TABLE IF EXISTS milks;
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
);

DROP TABLE IF EXISTS meats;
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
);

DROP TABLE IF EXISTS breads;
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
);

DROP TABLE IF EXISTS durabels;
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
);

DROP TABLE IF EXISTS fruits;
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
);

DROP TABLE IF EXISTS specials;
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
);

SELECT 
    groupName
FROM
    prodGroups;
    
SELECT 
    *
FROM
    prodCategories;
    
SELECT 
    *
FROM
    milks;
    
SELECT product,shop, price FROM meats Where groupName = 'Zöldség, gyümölcs' and categoryName = 'Gyümölcs' and prodName = 'Narancs' ORDER BY price ASC;
SELECT product,shop, price FROM meats Where groupName = 'Hús, felvágott' and categoryName = 'Felvágottak' and prodName = 'Párizsi' ORDER BY price ASC;

SELECT 
    *
FROM
    durabels;