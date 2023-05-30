def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('Homework//Seminar_8//book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('Homework//Seminar_8//book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('Homework//Seminar_8//book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = list(filter(lambda contact: info.lower() in contact.lower(), book))
    # return [contact for contact in book if info.lower() in contact.lower(),book]
    if not result:
        return 'Совпадений не найдено'
    elif len(result)==1:
        print('---------')
        return result
    elif len(result)>1:
        print('---------')
        print('\n'.join(result))
        print('---------')
        new_info=input('Введите данные для уточнения: ')
        return search(result,new_info)


def change_data() -> None:
    """Изменяет результат поиска по справочнику."""
    with open('Homework//Seminar_8//book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        print('\n'.join(data))
        print('---------')
    contact_to_change = input('Введите, данные для изменения:  ')
    contact_to_change = search(data, contact_to_change)
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    data[data.index(contact_to_change)] = f'{fio} | {phone_num}'
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def delete_data() -> None:
    """Удаляет результат поиска по справочнику."""
    with open('Homework//Seminar_8//book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        print('\n'.join(data))
        print('---------')
    contact_to_delete = input('Введите, что хотите удалить:  ')
    contact_to_delete = search(data, contact_to_delete)
    data.remove(contact_to_delete)
    with open('Homework//Seminar_8//book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))
