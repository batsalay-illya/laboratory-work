import pandas as pd
import matplotlib.pyplot as plt
import requests


#Попытка аутентификации и получения куки
def authentication(login: str, password: str):
    auth = requests.post("https://ksu24.kspu.edu/api/v2/login/", data={
        'username': login,
        'password': password
    })

    if not auth.ok:
        print(f"Ошибка аутентификации. Код:{auth.status_code} {auth.text}")
        auth.raise_for_status()
    else:
        print(f"Аутентификация успешна. Статус код:{auth.status_code}")

    print("-" * 30)
    try:
        auth_cookie = auth.cookies.get_dict()["JWT"]
        return auth_cookie
    except():
        print("Ошибка получения куки аутентификации...")
        return


#Получение переменной по запросу с заданым ключем и фильтром
def get_value(url: str, auth_cookie, key, filter_by: dict = None):
    profile_request = requests.get(url=url, cookies={'JWT': auth_cookie})

    if profile_request.ok:
        data = profile_request.json()
        value = None
        if 'results' not in data.keys():
            if key in data.keys():
                value = data.get(key)
                return value
            else:
                print("Заданого ключа не существует...")
                return value
        else:
            if filter_by is None:
                for dictionary in data['results']:
                    if key in dictionary.keys():
                        value = dictionary.get(key)
                        return value
                    else:
                        print("Заданого ключа не обнаружено...")
                        return value
            else:
                filter_key = list(filter_by.keys())[0]
                for dictionary in data['results']:
                    if filter_key in dictionary.keys() and filter_by[filter_key] in dictionary[filter_key]:
                        if key in dictionary.keys():
                            value = dictionary.get(key)
                            return value
                        else:
                            print("Заданого ключа не обнаружено...")
                            return value
                print("Информации по заданому фильтру не обнаружено...")
                return value
    else:
        print(f"Запрос не выполнен. Кoд:{profile_request.status_code} - {profile_request.json()['detail']}")


#Получение json результата по запросу
def get_json(url: str, auth_cookie):
    profile_request = requests.get(url=url, cookies={'JWT': auth_cookie})

    if profile_request.ok:
        print("Запрос выполнен успешно...")
        return profile_request.json()
    else:
        print(f"Запрос не выполнен. Кoд:{profile_request.status_code}")
        profile_request.raise_for_status()
        return None


#Создание графика по заданому ключу
def create_plot(df: pd.DataFrame, key: str):
    try:
        df[key].plot(kind="barh", title='График относительно баллов студента')
        plt.show()
    except():
        print("Ошибка при построении графика...")


#Сортировка таблицы по заданным параметрам
def sort_data_frame(df, colums: list, inplance=True, ascending=False, ignore_index=False, key=None):
    return df.sort_values(by=colums, inplace=inplance, ascending=ascending, ignore_index=ignore_index, key=key)


def main():
    login = input("Логін: ")
    password = input("Пароль: ")

    auth_cookie = authentication(login=login, password=password)
    student_id = get_value(url="https://ksu24.kspu.edu/api/v2/my/students/", auth_cookie=auth_cookie, key="id")
    recordbook_id = get_value(url="https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/",
                              auth_cookie=auth_cookie, key="id")

    data = get_json(
        url="https://ksu24.kspu.edu/api/v2/my/students/" + student_id + "/recordbooks/" + recordbook_id + "/records",
        auth_cookie=auth_cookie)

    if "results" in data.keys():
        results_list = data["results"]
        df = pd.DataFrame.from_records(results_list)
    else:
        df = pd.DataFrame(data)

    sort_data_frame(df, ["result"], ascending=True)
    df.to_excel("test1.xlsx", sheet_name="Оценки", index=False)
    create_plot(df, "result")

    sort_data_frame(df, ["result"], ascending=True, key=lambda x: x % 3)
    df.to_excel("test2.xlsx", sheet_name="Оценки", index=False)
    create_plot(df, "result")

    sort_data_frame(df, ["result", "teacher_name"], ascending=True)
    df.to_excel("test3.xlsx", sheet_name="Оценки", index=False)
    #create_plot(df, "result")


main()
