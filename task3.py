original_list = []
while True:
    key = input("Введіть ключ ('все' для завершення): ")
    if key == 'все':
        break
    value = int(input("Введіть значення: "))
    original_list.append((key, value))

grouped_dict = {}

for key, value in original_list:
    if key in grouped_dict:
        grouped_dict[key].append(value)
    else:
        grouped_dict[key] = [value]

print("Групування послідовності кортежів ключ-значення в словник списків:")
print(grouped_dict)