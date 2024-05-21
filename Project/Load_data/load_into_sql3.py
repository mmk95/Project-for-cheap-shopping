import csv
import mysql.connector
from mysql.connector import Error

path = '../Project/files/names.csv'

try:
    connection = mysql.connector.connect(
        host="localhost",
        database='mydatabase',
        user="root",
        password="12345",
        charset='utf8'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        with open(path, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            for row in csvreader:
                prodName = row[0]
                categoryName = row[1]
                groupName = row[2]
                sql = "INSERT INTO prodName (prodName, categoryName, groupName) VALUES (%s, %s,%s)"
                cursor.execute(sql, (prodName, categoryName, groupName))

        connection.commit()
        print("Data inserted successfully into MySQL table")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
