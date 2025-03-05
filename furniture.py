item = "Tv stand"
retail_price = 325.00
wholesale_price = 200.00
profit = retail_price - wholesale_price
sale_price = retail_price * 0.75
sale_profit = sale_price - wholesale_price
print("Item name:", item)
print("Retail Price: $", format(retail_price, '.2f'), sep='')
print("Wholesale Price: $", format(wholesale_price, '.2f'), sep='')
print("Profit: $", format(profit, '.2f'), sep='')
print("Sale Price: $", format(sale_price, '.2f'), sep='')
print("Sale Profit: $", format(sale_profit, '.2f'), sep='')
