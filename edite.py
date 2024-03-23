from data_create import name_data, surname_data, phone_data, address_data


first = 'data_first_variant.csv'
second = 'data_second_variant.csv'

def edite_data():
    file_name = input('Введите имя файла, в котором нужно изменить данные: ')
    with open(first, 'r', encoding='utf-8') as f:
        data = f.readlines()
    with open(second, 'r', encoding='utf-8') as f:
        data = f.readlines()

    print('Текущие данные:')
    print(*data)

    index_to_correct = int(input('Введите номер строки для изменения: ')) - 1
    if 0 <= index_to_correct < len(data):
        new_data = input('Введите новые данные: ')
        data[index_to_correct] = f'{new_data}\n'

        with open(first, 'w', encoding='utf-8') as f:
            f.writelines(data)
        with open(second, 'w', encoding='utf-8') as f:
            f.writelines(data)
        print('Данные успешно изменены!')
    else:
        print('Неверный номер строки.')
