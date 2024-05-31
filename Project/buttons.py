import csv
import os
import pandas as pd
from frame import *
from treeviews import *
from options import *
from texts import *

total_price = 0
total_price2 = 0

class Buttons:
    def __init__(self, parent, text, width, height, font, fg_color, hover_color, command = None, row = None, column=None, columnspan=None, padx=5, pady=5):
        self.button = customtkinter.CTkButton(parent, text=text, width=width, height=height, font=font, fg_color=fg_color, hover_color=hover_color, command=command)
        if columnspan is not None:
            self.button.grid(row=row, columnspan=columnspan, padx=padx, pady=pady)
        else:
            self.button.grid(row=row, column=column, padx=padx, pady=pady)
    def configure(self):
        self.button.configure()

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
    price_label.update_text("Végösszeg: \n{} ft".format(total_price))
    price_label1.update_text("Végösszeg: \n{} ft".format(total_price))
    totalprice_label.update_text("Végösszeg: \n{} ft".format(total_price2))

def raise_frame(frame):
    frame.tkraise()

def save_to_excel_treeview4(filename = 'shopping_list.xlsx'):
    data = []
    for item in treeview4.get_children():
        values = treeview4.item(item, "values")
        data.append(values)
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, header=False)

def save_to_excel_treeview3(filename = 'shopping_list.xlsx'):
    data = []
    for item in treeview3.get_children():
        values = treeview3.item(item, "values")
        data.append(values)
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, header=False)

def copy_data_to_frame2():
    for item in treeview3.get_children():
        treeview3.delete(item)

    for item in treeview2.get_children():
        item_values = treeview2.item(item, 'values')
        treeview3.insert('', 'end', values=item_values, tags=('row_font',))
    treeview3.tag_configure('row_font', font=("Helvetica", 12))

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

def remove_selected_items():
    global total_price
    selected_items = treeview2.selection()
    for item in selected_items:
        item_values = treeview2.item(item, 'values')
        price = int(item_values[2])
        total_price -= price
        treeview2.delete(item)
    update_total_label()

listofshops = ['Lidl', 'Aldi', 'Penny', 'Tesco', 'Auchan', 'Spar']
stickers = []
for i in range(6):
    sticker = customtkinter.CTkButton(f2, text=listofshops[i], width=70, height=70, fg_color="grey", hover_color="grey")
    sticker.grid(row=3, column=i, padx=5, pady=5)
    sticker.configure(command=lambda index=i: filter_with_sticker(index))
    stickers.append(sticker)
cart_label  = Buttons(f1, 'Kosár', 80, 50, ("Helvetica", 16), None, None, lambda: [copy_data_to_frame2(), raise_frame(f2)], 7, column=1, padx = 5, pady= 5)
delete_button = Buttons(f1, 'Törlés', 80, 50, ("Helvetica", 16), "#DB3E39", "#C4191C", remove_selected_items, 7, column=0, padx = 5, pady= 5)
put_label = Buttons(f1, 'Kosárba helyezés', 700, 50, ("Helvetica", 16), None, None, move_selected_items, 5, columnspan=3, padx = 5, pady= 5)
save_button = Buttons(f2, 'Mentés', 80, 50, ("Helvetica", 16),'black','black', save_to_excel_treeview3, 2, column=0, padx = (25,0), pady= 0)
back_button = Buttons(f2, 'Vissza', 80, 50, ("Helvetica", 16), None, None, lambda:raise_frame(f1), 6, columnspan=6, padx = (25,0), pady= 5)
save_button2 = Buttons(f2, 'Mentés', 80, 50, ("Helvetica", 16),'black','black', save_to_excel_treeview4, 6, column=0, padx = (25,0), pady= 0)