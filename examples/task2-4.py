def dog_list(types, func):
    for dogs in types:
        print(func(dogs))

types = ['Немецкая овчарка','Спаниель','Мопс']

dog_list(types, lambda dogs: dogs.lower() + ' - собака')
