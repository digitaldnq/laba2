def outer(vnesh_param1, vnesh_param2):
    def inner(vnutr_param1, vnutr_param2):
        return vnutr_param1 + vnutr_param2
    return inner(vnesh_param1, vnesh_param2)

print(outer("Моего мопса зовут: ", "Лолита"))
