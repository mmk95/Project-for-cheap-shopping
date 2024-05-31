from frame import *
from treeviews import *

def load_data_into_treeview():
    if my_option.get() == 'Hús, felvágott':
        load = f"SELECT product, shop, price FROM meats Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}' ORDER BY price ASC;"
        
    elif my_option.get() == 'Kenyérfélék':
        load = f"SELECT product, shop, price FROM breads Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}'ORDER BY price ASC;"
        
    elif my_option.get() == 'Speciális étrend':
        load = f"SELECT product, shop, price FROM specials Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}'ORDER BY price ASC;"
        
    elif my_option.get() == 'Tartós élelmiszerek, italok':
        load = f"SELECT product, shop, price FROM durabels Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}'ORDER BY price ASC;"
    
    elif my_option.get() == 'Tejtermék, sajt, tojás':
        load = f"SELECT product, shop, price FROM milks Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}'ORDER BY price ASC;"
        
    elif my_option.get() == 'Zöldség, gyümölcs':
        load = f"SELECT product, shop, price FROM fruits Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}'ORDER BY price ASC;"
    cursor.execute(load)
    data = cursor.fetchall()
    treeview.delete(*treeview.get_children())

    columns_to_display = ["Termék neve", "Bolt", "Ár(Ft)"]
    for col_name in columns_to_display:
        treeview.heading(col_name, text=col_name)

    for row in data:
        treeview.insert("", "end", values=row, tags=('row_font',))
    treeview.tag_configure('row_font', font=("Helvetica", 12))

def update_my_options(current_value):
    if current_value == my_option.get():
        sql_query = f"SELECT categoryName FROM prodName WHERE groupName = '{current_value}';"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        categories = list(set(result[0] for result in results))
        my_option2.configure(values = categories)
        my_option2.set(categories[0])
        query = f"SELECT prodName FROM prodName WHERE groupName = '{current_value}' and categoryName = '{categories[0]}';"
        cursor.execute(query)
        results2 = cursor.fetchall()
        products = list(set(result[0] for result in results2))
        my_option3.configure(values = products)
        my_option2.set(categories[0])
        my_option3.set(products[0])
        load_data_into_treeview()

def update_my_option2(current_value):
    if current_value == my_option2.get():
        sql_query = f"SELECT prodName FROM prodName WHERE categoryName = '{current_value}';"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        categories = list(set(result[0] for result in results))
        my_option3.configure(values = categories)
        my_option3.set(categories[0])
        load_data_into_treeview()

def update_my_option3(current_value):
    if my_option.get() == 'Hús, felvágott':
        table = 'meats'        
    elif my_option.get() == 'Kenyérfélék':
        table = 'breads'         
    elif my_option.get() == 'Speciális étrend':
        table = 'specials'            
    elif my_option.get() == 'Tartós élelmiszerek, italok':
        table = 'durabels'        
    elif my_option.get() == 'Tejtermék, sajt, tojás':
        table = 'milks'            
    elif my_option.get() == 'Zöldség, gyümölcs':
        table = 'fruits'
    if current_value == my_option3.get():
        sql_query = f"SELECT prodName FROM prodName WHERE prodName = '{current_value}';"
        cursor.execute(sql_query)
        results = cursor.fetchone()
        result = results[0]
        load = f"SELECT product, shop, price FROM {table} Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{result}' ORDER BY price ASC;"
        cursor.execute(load)
        data = cursor.fetchall()
        treeview.delete(*treeview.get_children())
        columns_to_display = ["Termék neve", "Bolt", "Ár(Ft)"]
        for col_name in columns_to_display:
            treeview.heading(col_name, text=col_name)
        for row in data:
            treeview.insert("", "end", values=row, tags=('row_font',))
        treeview.tag_configure('row_font', font=("Helvetica", 12))

my_option = customtkinter.CTkOptionMenu(f1, values=load_data_into_menus(1), width=230, command=update_my_options, font=("Helvetica", 14))
my_option.grid(row=2, column=0, padx=10, pady=5)
my_option2 = customtkinter.CTkOptionMenu(f1, values=load_data_into_menus(2), command=update_my_option2, width=230, font=("Helvetica", 14))
my_option2.grid(row=2, column=1, padx=10, pady=5)
my_option3 = customtkinter.CTkOptionMenu(f1, values=load_data_into_menus(3), width=230, command=update_my_option3,font=("Helvetica", 14))
my_option3.grid(row=2, column=2, padx=10, pady=5)

load_data_into_treeview()