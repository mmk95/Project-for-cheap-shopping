from tkinter import ttk
from frame import *

class TreeFrame(ttk.Frame):
    def __init__(self, parent, row, columnspan, padx, pady, **kwargs):
        super().__init__(parent, **kwargs)
        self.grid(row=row, columnspan=columnspan, padx=padx,  pady=pady)

class TreeScrollbar(ttk.Scrollbar):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack(side="right", fill="y")

tree_cols = ("Termék neve", "Bolt", "Ár(Ft)")
columns = ["Termék neve", "Bolt", "Ár(Ft)"]
widths = [270, 270, 270]

treeFrame = TreeFrame(f1, 4, 3, None, 10)
treeScroll = TreeScrollbar(treeFrame)
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set,style="Treeview", columns=tree_cols, height=10)
for column, width in zip(columns, widths):
    treeview.column(column, width=width)
treeview.pack()
treeScroll.config(command=treeview.yview)

treeFrame2 = TreeFrame(f1, 6, 3, 5, (5,10))
treeScroll2 = TreeScrollbar(treeFrame2)
treeview2 = ttk.Treeview(treeFrame2, show="headings",
                        yscrollcommand=treeScroll2.set, columns=tree_cols, height=10)
for tree_col in tree_cols:
    treeview2.heading(tree_col, text=tree_col)
for column, width in zip(columns, widths):
    treeview2.column(column, width=width)
treeview2.pack()
treeScroll2.config(command=treeview2.yview)

treeFrame3 = TreeFrame(f2, 1, 6, 5, (5,15))
treeScroll3 = TreeScrollbar(treeFrame3)
treeview3 = ttk.Treeview(treeFrame3, show="headings",
                        yscrollcommand=treeScroll3.set, columns=tree_cols, height=11)
for tree_col in tree_cols:
    treeview3.heading(tree_col, text=tree_col)
for column, width in zip(columns, widths):
    treeview3.column(column, width=width)
treeview3.pack()
treeScroll3.config(command=treeview3.yview)

treeFrame4 = TreeFrame(f2, 5, 6, 35, (15,15))
treeScroll4 = TreeScrollbar(treeFrame4)
treeview4 = ttk.Treeview(treeFrame4, show="headings",
                        yscrollcommand=treeScroll4.set, columns=tree_cols, height=11)
for tree_col in tree_cols:
    treeview4.heading(tree_col, text=tree_col)
for column, width in zip(columns, widths):
    treeview4.column(column, width=width)
treeview4.pack()
treeScroll4.config(command=treeview4.yview)