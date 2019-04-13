# файл с набором функций для обработки переписок


# обработка переписок между 2 людьми

# первое имя - имя пользователя, написавшего певым сообщения, второе имя - имя собеседника

# путь до файла указываем полный, начиная от запускаемого файла (например, если мы функцию запускаем в
# файле Main.py, а файл с необработанными данными хранится в папке DataProcessing и называется chat.txt,
# то путь будет следующим: DataProcessing/chat.txt)

# переменная do_save - булевого типа. True, если хотим затем сохранить обработанную переписку в отдельном файле
def main(first_name, second_name, path_of_file1, do_save):
    name1 = first_name
    name2 = second_name
    name_of_file = path_of_file1
    this_name = name1
    message = ''
    end_of_message = []

    file = open(name_of_file)
    for line in file:
        # здесь, с помощью условных операторов, добиваемся, чтобы подряд идущие сообщения от одного пользователя
        # сохранялись как одно целое сообщение. Ограничитель - точка
        # делается это с помощью проверки на имя (поменялось ли)
        if (line.find(name1) != -1) | (line.find(name2) != -1):
            if line.find(this_name) == -1:
                end_of_message.append(message)
                message = ''
                if this_name != name1:
                    this_name = name1
                    print(line + "1")
                else:
                    this_name = name2
                    print(line + "2")

        elif (line != '') & (line != '\n') & (line != '\t') & (line.find('http') == -1):
            line = line.strip()
            line = line.replace("(end)", "")
            if message != '':
                message += '. ' + line
            else:
                message += line

    if do_save:
        # сохраняем переписку в файле
        f = open(name_of_file + 'endOfData.txt', 'w')
        for i in end_of_message:
            f.write(i + '\n')

    print(end_of_message)
    return end_of_message


# функция для обработки переписок бесед

# путь до файла указываем полный, начиная от запускаемого файла (например, если мы функцию запускаем в
# файле Main.py, а файл с необработанными данными хранится в папке DataProcessing и называется chat.txt,
# то путь будет следующим: DataProcessing/chat.txt)

# переменная do_save - булевого типа. True, если хотим затем сохранить обработанную переписку в отдельном файле
def big_chats(path_of_file1, do_save):
    file = open(path_of_file1)
    message = ''
    end_of_message = []
    first_four_letters = ''

    for line in file:
        # здесь, с помощью условных операторов, добиваемся, чтобы подряд идущие сообщения от одного пользователя
        # сохранялись как одно целое сообщение. Ограничитель - точка
        # делается это с помощью проверки на первые 4 символа имени
        if (line.find('start') != -1) | (line.find('end') != -1):
            if line.find('start') != -1:
                if first_four_letters != line[:4]:
                    first_four_letters = line[:4]
                    if message != '':
                        end_of_message.append(message)
                        message = ''

        elif (line != '') & (line != '\n') & (line != '\t') & (line.find('http') == -1):
            line = line.strip()
            line = line.replace("(end)", "")
            if message != '':
                message += '. ' + line.capitalize()
            else:
                message += line.capitalize()

    if do_save:
        # сохраняем переписку в файле
        f = open(path_of_file1 + 'endOfData.txt', 'w')
        for i in end_of_message:
            f.write(i + '\n')

    print(end_of_message)
    # возвращаем массив строк, в котором каждая новая строка - сообщение пользователя
    return end_of_message
