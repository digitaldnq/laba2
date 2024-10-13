import random

def find_multiples():
    while True:
        try:
            x = int(input("Введите число X: "))
            break
        except ValueError:
            print("Некорректный ввод, необходимо ввести целое число.")

    random_numbers = [random.randint(0, 200) for _ in range(10)]

    multiples = list(filter(lambda num: num % x == 0, random_numbers))

    print(f"Сгенерированный список чисел: {random_numbers}")
    print(f"Числа, кратные {x}: {multiples}")

find_multiples()
