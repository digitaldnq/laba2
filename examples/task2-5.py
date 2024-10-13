def my_generate(start=0, stop=5):
    number = start
    while number <= stop:
        yield number
        number += 1

ranger = my_generate(0)

for value in ranger:
    print(value)
