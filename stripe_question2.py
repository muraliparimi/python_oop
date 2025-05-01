from collections import defaultdict
orders = {
    "country": "us",
    "items": [
        {"product": "mouse", "quantity": 20},
        {"product": "laptop", "quantity": 5}
    ]
}

shipping_costs = {
    "country": "us",
    "costs" : { "mouse":
        [
          { "min_quantity" : 0,
            "max_quantity" : None,
            "cost" : 750
            }
        ],
        "laptop":
        [
            {"min_quantity" : 0,
            "max_quantity" : 2,
            "cost" : 1100},
            
            {"min_quantity" : 3,
            "max_quantity" : 4,
            "cost" : 1000},
            
            {"min_quantity" : 4,
            "max_quantity" : None,
            "cost" : 900},
        ]
    }

}


# https://chatgpt.com/canvas/shared/68124130facc8191b643d980cf5f0a24

class ShippingCost:
    def __init__(self, orders, shipping_costs):
        self.orders = orders
        self.shipping_costs = shipping_costs
        self.shipping_cost_lookup = self.create_shipping_costs_lookup()

    def get_product_details(self):
        country = self.orders["country"]
        products = []
        for item_details in self.orders["items"]:
            product, quantity = item_details.values()
            products.append((product, quantity))
        return {country: products}
    
    def create_shipping_costs_lookup(self):
        country = self.shipping_costs["country"]
        shipping_cost_lookup = defaultdict(lambda: defaultdict(list))
        for product in self.shipping_costs["costs"]:
            shipping_cost_lookup[country][product] = self.shipping_costs["costs"][product]
        return shipping_cost_lookup

    
    def is_tiered_rating(self, country, product):
        # shipping_cost_lookup = self.create_shipping_costs_lookup()
        if country in self.shipping_cost_lookup and product in self.shipping_cost_lookup[country]:
            return True if len(self.shipping_cost_lookup[country][product])> 1 else False
        
    def get_tiered_brackets(self, country, product):
        res = []
        for costs in self.shipping_cost_lookup[country][product]:
            min_quantity, max_quantity, cost = costs.values()
            res.append((min_quantity, max_quantity, cost))
        return res

    def get_shipping_costs(self, country, product, quantity):
        sum = 0
        is_tiered_rating = self.is_tiered_rating(country, product)
        if not is_tiered_rating:
            sum += self.get_tiered_brackets(country, product)[0][2] * quantity
            return sum
        while quantity > 0:
            tiers = self.get_tiered_brackets(country, product)
            for tier in tiers:
                min_quantity, max_quantity, cost = tier
                if max_quantity:
                    if min_quantity == 0:
                        temp_quantity = max_quantity - min_quantity
                    else:
                        temp_quantity = max_quantity - min_quantity + 1
                    sum += temp_quantity * cost
                    quantity -= temp_quantity
                else:
                    # print(f"no max_quanity and remaining quantity for product:{product} is {quantity}")
                    sum += quantity * cost
                    quantity = 0
        return sum
    
    def total_shipping_cost(self):
        d = self.get_product_details()
        cost = 0
        for country, products in d.items():
            for product in products:
                cost += self.get_shipping_costs(country, product[0], product[1])
        return cost


if __name__ == '__main__':
    electronics = ShippingCost(orders, shipping_costs)
    print(electronics.total_shipping_cost())





