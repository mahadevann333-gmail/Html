# Store product prices
rice_price = 45
sugar_price = 40
oil_price = 130

# Store product quantities
rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

# Calculate price and quantities
rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

# print item price
print("rice_total:",rice_total)
print("sugar_total:",sugar_total)
print("oil_total:",oil_total)

# Calculate total bill
total_bill = rice_total + sugar_total + oil_total

print("Total bill:",total_bill)

# Convert total bill to integer
print("Total bill as integer:", int(total_bill))

# Convert total bill to string
print("Total bill as string:", str(total_bill))

# Generate random delivery charge
import random
delivery_charge = random.randint(5, 10)

# Calculate final bill
final_bill = total_bill + delivery_charge

print("Delivery charge:", delivery_charge)
print("Final bill including delivery:", final_bill)
