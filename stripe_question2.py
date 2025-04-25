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