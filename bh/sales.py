class Sales:

    total_sales = 0
    
    def __init__(self,  sku, amt, price):
        self.sku = sku
        self.amt = amt
        self.price = price
        total_sales += self.amt * self.price
        
    def total_sales():
        return self.amt * self.price