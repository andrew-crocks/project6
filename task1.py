data = []

while True:
    item = input("Введіть назву елементу (або введіть 'кінець', щоб завершити ввід): ")
    if item == 'кінець':
        break

    amount = int(input("Введіть кількість для елементу '{}': ".format(item)))

    data.append({'item': item, 'amount': amount})

result = {}

for d in data:
    if d['item'] in result:
        result[d['item']] += d['amount']
    else:
        result[d['item']] = d['amount']

print(result)