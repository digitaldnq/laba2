import random

def rockScissorsPapper():
    choices = ['камень', 'ножницы', 'бумага']
    user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()

    while user_choice not in choices:
        print("Некорректный ввод, выберите камень, ножницы или бумага.")
        user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()

    computer_choice = random.choice(choices)
    print(f"Вы выбрали: {user_choice}\nКомпьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы выиграли.")
    else:
        print("Компьютер выиграл.")

rockScissorsPapper()
