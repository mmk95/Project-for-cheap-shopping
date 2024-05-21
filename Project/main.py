from tkinter import NS
import csv
import customtkinter, tkinter
from tkinter import ttk
import os
import mysql.connector
import pandas as pd



connection = mysql.connector.connect(
    host="localhost",
    database='mydatabase',
    user="root",
    password="12345",
    charset='utf8'
)

cursor = connection.cursor()


def raise_frame(frame):
    frame.tkraise()

def remove_selected_items():
    global total_price
    selected_items = treeview2.selection()
    for item in selected_items:
        item_values = treeview2.item(item, 'values')
        price = int(item_values[2])
        total_price -= price
        treeview2.delete(item)
    update_total_label()
  
def copy_data_to_frame2():
    for item in treeview3.get_children():
        treeview3.delete(item)

    for item in treeview2.get_children():
        item_values = treeview2.item(item, 'values')
        treeview3.insert('', 'end', values=item_values, tags=('row_font',))
    treeview3.tag_configure('row_font', font=("Helvetica", 12))

def delete_csv_file():
    csv_filename = "treeview_data.csv"
    if os.path.exists(csv_filename):
        os.remove(csv_filename)

def filter_with_sticker(index):
    global total_price2
    csv_filename = "treeview_data.csv"
    if not os.path.exists(csv_filename):
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in treeview4.get_children():
                values = treeview4.item(item, "values")
                writer.writerow(values)

    for i in range(len(stickers)):
        if i == index:
            stickers[i].configure(fg_color="orange", hover_color="orange")
        else:
            stickers[i].configure(fg_color="grey", hover_color="grey")

    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        count = {}
        for row in reader:
            row_tuple = tuple(row)
            if row_tuple in count:
                count[row_tuple] += 1
            else:
                count[row_tuple] = 1

    for item in treeview4.get_children():
        treeview4.delete(item)

    for row, db in count.items():
        product = row[0]
        shop = row[1]
        price = int(row[2])
        product_with_count = f'{product} ({db} db)'
        price_value = price * db
        treeview4.insert('', 'end', values=[product_with_count, shop, price_value])             
    
    selected_sticker = stickers[index]
    filter_value = selected_sticker.cget("text")
    
    for item in treeview4.get_children():
        item_value = treeview4.item(item, "values")[1]

        if item_value != filter_value:
            treeview4.detach(item) 
        else:
            if item not in treeview4.get_children():
                treeview4.reattach(item, '', 'end')

    item_values = treeview4.item(item, 'values')
    item_id = item_values[0]
    item_counts = {}
    item_counts[item_id] = item_counts.get(item_id, 0) + 1
    total_price2 = 0
    for child in treeview4.get_children():
        item_values = treeview4.item(child, 'values')
        item_id = item_values[0]
        price = int(item_values[2])
        total_price2 += price * item_counts.get(item_id, 1)
    update_total_label()
    
def update_total_label():
    price_label.configure(text="Végösszeg: \n{} ft".format(total_price))
    price_label1.configure(text="Végösszeg: \n{} ft".format(total_price))
    totalprice_label.configure(text="Végösszeg: \n{} ft".format(total_price2))

def move_selected_items():
    global total_price
    selected_items = treeview.selection()
    
    item_counts = {}
    
    for item in selected_items:
        item_values = treeview.item(item, 'values')
        item_id = item_values[0]
        
        existing_item = None
        for child in treeview2.get_children():
            child_value = treeview2.item(child, 'values')[0]
            if item_id in child_value:
                existing_item = child
                break
        
        if existing_item:
            existing_values = treeview2.item(existing_item, 'values')
            start_index = existing_values[0].find('(')
            product = existing_values[0]
            found_number = ""
            times = 2
            if start_index != -1:
                for char in product[start_index + 1:start_index + 3]:
                    if char.isdigit():
                        found_number += char
                        found_number_int = int(found_number)
                        found_number_int += 1
                        product = product[:start_index - 1]
                        new_string = f'{product} ({found_number_int} db)'
                        new_price = int(existing_values[2]) + int(item_values[2])
                    treeview2.item(existing_item, values=(new_string, existing_values[1], new_price))
            else:
                new_string = f'{existing_values[0]} ({times} db)'
                existing_price = int(existing_values[2])
                new_price = existing_price+int(item_values[2])
                treeview2.item(existing_item, values=(new_string, existing_values[1], new_price))
        else:
            treeview2.insert('', 'end', values=item_values, tags=('row_font',))
        
        item_counts[item_id] = item_counts.get(item_id, 0) + 1

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

        if item_values[1] == 'Tesco':
            load1 = f"SELECT product,shop, price FROM {table} Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}' ORDER BY price ASC"
            cursor.execute(load1)

        elif item_values[1] == 'Aldi':
            load1 = f"SELECT product,shop, price FROM {table} Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}' ORDER BY price ASC"
            cursor.execute(load1)

        elif item_values[1] == 'Lidl':
            load1 = f"SELECT product,shop, price FROM {table} Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}' ORDER BY price ASC"
            cursor.execute(load1)

        elif item_values[1] == 'Spar':
            load1 = f"SELECT product,shop, price FROM {table} Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}' ORDER BY price ASC"
            cursor.execute(load1)

        elif item_values[1] == 'Auchan':
            load1 = f"SELECT product,shop, price FROM {table} Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}' ORDER BY price ASC"

            cursor.execute(load1)
        
        elif item_values[1] == 'Penny':
            load1 = f"SELECT product,shop, price FROM {table} Where groupName = '{my_option.get()}' and categoryName = '{my_option2.get()}' and prodName = '{my_option3.get()}' ORDER BY price ASC"
            cursor.execute(load1)
        first_element = cursor.fetchall()

        columns_to_display = ["Termék neve", "Bolt", "Ár(Ft)"]
        for col_name in columns_to_display:
            treeview4.heading(col_name, text=col_name)


        cheapest_products = {}
        for product, shop, price in first_element:
            if shop not in cheapest_products or price < cheapest_products[shop][2]:
                cheapest_products[shop] = (product, shop, price)
        
        for product, shop, price in cheapest_products.values():
            treeview4.insert("", "end", values=(product, shop, price), tags=('row_font',))
        
        existing_item = None
        for child in treeview4.get_children():
            child_value = treeview4.item(child, 'values')[0]
            if item_id in child_value:
                existing_item = child
                break

        for existing_item in treeview4.get_children():
            existing_values = treeview4.item(existing_item, 'values')
            if existing_values not in cheapest_products:
                start_index = existing_values[0].find('(')
                product = existing_values[0]
                found_number = ""

                if start_index != -1:
                    for char in product[start_index + 1:start_index + 3]:
                        if char.isdigit():
                            found_number += char
                            found_number_int = int(found_number)
                            found_number_int += 1
                            product = product[:start_index - 1]
                            new_string = f'{product}'
                            new_price = int(existing_values[2])
                    treeview4.item(existing_item, values=(new_string, existing_values[1], existing_values[2]))
                else:
                    new_string = f'{existing_values[0]}'
                    existing_price = int(existing_values[2])
                    treeview4.item(existing_item, values=(new_string, existing_values[1], existing_price))
            else:
                treeview4.insert('', 'end', values=item_values, tags=('row_font',))


    total_price = 0
    for child in treeview2.get_children():
        item_values = treeview2.item(child, 'values')
        item_id = item_values[0]
        price = int(item_values[2])
        total_price += price * item_counts.get(item_id, 1)
    
    treeview2.tag_configure('row_font', font=("Helvetica", 12))
    update_total_label()

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

def save_to_excel2():
    filename = 'shopping_list.xlsx'
    data = []
    for item in treeview4.get_children():
        values = treeview4.item(item, "values")
        data.append(values)
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, header=False)

def save_to_excel():
    filename = 'shopping_list.xlsx'
    data = []
    for item in treeview3.get_children():
        values = treeview3.item(item, "values")
        data.append(values)
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, header=False)

app = customtkinter.CTk()
f1 = tkinter.Frame(app)
f2 = tkinter.Frame(app)

for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')

app.geometry("750x710")
app.title('Vásárolj olcsón')
total_price = 0
total_price2 = 0
welcome_label = customtkinter.CTkLabel(f1, text_color="#003d61", font=("Helvetica", 24), text="Üdvözöljük!")
welcome_label.grid(row=0, columnspan=3, padx=5, pady=40)
text_label = customtkinter.CTkLabel(f1, text_color="#003d61", font=("Helvetica", 16),
                                   text="Adja meg az élelmiszer típust, aminek az árára kíváncsi.")
text_label.grid(row=1, columnspan=3, padx=5, pady=5)

text_label2 = customtkinter.CTkLabel(f1, text_color="#003d61", font=("Helvetica", 16),
                                   text="Kérem válassza ki azt a terméket, amit a kosárba helyezne.")
text_label2.grid(row=3, columnspan=3, padx=50, pady=5)

treeFrame = ttk.Frame(f1)
treeFrame.grid(row=4, columnspan=3, pady=10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

tree_cols = ("Termék neve", "Bolt", "Ár(Ft)")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set,style="Treeview", columns=tree_cols, height=10)
treeview.column("Termék neve", width=270)
treeview.column("Bolt", width=270)
treeview.column("Ár(Ft)", width=270)
treeview.pack()
treeScroll.config(command=treeview.yview)

my_option = customtkinter.CTkOptionMenu(f1, values=load_data_into_menus(1), width=230, command=update_my_options, font=("Helvetica", 14))
my_option.grid(row=2, column=0, padx=10, pady=5)
my_option2 = customtkinter.CTkOptionMenu(f1, values=load_data_into_menus(2), command=update_my_option2, width=230, font=("Helvetica", 14))
my_option2.grid(row=2, column=1, padx=10, pady=5)
my_option3 = customtkinter.CTkOptionMenu(f1, values=load_data_into_menus(3), width=230, command=update_my_option3,font=("Helvetica", 14))
my_option3.grid(row=2, column=2, padx=10, pady=5)
load_data_into_treeview()
delete_csv_file()
put_label = customtkinter.CTkButton(f1, text="Kosárba helyezés", width=700, height=30, font=("Helvetica", 14), command=move_selected_items)
put_label.grid(row=5, columnspan=3, padx=5, pady=5)

treeFrame2 = ttk.Frame(f1)
treeFrame2.grid(row=6, columnspan=3, padx=5, pady=(5,10))
treeScroll2 = ttk.Scrollbar(treeFrame2)
treeScroll2.pack(side="right", fill="y")
treeview2 = ttk.Treeview(treeFrame2, show="headings",
                        yscrollcommand=treeScroll2.set, columns=tree_cols, height=10)

for tree_col in tree_cols:
    treeview2.heading(tree_col, text=tree_col)

treeview2.column("Termék neve", width=270)
treeview2.column("Bolt", width=270)
treeview2.column("Ár(Ft)", width=270)
treeview2.pack()
treeScroll2.config(command=treeview2.yview)

cart_label = customtkinter.CTkButton(f1, text="Kosár", width=80, height=50, font=("Helvetica", 14), command=lambda: [copy_data_to_frame2(), raise_frame(f2)])
cart_label.grid(row=7, column=1, padx=5, pady=5)
delete_button = customtkinter.CTkButton(f1, text="Törlés", width=80, height=50, font=("Helvetica", 14), fg_color="#DB3E39", hover_color="#C4191C", command=remove_selected_items)
delete_button.grid(row=7, column=0, padx=5, pady=5)
price_label = customtkinter.CTkLabel(f1, text="Végösszeg: ", text_color="#003d61", font=("Helvetica", 16))
price_label.grid(row=7, column=2, padx=5, pady=5)

#second frame

secondTop_label = customtkinter.CTkLabel(f2, text_color="#003d61", font=("Helvetica", 24), text="Kosár")
secondTop_label.grid(row=0, columnspan=6, padx=5, pady=(10,25))

treeFrame3 = ttk.Frame(f2)
treeFrame3.grid(row=1, columnspan=6, padx=5, pady=(5,15))
treeScroll3 = ttk.Scrollbar(treeFrame3)
treeScroll3.pack(side="right", fill="y")
treeview3 = ttk.Treeview(treeFrame3, show="headings",
                        yscrollcommand=treeScroll3.set, columns=tree_cols, height=11)

for tree_col in tree_cols:
    treeview3.heading(tree_col, text=tree_col)

treeview3.column("Termék neve", width=270)
treeview3.column("Bolt", width=270)
treeview3.column("Ár(Ft)", width=270)
treeview3.pack()
treeScroll3.config(command=treeview3.yview)

text_label3 = customtkinter.CTkLabel(f2, text_color="#003d61", font=("Helvetica", 16),
                                  text="Ha egy boltban szeretne vásárolni.")
text_label3.grid(row=2, columnspan=6, padx=5, pady=(5,15))
price_label1 = customtkinter.CTkLabel(f2, text="Végösszeg: ", text_color="#003d61", font=("Helvetica", 16))
price_label1.grid(row=2, column=5, padx=5, pady=5)
save_button = customtkinter.CTkButton(f2, text="Mentés", width=80, height=50, font=("Helvetica", 14), fg_color="black", hover_color="black" ,command=save_to_excel)
save_button.grid(row=2, column=0, padx=(25,0), pady=5)

listofshops = ['Lidl', 'Aldi', 'Penny', 'Tesco', 'Auchan', 'Spar']
stickers = []
for i in range(6):
    sticker = customtkinter.CTkButton(f2, text=listofshops[i], width=70, height=70, fg_color="grey", hover_color="grey")
    sticker.grid(row=3, column=i, padx=5, pady=5)
    sticker.configure(command=lambda index=i: filter_with_sticker(index))
    stickers.append(sticker)

treeFrame4 = ttk.Frame(f2)
treeFrame4.grid(row=5, columnspan=6, padx=35, pady=(15,15))
treeScroll4 = ttk.Scrollbar(treeFrame4)
treeScroll4.pack(side="right", fill="y")
treeview4 = ttk.Treeview(treeFrame4, show="headings",
                        yscrollcommand=treeScroll4.set, columns=tree_cols, height=11)

for tree_col in tree_cols:
    treeview4.heading(tree_col, text=tree_col)

treeview4.column("Termék neve", width=270)
treeview4.column("Bolt", width=270)
treeview4.column("Ár(Ft)", width=270)
treeview4.pack()
treeScroll4.config(command=treeview4.yview)

back_button = customtkinter.CTkButton(f2, text="Vissza", width=80, height=50, font=("Helvetica", 14), command=lambda:raise_frame(f1))
back_button.grid(row=6, columnspan=6, padx=(25,0), pady=5)
save_button2 = customtkinter.CTkButton(f2, text="Mentés", width=80, height=50, font=("Helvetica", 14), fg_color="black", hover_color="black" ,command=save_to_excel2)
save_button2.grid(row=6, column=0, padx=(25,0), pady=5)
totalprice_label = customtkinter.CTkLabel(f2, text="Végösszeg: ", text_color="#003d61", font=("Helvetica", 16))
totalprice_label.grid(row=6, column=5, padx=5, pady=5)

raise_frame(f1)
app.mainloop()
delete_csv_file()