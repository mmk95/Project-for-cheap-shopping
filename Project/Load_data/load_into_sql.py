import csv
import mysql.connector
from mysql.connector import Error

path = '../Project/files/group_names.csv'

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
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                category_name = ','.join(row)  # Join the fields into a single string
                sql = "INSERT INTO prodGroups (groupName) VALUES (%s)"
                cursor.execute(sql, (category_name,))

        connection.commit()
        print("Data inserted successfully into MySQL table")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
