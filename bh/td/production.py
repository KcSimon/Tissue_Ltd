import datetime

class Product:
    
    total_produced = 0.0
    total_production_cost = 0.0
    
    def __init__(self, sku, produced, cost, date):
        self.sku = sku
        self.produced = produced
        self.cost = cost
        self.date = date
        self.profit = 0
        self.margin = 0
        self.production_cost = self.produced * self.cost
        Product.total_produced += produced
        Product.total_production_cost += produced * cost
        
    def set_profit(self, sales):
        self.profit = sales - self.cost
        self.set_margin
        
    def set_margin():
        self.margin = self.profit / (self.profit * 100)