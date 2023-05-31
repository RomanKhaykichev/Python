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
        print('\n'.join(result))
        print('---------')
        return result[0]
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
    with open('Homework//Seminar_8//book.txt', 'w', encoding='utf-8') as file:
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

# позволяет редактировать отдельно ФИО и номер телефона

def enter_contact(contact:str)->str:
    """Ввод и изменение контакта (фамилия_телефон)"""
    new_fio=input("Введите ФИО: ")
    new_phone=input("Введите номер телефона: ")

    old_fio=contact.split(" | ")[0]
    old_phone=contact.split(" | ")[1]

    if len(new_fio)>0 and len(new_phone)>0:
        return f'{new_fio} | {new_phone}'
    elif not new_phone and len(new_fio)>0:
        return f'{new_fio} | {old_phone}'
    elif not new_fio and len(new_phone)>0:
        return f'{old_fio} | {new_phone}'
    return f'{old_fio} | {old_phone}'
