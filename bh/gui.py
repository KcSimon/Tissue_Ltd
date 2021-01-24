import random
import datetime
from functools import partial
import tkinter as tk
from tkinter import ttk
import dbconn

revenue = {"sku": None, "product_name": None, "cost": 0, "sales" : 0, "profit" : 0, "margin" : 0}

window = tk.Tk()
window.grid_columnconfigure((0, 1, 3), weight=6)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.geometry("575x276")
window.title("Gross Profit Calculator")

frame = tk.Frame(window, width=555, height=250)
frame.grid(row=0, column=0, sticky="nswe")
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.grid_propagate(False)

canvas = tk.Canvas(frame, borderwidth=0, width=550, height=240)
canvas.grid(row=0, column=0, sticky="nswe")
canvas.rowconfigure(0, weight=1)
canvas.columnconfigure(0, weight=1)

'''scroll = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll.grid(sticky=tk.N+tk.S, row=0, column=8)
canvas.config(yscrollcommand=scroll.set)'''

tab_control = ttk.Notebook(canvas)

tab1 = tk.Frame(tab_control) #product
tab2 = tk.Frame(tab_control) #production
tab3 = tk.Frame(tab_control) #sales
tab4 = tk.Frame(tab_control) #gross profit
tab5 = tk.Frame(tab_control) #product list

tab_control.add(tab5, text="Product List")
#tab_control.add(tab1, text="Add Product")
tab_control.add(tab2, text="Add Production Figure")
tab_control.add(tab3, text="Add Sale")
tab_control.add(tab4, text="Gross Profit")

tab_control.grid(column=0, row=0)
tab_control.columnconfigure(0, weight=1)
tab_control.rowconfigure(0, weight=1)

sku_val = tk.StringVar()
product_name_val = tk.StringVar()
cost_val = tk.StringVar()
sales_val = tk.StringVar()
profit_val = tk.StringVar()
margin_val = tk.StringVar()

# Product List

def calculate_profits():
    revenue["profit"] = revenue["sales"] - revenue["cost"]
    revenue["margin"] = revenue["profit"] / (revenue["profit"] * 100) 

def calculate_totals(product):
    for t in product:
        revenue["sales"] = revenue["sales"] + (t[5] * t[6])
        revenue["cost"] = revenue["cost"] + (t[2] * t[6])
        
def get_gross_profit(index):
    tab_control.select(tab4)
    
def index(i):
    product = dbconn.conn.execute(dbconn.select_a_product_sale%i).fetchall()
    revenue["sku"] = product[0][0]
    revenue["product_name"] = product[0][1]
    calculate_totals(product)
    calculate_profits()
    sku_val.set(revenue["sku"])
    product_name_val.set(revenue["product_name"])
    cost_val.set((revenue["cost"]))
    sales_val.set((revenue["sales"]))
    profit_val.set((revenue["profit"]))
    margin_val.set((revenue["margin"]))
    window.update_idletasks()
    get_gross_profit(i)
    
products = dbconn.conn.execute(dbconn.select_product_sale).fetchall()

tk.Label(tab5, text="SKU").grid(row=0, column=0, padx=8)
tk.Label(tab5, text="Product").grid(row=0, column=1, padx=8)
tk.Label(tab5, text="Cost").grid(row=0, column=2, padx=8)
tk.Label(tab5, text="Date Produced").grid(row=0, column=3, padx=8)
tk.Label(tab5, text="Price").grid(row=0, column=4, padx=8)
tk.Label(tab5, text="Amount Sold").grid(row=0, column=5, padx=8)

for i, p in enumerate(products, start=0):
    tk.Label(tab5, text=p[0]).grid(row=i+1, column=0, padx=8),
    tk.Label(tab5, text=p[1]).grid(row=i+1, column=1, padx=8),
    tk.Label(tab5, text=p[2]).grid(row=i+1, column=2, padx=8),
    tk.Label(tab5, text=p[3]).grid(row=i+1, column=3, padx=8),
    tk.Label(tab5, text=p[6]).grid(row=i+1, column=4, padx=8),
    tk.Label(tab5, text=p[5]).grid(row=i+1, column=5, padx=8),
    tk.Button(tab5, text="Gross Sales", command=partial(index, p[0])).grid(row=i+1, column=6, padx=7)

#clear_prod_button.bind('<Button-1>', get_gross_profit)

# Add Product

'''data_input_label = tk.Label(tab1, text="Enter product information")
data_input_label.grid(column=0, row=1, padx=8, columnspan=4)

prod_SKU_label = tk.Label(tab1, text="Product SKU")
prod_SKU_label.grid(column=0, row=2, padx=8)
prod_SKU_input = tk.Entry(tab1, width=64)
prod_SKU_input.grid(column=1, row=2, padx=8, pady=8, columnspan=3)

prod_name_label = tk.Label(tab1, text="Product Name")
prod_name_label.grid(column=0, row=3, padx=8)
prod_name_input = tk.Entry(tab1, width=64)
prod_name_input.grid(column=1, row=3, padx=8, pady=8, columnspan=3)

blank1_label = tk.Label(tab1, text=" ")
blank1_label.grid(column=0, row=4, padx=8, pady=8)
blank2_label = tk.Label(tab1, text=" ")
blank2_label.grid(column=0, row=5, padx=8, pady=8)

clear_prod_button = tk.Button(tab1, text="Clear")
clear_prod_button.grid(column=2, row=6, rowspan=1, padx=8, sticky=tk.W)

save_prod_button = tk.Button(tab1, text="Save")
save_prod_button.grid(column=2, row=6, rowspan=1, padx=8, sticky=tk.E)

def clear_input(event):
    prod_SKU_input.delete(0, tk.END)
    prod_name_input.delete(0, tk.END)

def save_prod(event):
    conn.execute(insert_product+(prod_SKU_input.get(), prod_name_input.get(), )
    print("Saved")

clear_prod_button.bind('<Button-1>', clear_input)
save_prod_button.bind('<Button-1>', save_prod)'''

# Add Production Figure

data_input_label = tk.Label(tab2, text="Enter production information")
data_input_label.grid(column=0, row=1, padx=8, columnspan=4)

sku_label = tk.Label(tab2, text="SKU")
sku_label.grid(column=0, row=2, padx=8)
sku_input = tk.Entry(tab2, width=64)
sku_input.grid(column=1, row=2, padx=8, pady=8, columnspan=3)

produced_label = tk.Label(tab2, text="Produced")
produced_label.grid(column=0, row=3, padx=8)
produced_input = tk.Entry(tab2, width=64)
produced_input.grid(column=1, row=3, padx=8, pady=8, columnspan=3)

cost_label = tk.Label(tab2, text="Cost")
cost_label.grid(column=0, row=4, padx=8)
cost_input = tk.Entry(tab2, width=64)
cost_input.grid(column=1, row=4, padx=8, pady=8, columnspan=3)

date_label = tk.Label(tab2, text="Date Produced")
date_label.grid(column=0, row=5, padx=8)
date_input = tk.Entry(tab2, width=64)
date_input.grid(column=1, row=5, padx=8, pady=8, columnspan=3)

clear_produced_button = tk.Button(tab2, text="Clear")
clear_produced_button.grid(column=2, row=6, rowspan=1, padx=8, sticky=tk.W)

save_produced_button = tk.Button(tab2, text="Save")
save_produced_button.grid(column=2, row=6, rowspan=1, padx=8, sticky=tk.E)

def clear_input(event):
    sku_input.delete(0, tk.END)
    produced_input.delete(0, tk.END)
    cost_input.delete(0, tk.END)
    date_input.delete(0, tk.END)

def save_prod(event):
    dbconn.conn.execute(dbconn.insert_product%(sku_input.get(), produced_input.get(), float(cost_input.get()), date_input.get()))
    dbconn.conn.commit()

clear_produced_button.bind('<Button-1>', clear_input)
save_produced_button.bind('<Button-1>', save_prod)

# Add Sale

data_input_label = tk.Label(tab3, text="Enter sales information")
data_input_label.grid(column=0, row=1, padx=8, columnspan=4)

sales_sku_label = tk.Label(tab3, text="SKU")
sales_sku_label.grid(column=0, row=2, padx=8)
sales_sku_input = tk.Entry(tab3, width=64)
sales_sku_input.grid(column=1, row=2, padx=8, pady=8, columnspan=3)

amount_label = tk.Label(tab3, text="Amount")
amount_label.grid(column=0, row=3, padx=8)
amount_input = tk.Entry(tab3, width=64)
amount_input.grid(column=1, row=3, padx=8, pady=8, columnspan=3)

price_label = tk.Label(tab3, text="Price")
price_label.grid(column=0, row=4, padx=8)
price_input = tk.Entry(tab3, width=64)
price_input.grid(column=1, row=4, padx=8, pady=8, columnspan=3)

blank3_label = tk.Label(tab3, text=" ")
blank3_label.grid(column=0, row=5, padx=8, pady=8)

clear_sales_button = tk.Button(tab3, text="Clear")
clear_sales_button.grid(column=2, row=6, rowspan=1, padx=8, sticky=tk.W)

save_sales_button = tk.Button(tab3, text="Save")
save_sales_button.grid(column=2, row=6, rowspan=1, padx=8, sticky=tk.E)

def clear_input(event):
    sales_sku_input.delete(0, tk.END)
    amount_input.delete(0, tk.END)
    price_input.delete(0, tk.END)

def add_sale(event):
    dbconn.conn.execute(dbconn.insert_sale%(sales_sku_input.get(), int(amount_input.get()), float(price_input.get())))
    dbconn.conn.commit()

clear_sales_button.bind('<Button-1>', clear_input)
save_sales_button.bind('<Button-1>', add_sale)

# Gross Profit

profit_label = tk.Label(tab4, text="Gross Profit")

profit_sku_label = tk.Label(tab4, text="SKU")
profit_sku_label.grid(column=0, row=1, padx=8, pady=8)

profit_sku_data_label = tk.Label(tab4, textvariable=sku_val)
profit_sku_data_label.grid(column=1, row=1, padx=8, pady=8, columnspan=3)

profit_name_label = tk.Label(tab4, text="Product Name")
profit_name_label.grid(column=0, row=2, padx=8, pady=8)

profit_name_data_label = tk.Label(tab4, textvariable=product_name_val)
profit_name_data_label.grid(column=1, row=2, padx=8, pady=8, columnspan=3)

profit_cost_label = tk.Label(tab4, text="Gross Cost")
profit_cost_label.grid(column=0, row=3, padx=8, pady=8)

profit_cost_data_label = tk.Label(tab4, textvariable=cost_val)
profit_cost_data_label.grid(column=1, row=3, padx=8, pady=8, columnspan=3)

profit_sales_label = tk.Label(tab4, text="Gross Sales")
profit_sales_label.grid(column=0, row=4, padx=8, pady=8)

profit_sales_data_label = tk.Label(tab4, textvariable=sales_val)
profit_sales_data_label.grid(column=1, row=4, padx=8, pady=8, columnspan=3)

profit_income_label = tk.Label(tab4, text="Gross Profit")
profit_income_label.grid(column=0, row=5, padx=8, pady=8)

profit_income_data_label = tk.Label(tab4, textvariable=profit_val)
profit_income_data_label.grid(column=1, row=5, padx=8, pady=8, columnspan=3)

profit_margin_label = tk.Label(tab4, text="Profit Margin")
profit_margin_label.grid(column=0, row=6, padx=8, pady=8)

profit_margin_data_label = tk.Label(tab4, textvariable=margin_val)
profit_margin_data_label.grid(column=1, row=6, padx=8, pady=8, columnspan=3)

def on_closing():
    dbconn.conn.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()