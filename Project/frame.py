import customtkinter, tkinter
import mysql.connector

def load_data_into_menus(main_index):
    query = "SELECT groupName FROM prodName;"
    cursor.execute(query)

    main = list(set([row[0] for row in cursor.fetchall()]))

    query2 = f"SELECT categoryName FROM prodName Where groupName = '{main[0]}';"
    cursor.execute(query2)

    main2 = [row[0] for row in cursor.fetchall()]

    query3 = f"SELECT prodName FROM prodName Where groupName = '{main[0]}' and categoryName = '{main2[0]}';"
    cursor.execute(query3)

    main3 = [row[0] for row in cursor.fetchall()]
    if main_index == 1:
        return main
    elif main_index == 2:
        return main2
    else:
        return main3

connection = mysql.connector.connect(
    host="localhost",
    database='mydatabase',
    user="root",
    password="12345",
    charset='utf8'
)

cursor = connection.cursor()

app = customtkinter.CTk()
f1 = tkinter.Frame(app)
f2 = tkinter.Frame(app)

for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')

app.geometry("750x750")
app.title('Vásárolj olcsón')

