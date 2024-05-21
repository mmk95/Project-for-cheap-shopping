import openpyxl
import mysql.connector
from mysql.connector import Error

path = '../Project/files/Speciál_termékek/Transformed/specials.xlsx'

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

        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            product = row[0]
            shop = row[1]
            price = row[2]
            prodName = row[3]
            categoryName = row[4]
            groupName = row[5]
            sql = "INSERT INTO specials (product, shop, price, prodName, categoryName, groupName) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (product, shop, price, prodName, categoryName, groupName))

        connection.commit()
        print("Data inserted successfully into MySQL table")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")