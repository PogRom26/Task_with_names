import os
import re

main_dir = os.path.dirname(__file__)


def clear_names(file_name: str) -> list:
    """Функция для очистки имен от лишних символов """
    new_names_list = list()

    # Строим полный путь к файлу
    file_path = os.path.join(main_dir, '..', 'data', file_name)

    with open(file_path) as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list

def is_cyrillic(name_item: str) -> bool:
    """Проверка на вхождение кириллицы в строку"""
    return bool(re.search('[а-яА-Я]', name_item))


def filter_russian_list(names_list: list) -> list:
    """Фильтрация имен написанных на русском"""
    new_names_list = list()
    for name_item in names_list:
        if is_cyrillic(name_item):
            new_names_list.append(name_item)
    return new_names_list


if __name__ == "__main__":
    cleared_names = clear_names('names.txt')

    new_file_path = os.path.join(main_dir, '..', 'data', 'names_clean_list.txt')

    for i in cleared_names:
        with open(new_file_path, 'w') as f:
            f.writelines(f"{item}\n" for item in cleared_names)

        #print(i)

print(filter_russian_list(cleared_names))