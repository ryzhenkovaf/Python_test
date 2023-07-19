import Note


def createNote(number):
    title = checkInputLength(
        input('Название заметки: '), number)
    body = checkInputLength(
        input('Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Заметки'. Выбрать функцию:\n\n1 - вывод всех заметок \n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выбор заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВыбрать номер функции: ")


def checkInputLength(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def close():
    print("The end!")
