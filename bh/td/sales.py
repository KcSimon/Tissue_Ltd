class Sales:

    sales_total = 0.0
    
    def __init__(self, sku, amt, price):
        self.sku = sku
        self.amt = amt
        self.price = price
        self.sales = self.amt * self.price
        Sales.sales_total += self.amt * self.price
        