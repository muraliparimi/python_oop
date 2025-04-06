from functools import reduce
import json
from datetime import datetime

class SalesAggregator:
    def __init__(self):
        self.sales = {}

    def add_sale(self, sale_id: str, amount: float, date: str) -> None:
        self.sales[sale_id] = {"amount": amount, "date": date}
    
    def get_sale(self, sale_id: str) -> float | None:
        return self.sales.get(sale_id)

    def delete_sale(self, sale_id: str) -> bool:
        if sale_id in self.sales:
            del self.sales[sale_id]
            return True
        return False
    
    def aggregate_sales(self, min_amount: float = 0) -> dict[str, int | float]:
        total_amount = reduce(lambda x, y: x + y["amount"] if y["amount"] > min_amount else 0, self.sales.values(), 0)
        return {
            "total_sales": len(self.sales),
            "total_amount": total_amount
        }
    
    def format_sales(self, min_amount: float = 0) -> str:
        filtered_sales = [sale for sale in self.sales.items() if sale[1]["amount"] > min_amount]
        statistics = self.aggregate_sales(min_amount)

        result = {
        "sales": [{"sale_id": sale_id, "amount": sale["amount"], "date": sale["date"]} for sale_id, sale in filtered_sales],
        "statistics": statistics
    }
        return json.dumps(result)

    def get_sales_in_date_range(self, start_date: str, end_date: str) -> list[dict]:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        return [{"sale_id": sale_id, "amount": sale["amount"], "date": sale["date"]} for sale_id, sale in self.sales.items() if
                (start_date <= datetime.strptime(sale["date"], '%Y-%m-%d') <= end_date)
                ]
        


if __name__ == '__main__':
    aggregator = SalesAggregator()

    # Add sales with date
    aggregator.add_sale('001', 100.50, '2023-01-01')
    aggregator.add_sale('002', 200.75, '2023-01-15')
    
    # Aggregate sales
    print(aggregator.aggregate_sales(min_amount=50)) 
    # Output: {'total_sales': 2, 'total_amount': 301.25}
    print(aggregator.format_sales(min_amount=50))
    print(aggregator.get_sales_in_date_range('2023-01-01', '2023-01-14'))