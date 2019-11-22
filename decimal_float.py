import decimal from Decimal

product_cost = decimal(88.40)
commission_rate = decimal(0.08)
qty = 450


product_cost += (commission_rate * product_cost)
print(product_cost * qty)