def outer2(out_param):
    def inner2():
        return f'Моего мопса зовут: {out_param}'
    return inner2

value = outer2('Лолита')
print(value())
