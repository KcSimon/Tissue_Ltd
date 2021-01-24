import datetime

class Production:
    
    total_produced = 0
    total_production_cost = 0
    
    def __init__(self, sku, produced, cost, date):
        self.sku = sku
        self.produced = produced
        self.cost = cost
        self.date = date
        total_produced += produced
        total_production_cost += produced * cost
        
    def production_cost():
        return self.produced * self.cost