def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))
    # return [contact for contact in book if info.lower() in contact.lower(),book]

def change_data() -> None:
    """Изменяет результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    contact_to_change = input('Введите, что хотите изменить:  ')
    contact_to_change = search(data, contact_to_change)
    print(contact_to_change)
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    data[data.index(contact_to_change)] = f'{fio} | {phone_num}'
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))

def delete_data() -> None:
    """Удаляет результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    contact_to_delete = input('Введите, что хотите удалить:  ')
    print(contact_to_delete)
    contact_to_delete = search(data, contact_to_delet)
    data.remove(contact_to_delete)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))