#shopping cart project
#beginner project to practice my understanding of python datatypes and vaiables
# I imported decimal point  to avoid floating point errors in money calculations
from decimal import Decimal
# my shopping cart is a LIST of DICTIONARIES
# Each dictionary represents ONE item in the cart
cart=[
    {"sku": "A001", "name": "T-shirt", "qty": 2, "price": Decimal("14.99")},
    {"sku": "B205", "name": "Mug", "qty":1, "price": Decimal("6.50")},
    {"sku": "C301", "name": "Notebook", "qty": 3, "price": Decimal("2.25")},
    {"sku": "D099", "name": "Pen", "qty": 5, "price": Decimal("0.99")},
]
#print a header for our mini receipt
print("===Shopping cart===")
# Loop through each item in the cart and print details
for item in cart:
    # Calculate total cost for this item (price * qty)
    line_total=item["price"] * item["qty"]
    print(f"{item['qty']} * {item['name']} @ {item['price']} each= {line_total}")
    # Calculate the grand total for all items
    total= sum(item["price"] * item["qty"] for item in cart)
print("=======================")
print(f"TOTAL: KES {total}")

