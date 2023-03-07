def list_functions():

    # Добавление одного элемента в конец списка
    def add_one(list_: list, value):
        print(f"Добавление элемента {value} в конец списка {list_}")
        list_.append(value)
        print(f"Результат: {list_}\n")

    # Удаление одного элемента по заданому индексу
    def remove_element(list_: list, index: int):
        print(f"Удаление элемента из списка {list_} по индексу ({index})")

        if index > len(list_)-1:
            print(f"Индекс ({index}) выходит за рамки списка\n")
            return

        list_.pop(index)
        print(f"Результат: {list_}\n")

    # Удаление одного элемента в конце списка
    def remove_last_element(list_: list):
        print(f"Удаление последнего элемента из списка {list_}")
        list_.pop()
        print(f"Результат: {list_}\n")

    # Срез списка начиная с (х) заканчивая (у)
    def slice_list(list_: list, x: int, y: int):
        print(f"Срез с ({x}) элемента по ({y}) элемент списка {list_}")
        result = list_[slice(x, y)]
        print(f"Результат: {result}\n")
        return result

    # Срез списка начиная с (х) заканчивая (у) с шагом в (s)
    def slice_step_list(list_: list, x: int, y: int, s: int):
        print(f"Срез с ({x}) элемента по ({y}) элемент с шагом в ({s}) списка {list_}")
        result = list_[slice(x, y, s)]
        print(f"Результат: {result}\n")
        return result

    # Объединение элементов двух списков в один
    def combine_two(list_1: list, list_2: list):
        print(f"Добавляем к списку {list_1} элементы списка {list_2}")
        list_1.extend(list_2)
        print(f"Результат: {list_1}\n")

    # Пересечение двух списков
    def list_intersection(list_1: list, list_2: list):
        print(f"Пересечение списка {list_1} и {list_2}")
        result = list()

        for l1 in list_1:
            if l1 in result:
                continue

            for l2 in list_2:
                if l1 == l2:
                    result.append(l2)

        print(f"Результат: {result}\n")
        return result

    # Сортировка списка по ключу (k/key) и параметру (rev/reverse)
    def sort_list(list_: list, k, rev: bool):
        print(f"Сортировка списка {list_} с ключом ({k}), значение reverse: {rev}")
        list_.sort(key=k, reverse=rev)
        print(f"Результат: {list_}\n")

    # Проверка наличия значения в списке
    def find(list_: list, value):
        print(f"Проверка наличия значения ({value}) в списке {list_}")

        for item in list_:
            try:
                if item == value:
                    print(f"Элемент ({value}) найден по индексу {list_.index(value)}\n")
                    return True
            except StopIteration:
                break

        print(f"Указанный элемент не найден в списке\n")

    a = [1, 2, 3, 4, 5]
    b = [1, 5, 4]

    c = ['H', 'e', 'l', 'l', 'o']
    d = ['W', 'o', 'r', 'l', 'd']

    print("List")
    print("=====================================")

    add_one(a, 6)

    remove_element(b, 1)

    remove_last_element(a)

    slice_list(a, 1, 4)

    slice_step_list(a, 1, 4, 2)

    combine_two(c, d)

    sort_list(list_intersection(c, d), None, rev=False)

    if find(c, "W"):
        print("Проверка выполнена успешно\n")


def dict_functions():

    # Добавление одного элемента в конец словаря
    def add_one(dict_: dict, value):
        print(f"Добавление элемента {value} в конец словаря {dict_}")
        dict_.update(value)
        print(f"Результат: {dict_}\n")

    # Удаление одного элемента по заданому ключу
    def remove_element(dict_: dict, key):
        print(f"Удаление элемента из словаря {dict_} по ключу ({key})")

        if key not in dict_:
            print(f"Ключ ({key}) не существует в словаре\n")
            return

        dict_.pop(key)
        print(f"Результат: {dict_}\n")

    # Удаление одного элемента в конце словаря
    def remove_last_element(dict_: dict):
        print(f"Удаление последнего элемента из словаря {dict_}")
        dict_.popitem()
        print(f"Результат: {dict_}\n")

    # Срез словаря начиная с (х) ключа заканчивая (у) ключом
    def slice_dict(dict_: dict, x: int, y: int):
        print(f"Срез с ({x}) ключа по ({y}) ключ словаря {dict_}")
        result = dict(list(dict_.items())[x:y])
        print(f"Результат: {result}\n")
        return result

    # Срез списка начиная с (х) ключа заканчивая (у) ключом с шагом в (s)
    def slice_step_dict(dict_: dict, x: int, y: int, s: int):
        print(f"Срез с ({x}) ключа по ({y}) ключ с шагом в ({s}) словаря {dict_}")
        result = dict(list(dict_.items())[x:y:s])
        print(f"Результат: {result}\n")
        return result

    # Объединение элементов двух словарей в один
    def combine_two(dict_1: dict, dict_2: dict):
        print(f"Добавляем к словарю {dict_1} элементы словаря {dict_2}")
        dict_1.update(dict_2)
        print(f"Результат: {dict_1}\n")

    # Пересечение двух списков
    def dict_intersection(dict_1: dict, dict_2: dict):
        print(f"Пересечение словаря {dict_1} и {dict_2}")
        result = dict()

        for d1 in dict_1.keys():
            if d1 in result:
                continue

            for d2 in dict_2.keys():
                if d1 == d2:
                    result.update({d2: dict_2[d2]})

        print(f"Результат: {result}\n")
        return result

    # Сортировка словаря по ключу (k/key) и параметру (rev/reverse)
    def sort_dict(dict_: dict, k, rev: bool):
        print(f"Сортировка списка {dict_} с ключом ({k}), значение reverse: {rev}")
        result = sorted(dict_.items(), key=k, reverse=rev)
        print(f"Результат: {result}\n")

        return result

    # Проверка наличия ключа в словаре
    def find_key(dict_: dict, value):
        print(f"Проверка наличия ключа ({value}) в словаре {dict_}")

        for key in dict_.keys():
            try:
                if key == value:
                    print(f"Ключ ({value}) существует в словаре\n")
                    return True
            except StopIteration:
                break

        print(f"Указанный ключ не найден в словаре\n")

    # Проверка наличия значения в словаре
    def find_value(dict_: dict, value):
        print(f"Проверка наличия значения ({value}) в словаре {dict_}")

        for val in dict_.values():
            try:
                if val == value:
                    print(f"Значение ({value}) существует в словаре\n")
                    return True
            except StopIteration:
                break

        print(f"Указанное значение не найдено в словаре\n")

    a = {1: "Tom", 2: "Bill", 3: "Sam", 4: "Alice", 5: "Kate"}
    b = {1: "Thomas", 5: "Bob", 4: "Lina"}

    c = {1: 'H', 2: 'i'}
    d = {4: 'o', 7: 'l', 5: 'r', 3: 'W', 8: 'd'}
    f = {4: 'o', 3: 'W', 7: 'l'}

    print("Dictionary")
    print("=====================================")

    add_one(a, {6: "Jane"})

    remove_element(b, 4)

    remove_last_element(a)

    slice_dict(a, 1, 4)

    slice_step_dict(a, 1, 4, 2)

    combine_two(c, d)

    intersection = dict_intersection(c, f)

    sort_dict(intersection, None, rev=False)

    find_key(d, 6)
    find_value(a, "Sam")


def set_functions():
    # Добавление одного элемента в конец множества
    def add_one(set_: set, value):
        print(f"Добавление элемента {value} в конец множества {set_}")
        set_.add(value)
        print(f"Результат: {set_}\n")

    # Удаление одного заданого элемента
    def remove_element(set_: set, value):
        print(f"Удаление элемента ({value}) из множества {set_}")

        for val in set_:
            if val == value:
                set_.remove(value)
                print(f"Результат: {set_}\n")
                return

        print(f"Элемент со значением {value} не найден во множестве\n")

    # Удаление одного элемента в конце множества
    def remove_last_element(set_: set):
        print(f"Удаление последнего элемента во множестве {set_}")
        set_.remove(max(set_))
        print(f"Результат: {set_}\n")

    # Срез множества начиная с (х) заканчивая (у)
    def slice_set(set_: set, x: int, y: int):
        print(f"Срез с ({x}) элемента по ({y}) элемент множества {set_}")
        result = set(list(set_)[slice(x, y)])
        print(f"Результат: {result}\n")
        return result

    # Срез множества начиная с (х) заканчивая (у) с шагом в (s)
    def slice_step_set(set_: set, x: int, y: int, s: int):
        print(f"Срез с ({x}) элемента по ({y}) элемент с шагом в ({s}) множества {set_}")
        result = set(list(set_)[slice(x, y, s)])
        print(f"Результат: {result}\n")
        return result

    # Объединение элементов двух множеств в один
    def combine_two(set_1: set, set_2: set):
        print(f"Добавляем к множеству {set_1} элементы множества {set_2}")
        set_1 = set_1.union(set_2)
        print(f"Результат: {set_1}\n")

    # Пересечение двух множеств
    def set_intersection(set_1: set, set_2: set):
        print(f"Пересечение множества {set_1} и {set_2}")
        result = set_1.intersection(set_2)

        print(f"Результат: {result}\n")
        return result

    # Сортировка множества по ключу (k/key) и параметру (rev/reverse)
    def sort_set(set_: set, k, rev: bool):
        print(f"Сортировка списка {set_} с ключом ({k}), значение reverse: {rev}")
        set_to_list = list(set_)
        result = sorted(set_to_list, key=k, reverse=rev)

        print(f"Результат: {result}\n")
        return result

    # Проверка наличия значения во множестве
    def find(set_: set, value):
        print(f"Проверка наличия значения ({value}) в списке {set_}")

        for item in set_:
            try:
                if item == value:
                    print(f"Элемент ({value}) существует во множестве\n")
                    return True
            except StopIteration:
                break

        print(f"Указанный элемент ({value}) не найден в списке\n")

    print("Set")
    print("=====================================")

    a = {1, 2, 3, 4, 5, 5, 3}
    b = {1, 5, 4}

    c = {'W', 'e', 'd', 'l', 'o'}
    d = {'W', 'o', 'r', 'l', 'd'}
    f = {'o', 'W', 'l'}

    add_one(a, 10)

    remove_element(b, 1)

    remove_last_element(a)

    slice_set(a, 1, 4)

    slice_step_set(a, 1, 4, 2)

    combine_two(c, d)

    sort_set(set_intersection(c, f), None, rev=True)

    if find(d, "f"):
        print("Проверка выполнена успешно\n")
    else:
        print("")


def main():
    list_functions()
    dict_functions()
    set_functions()


main()
