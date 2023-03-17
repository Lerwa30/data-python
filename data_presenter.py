orders = open('CupcakeInvoices.csv')

# for item in orders:
#     # print(item)
#     item = item.strip()
#     type = item.split(",")
#     print(type[2])

# for item in orders:
#     item = item.split(',')
#     total = int(item[3]) * float(item[4])
#     new_total = round(total, 2)
#     print(new_total)

total = 0
for item in orders:
    item = item.split(',')
    total = total + int(item[3]) * float(item[4])
    new_total = round(total, 2)
print(new_total)

orders.close()