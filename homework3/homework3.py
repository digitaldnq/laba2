from datetime import datetime

def calculate_age():
    while True:
        birth_date_str = input("Введите вашу дату рождения (день/месяц/год): ")

        parts = birth_date_str.split('/')

        if len(parts) != 3:
            print("Используйте верный формат день/месяц/год (например - 25/12/1990).")
            continue

        if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
            print("Используйте целочисленные числа.")
            continue

        day, month, year = map(int, parts)

        try:
            birth_date = datetime(year, month, day)
        except ValueError:
            print("Введена некорректная дата, убедитесь, что день, месяц и год существуют.")
            continue

        today = datetime.today()

        if birth_date > today:
            print("Вы не могли родиться в будущем")
            continue

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        print(f"Ваш возраст: {age} лет")
        break

calculate_age()
