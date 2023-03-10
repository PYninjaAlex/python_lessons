def menu(menu_: dict[list], allergy: str) -> dict:
    output_dict = {}
    for i in menu_:
        output_dict[i] = []
        for j in menu_[i]:
            if j == allergy:
                continue
            else:
                output_dict[i].append(j)
    return menu_


my_menu = {
    "понедельник": ["пюре", "котлета", "компот"],
    "вторник": ["пюре", "котлета", "компот"],
    "среда": ["пюре", "котлета", "компот"],
    "четверг": ["гречка", "котлета", "компот"],
    "пятница": ["пюре", "котлета", "компот"],
    "суббота": ["пюре", "котлета", "компот"],
    "восскресенье": ["пюре", "котлета", "компот"],

}

print(menu(my_menu, "пюре"))
