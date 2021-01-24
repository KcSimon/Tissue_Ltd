import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))
conn = sqlite3.connect(path+'\product_data_main.db')
sql_queries = conn.cursor()

insert_product = """ INSERT INTO products (sku, product, cost, productionDate) VALUES ( '%s', '%s', '%f', '%s')""" #%(var, var1, var2, var3)
insert_sale = """ INSERT INTO sales (sku, amount, price) VALUES ( '%s', '%d', '%f')""" #%(var, var1, var2)
select_product = """ SELECT sku, product, cost, productionDate FROM products"""
select_a_product = """ SELECT sku, product, cost, productionDate FROM products WHERE sk = '%s'""" #%var
select_sale = """ SELECT sku, amount, price FROM sales WHERE sk = '%s'""" #%var
select_product_sale = """ SELECT products.sku, product, cost, productionDate, sales.sku, amount, price FROM products LEFT JOIN sales ON products.sku = sales.sku ORDER BY products.sku ASC"""
select_a_product_sale = """ SELECT products.sku, product, cost, productionDate, sales.sku, amount, price FROM products LEFT JOIN sales ON products.sku = sales.sku WHERE products.sku = '%s'""" #%var
