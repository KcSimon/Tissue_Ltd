from production import Product
from sales import Sales

import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))
conn = sqlite3.connect(path+'\product_data_main.db')
sql_queries = conn.cursor()

#insert_product = """ INSERT INTO products (sku, product, cost, productionDate) VALUES ( '%s', '%s', '%f', '%s')""" #%(var, var1, var2, var3)
#insert_sale = """ INSERT INTO sales (sku, amount, price) VALUES ( '%s', '%d', '%f')""" #%(var, var1, var2)
#select_product = """ SELECT sku, product, cost, productionDate FROM products"""
#select_a_product = """ SELECT sku, product, cost, productionDate FROM products WHERE sk = '%s'""" #%var
#select_sale = """ SELECT sku, amount, price FROM sales WHERE sku = '%s'""" #%var
select_product_sale = """ SELECT products.sku, product, cost, productionDate, sales.sku, amount, price FROM products LEFT JOIN sales ON products.sku = sales.sku ORDER BY products.sku ASC"""
#select_a_product_sale = """ SELECT products.sku, product, cost, productionDate, sales.sku, amount, price FROM products LEFT JOIN sales ON products.sku = sales.sku WHERE products.sku = '%s'""" #%var

sales = conn.execute(select_product_sale).fetchall()
product_sales = []
product_cost = []

for s in sales:
    product_sales.append(Sales(s[0], s[5], s[6]))
    product_cost.append(Product(s[0], s[5], s[2], s[3]))
    product_cost[-1].set_profit(product_sales[-1].sales_total)

print("Sku \tProduced Cost \tDate \t\tAmount \tPrice \tProduction Cost Product Sales \tTotal Sales \tProfit \t\tMargin")

for i, p in enumerate(product_cost):
    print("%s \t%.2f \t%.2f \t%s \t%.2f \t%.2f \t%.2f \t%.2f \t%.2f \t%.2f \t%f" %(p.sku, p.produced, p.cost, p.date, product_sales[i].amt, product_sales[i].price, p.production_cost, product_sales[i].sales, product_sales[i].sales_total, p.profit, p.margin))
    
    