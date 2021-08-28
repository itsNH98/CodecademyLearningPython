# Start coding below!
daily_sales_replaced = daily_sales.replace(';,;',';')
# print(daily_sales_replaced)

daily_transactions = daily_sales_replaced.split(',')
# print(daily_transactions)

daily_transactions_split = []
for transaction in daily_transactions:
  daily_transactions_split.append(transaction.split(';'))

# print(daily_transactions_split)

transactions_clean = []
for daily_transactions in daily_transactions_split:
  transaction_clean = []
  for transaction in daily_transactions:
    transaction_clean.append(transaction.strip('\n').strip())
  transactions_clean.append(transaction_clean)

customers = []
sales = []
thread_sold = []

for transaction in transactions_clean:
  customers.append(transaction[0])
  sales.append(transaction[1])
  thread_sold.append(transaction[2])

total_sales = 0

for sale in sales:
  total_sales += float(sale.strip('$'))
print(total_sales)

print(thread_sold)

thread_sold_split = []

for item in thread_sold:
  for color in item.split('&'):
    thread_sold_split.append(color)
#print(thread_sold_split)

def color_count(color):
  color_count = 0
  for item in thread_sold_split:
    if color == item:
      color_count += 1
  return color_count
#print(color_count('white'))

colors = ['red','yellow','green','white','black','blue','purple']

for color in colors:
  print("Thread Shed sold {0} threads of {1} thread today.".format(color_count(color), color))