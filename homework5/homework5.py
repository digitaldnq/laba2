def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

generator = get_number()

first_value = None
fifth_value = None
last_value = None

for i, value in enumerate(generator, start=1):
    if i == 1:
        first_value = value
    if i == 5:
        fifth_value = value
    last_value = value  

print(f"Первое значение: {first_value}")
print(f"Пятое значение: {fifth_value}")
print(f"Последнее значение: {last_value}")
