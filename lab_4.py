import json
import csv
import datetime


class Person:
    name: str = None
    birthday: datetime.date = None

    def __init__(self, name: str, birthday: str):
        self.name = name
        self.birthday = datetime.datetime.fromisoformat(birthday).date()

    def __repr__(self):
        return f"{self.name} [{self.birthday}]"

    def __eq__(self, obj):
        return self.name == obj.name and self.birthday == obj.birthday

    def to_dict(self):
        return {
            "name": self.name,
            "birthday": self.birthday
        }


class Data:
    p1 = Person(name="Isabela", birthday="2004-03-03")
    p2 = Person(name="Larissa", birthday="2004-04-03")

    persons_1 = [
        Person(name="Ivan", birthday="2000-01-02"),
        Person(name="Olga", birthday="1998-10-08"),
        Person(name="Ben", birthday="1999-02-03"),
        Person(name="Sam", birthday="2001-01-10"),
        Person(name="Lina", birthday="2001-12-09")
    ]
    persons_2 = [
        Person(name="Ben", birthday="1999-02-03"),
        Person(name="Ivan", birthday="2000-01-02"),
        Person(name="Sam", birthday="2001-01-10"),
        Person(name="Lina", birthday="2001-12-09"),
        Person(name="Olga", birthday="1998-10-08")
    ]


class Functions:
    #Сортировка по именам
    @staticmethod
    def sort_by_name(persons: list):
        persons.sort(key=lambda x: x.name)

    #Сортировка по датам рождения
    @staticmethod
    def sort_by_date(persons: list):
        persons.sort(key=lambda x: x.birthday)

    #Сортировка по годам рождения
    @staticmethod
    def sort_by_year(persons: list):
        persons.sort(key=lambda x: x.birthday.year)

    #Сортировка по месяцам рождения
    @staticmethod
    def sort_by_month(persons: list):
        persons.sort(key=lambda x: x.birthday.month)

    #Сортировка по дням рождения
    @staticmethod
    def sort_by_day(persons: list):
        persons.sort(key=lambda x: x.birthday.day)

    #Сравнение двух списков
    @staticmethod
    def equal(list_1: list, list_2: list):
        l1 = sorted(list_1, key=lambda x: x.name)
        l2 = sorted(list_2, key=lambda x: x.name)
        if l1 == l2:
            print(f"Списки одинаковые.")
            return True
        else:
            print(f"Списки разные.")
            return False

    #Сравнение двух персон
    @staticmethod
    def equal_two_person(pers_1: Person, pers_2: Person):
        if pers_1 == pers_2:
            print("Эти персоны одинаковы.")
            return True
        else:
            print(f"{pers_1.name} и {pers_2.name} разные.")
            return False

    #Сравнение имен персон
    @staticmethod
    def equal_name(pers_1: Person, pers_2: Person):
        if pers_1.name == pers_2.name:
            print("У этих персон одинаковые имена.")
            return True
        else:
            print(f"У {pers_1.name} и {pers_2.name} разные имена.")
            return False

    #Сравнение полных дат рождения
    @staticmethod
    def equal_birthday_date(pers_1: Person, pers_2: Person):
        if pers_1.birthday == pers_2.birthday:
            print(f"У {pers_1.name} и {pers_2.name} одинаковая дата рождения.")
            return True
        else:
            print(f"У {pers_1.name} и {pers_2.name} разные даты рождения.")
            return False

    #Сравнение годов рождения
    @staticmethod
    def equal_birthday_year(pers_1: Person, pers_2: Person):
        if pers_1.birthday.year == pers_2.birthday.year:
            print(f"У {pers_1.name} и {pers_2.name} одинаковый год рождения.")
            return True
        else:
            print(f"У {pers_1.name} и {pers_2.name} разные года рождения.")
            return False

    #Сравнение месяцев рождения
    @staticmethod
    def equal_birthday_month(pers_1: Person, pers_2: Person):
        if pers_1.birthday.month == pers_2.birthday.month:
            print(f"У {pers_1.name} и {pers_2.name} одинаковый месяц рождения.")
            return True
        else:
            print(f"У {pers_1.name} и {pers_2.name} разные месяца рождения.")
            return False

    #Сравнение дней рождения
    @staticmethod
    def equal_birthday_day(pers_1: Person, pers_2: Person):
        if pers_1.birthday.day == pers_2.birthday.day:
            print(f"У {pers_1.name} и {pers_2.name} одинаковый день рождения.")
            return True
        else:
            print(f"У {pers_1.name} и {pers_2.name} разные дни рождения.")
            return False

    @staticmethod
    def list_to_dict(lis: list):
        result = list()
        for p in lis:
            result.append(p.to_dict())
        return result


class FileManager:
    @staticmethod
    def write_csv():
        with open("Persons.csv", "w") as file:
            columns = ["name", "birthday"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

            dictionary = Functions.list_to_dict(Data.persons_1)

            writer.writerows(dictionary)

    @staticmethod
    def read_csv():
        with open("Persons.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row["name"], "-", row["birthday"])

    @staticmethod
    def write_json():
        with open("Persons.json", "w") as file:
            json.dump(Data.p2.to_dict(), file, default=str)

    @staticmethod
    def read_json():
        with open("Persons.json", "r") as file:
            x = json.load(file)
            print(x)


def main():
    #Работа с классом Person
    print(f"Сравниваем два списка: \n{Data.persons_1} \n{Data.persons_2}")
    Functions.equal(Data.persons_1, Data.persons_2)

    print(f"\nСравниваем две персоны: {Data.p1} и {Data.p2}")
    Functions.equal_two_person(Data.p1, Data.p2)
    Functions.equal_name(Data.p1, Data.p2)

    Functions.equal_birthday_date(Data.p1, Data.p2)

    print("\nСортировка списка персон:")

    print(f"До сортировки: {Data.persons_1}")

    Functions.sort_by_name(Data.persons_1)
    print(f"После сортировки по именам: {Data.persons_1}")

    #Считывание и запись данных объектов из/в csv/json
    print("\n")
    FileManager.write_csv()
    print("Считываем данные из файла 'Persons.cvs':")
    FileManager.read_csv()

    print("\n")
    FileManager.write_json()
    print("Считываем данные из файла 'Persons.json':")
    FileManager.read_json()


main()
