# Sample data
products = [
    {"name": "Orange Juice", "price": 3.5},
    {"name": "Milk", "price": 2.0},
    {"name": "Bread", "price": 1.5},
    {"name": "Apple", "price": 0.8},
    {"name": "Cheese", "price": 4.0}
]

orders = [
    {"customer": "Alice", "product": "Orange Juice", "quantity": 2},
    {"customer": "Bob", "product": "Bread", "quantity": 5},
    {"customer": "Charlie", "product": "Milk", "quantity": 1},
    {"customer": "Alice", "product": "Apple", "quantity": 10},
    {"customer": "Ethan", "product": "Cheese", "quantity": 3}
]

# 1: Total products sold
total_products_sold = sum(order["quantity"] for order in orders)

# 2: Most popular product
from collections import Counter
product_counts = Counter(order["product"] for order in orders)
most_popular = product_counts.most_common(1)[0][0]

# 3: Revenue /customer
revenue_per_customer = {}
for order in orders:
    revenue = next(p["price"] for p in products if p["name"] == order["product"]) * order["quantity"]
    revenue_per_customer[order["customer"]] = revenue_per_customer.get(order["customer"], 0) + revenue

# 4: Print 
print(f"Total Products Sold: {total_products_sold}")
print(f"Most Popular Product: {most_popular}")
print("Revenue per Customer:")
for customer, revenue in revenue_per_customer.items():
    print(f" - {customer}: ${revenue:.2f}")

import json
report = {
    "total_products_sold": total_products_sold,
    "most_popular_product": most_popular,
    "revenue_per_customer": revenue_per_customer
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=4)
