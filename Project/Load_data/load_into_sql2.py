import csv
import mysql.connector
from mysql.connector import Error

path = '../Project/files/category_name.csv'

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
                categoryName = row[0]
                groupName = ','.join(row[1:])
                sql = "INSERT INTO prodCategories (categoryName, groupName) VALUES (%s, %s)"
                cursor.execute(sql, (categoryName, groupName))

        connection.commit()
        print("Data inserted successfully into MySQL table")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
