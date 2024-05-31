from frame import *
from texts import *
from buttons import *
from treeviews import *
from options import *


def delete_csv_file():
    csv_filename = "treeview_data.csv"
    if os.path.exists(csv_filename):
        os.remove(csv_filename)

def delete_xlsx_file():
    xlsx_filename = "shopping_list.xlsx"
    if os.path.exists(xlsx_filename):
        os.remove(xlsx_filename)


raise_frame(f1)
app.mainloop()
delete_csv_file()
delete_xlsx_file()
