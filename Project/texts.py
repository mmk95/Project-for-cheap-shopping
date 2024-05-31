from frame import *

class Texts:
    def __init__(self, parent, text, text_color, font, row, column=None, columnspan=None, padx=5, pady=5):
        self.label = customtkinter.CTkLabel(parent, text=text, text_color=text_color, font=font)
        if columnspan is not None:
            self.label.grid(row=row, columnspan=columnspan, padx=padx, pady=pady)
        else:
            self.label.grid(row=row, column=column, padx=padx, pady=pady)
    
    def update_text(self, new_text):
        self.label.configure(text=new_text)

welcome_label = Texts(f1, 'Üdvözöljük!', "#003d61", ("Helvetica", 24), 0, columnspan=3, padx = 5, pady= 40)
text_label = Texts(f1, 'Adja meg az élelmiszer típust, aminek az árára kíváncsi.', "#003d61", ("Helvetica", 16), 1, columnspan=3, padx = 5, pady= 5)
text_label2 = Texts(f1, 'Kérem válassza ki azt a terméket, amit a kosárba helyezne.', "#003d61", ("Helvetica", 16), 3, columnspan=3, padx = 50, pady= 5)
price_label = Texts(f1, 'Végösszeg: ', "#003d61", ("Helvetica", 16), 7, column = 2, padx = 5, pady= 5)
secondTop_label = Texts(f2, 'Kosár', "#003d61", ("Helvetica", 16), 0, columnspan=6, padx = 5, pady= (10,15))
text_label3 = Texts(f2, 'Ha egy boltban szeretne vásárolni.', "#003d61", ("Helvetica", 16), 2, columnspan=6, padx = 5, pady= (5,15))
price_label1 = Texts(f2, 'Végösszeg: ', "#003d61", ("Helvetica", 16), 2, column = 5, padx = 5, pady= 5)
totalprice_label = Texts(f2, 'Végösszeg: ', "#003d61", ("Helvetica", 16), 6, column = 5, padx = 5, pady= 5)