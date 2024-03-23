from logger import input_data, print_data
from edite import edite_data
from delet import delete_data


def interface():
    print("Добрый день! Вы попали в бот-справочник! \n 1-запись данных \n 2-вывод данных \n 3-изменить данные \n 4-удалить данные")
    command = int(input())

    while command != 1 and command !=2 and command !=3 and command !=4:
        print("Неправильный ввод")
        command = int(input('Введите число '))

    if command ==1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edite_data()
    elif command == 4:
        delete_data()