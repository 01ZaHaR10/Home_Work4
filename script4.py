inventory = dict()
max_weight = 500
weight = 0

while True:
    choice = input("Хотите добавить предмет в инвентарь?\n ")
    if choice.lower() == "нет" or choice.lower() == "no":
        choice = input("Хотите удалить предмет из инвентаря?\n ")
        if choice.lower() == "нет" or choice.lower() == "no":
            choice = input("Хотите просмотреть содержимое инвентаря?\n ")
            if choice.lower() == "да" or choice.lower() == "yes":
                if len(inventory) == 0:
                    print("Инвентарь пуст.")
                else:
                    print("Содержимое: ")
                    for i in inventory.keys():
                        print(f"Предмет - {i} : вес - {inventory[i]}")
                    print(f"Общий вес: {weight}")
            elif choice.lower() == "нет" or choice.lower() == "no":
                break
            else:
                print("Некорректный ответ.")
        elif choice.lower() == "да" or choice.lower() == "yes":
            lst = input("Введите название предмета: ")
            if lst.lower() in inventory:
                weight -= inventory.pop(lst.lower())
            else:
                print("Такого предмета нет в инвентаре!")
        else:
            print("Некорректный ответ.")
    elif choice.lower() == "да" or choice.lower() == "yes":
        lst = list(input("Введите предмет и его вес через пробел: ").split())
        if lst[0].lower() in inventory:
            print("Такой предмет уже есть!")
        elif weight + int(lst[1]) > max_weight:
            print("Не хватает места!")
        elif weight + int(lst[1]) == max_weight:
            inventory[lst[0].lower()] = int(lst[1])
            weight += int(lst[1])
            print("Инвентарь полон.\n")
            print("Содержимое: ")
            for i in inventory.keys():
                print(f"Предмет - {i} : вес - {inventory[i]}")
            print(f"Общий вес: {weight}")
            break
        else:
            inventory[lst[0].lower()] = int(lst[1])
            weight += int(lst[1])
    else:
        print("Некорректный ответ.")
    print()