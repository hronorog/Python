import os
from datetime import datetime

timez = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
suffix_orig = '_txt_orig.txt'
suffix_tran = '_txt_tran.txt'


# стоп-слово для приостановки работы скрипта

def stop():
    a = input('Press any key to continue or "s" to stop\n')
    if a == "s":
        exit()


def parser(filename):
    FILENAME = filename
    score_rpy = score_word = 0

    with open(FILENAME, "r", encoding='utf-8') as f:
        massiv = f.readlines()

    for i, line in enumerate(massiv, start=0):
        if ".rpy:" in line:
            score_rpy += 1
            if "translate" in massiv[i + 1]:
                #print(i, massiv[i], i + 3, massiv[i + 3])
                with open(FILENAME.split('.')[0] + suffix_orig, 'a', encoding='utf-8') as f2:
                    f2.write(massiv[i + 3])
                score_word += 1
            elif "old" in massiv[i + 1]:
                with open(FILENAME.split('.')[0] + suffix_orig, 'a', encoding='utf-8') as f2:
                    f2.write(massiv[i + 1])
                score_word += 1

    print('Создан файл {}'.format(FILENAME.split('.')[0] + suffix_orig))
    if score_rpy != score_word:
        print('{}\n{}:{}\n{}:{}\n'.format('File length mismatch!',
              FILENAME, score_rpy,
              FILENAME.split('.')[0] + suffix_orig, score_word))


def parser_tran(filename):
    FILENAME = filename

    score_rpy = score_word = 0

    with open(FILENAME, "r", encoding='utf-8') as f:
        massiv = f.readlines()

    for i, line in enumerate(massiv, start=0):
        if ".rpy:" in line:
            score_rpy += 1
            if "translate" in massiv[i + 1]:
                #print(i, massiv[i], i + 3, massiv[i + 3])
                with open(FILENAME.split('.')[0] + suffix_tran, 'a', encoding='utf-8') as f2:
                    f2.write(massiv[i + 4])
                score_word += 1
            elif "old" in massiv[i + 1]:
                with open(FILENAME.split('.')[0] + suffix_tran, 'a', encoding='utf-8') as f2:
                    f2.write(massiv[i + 2])
                score_word += 1

    print('Создан файл {}'.format(FILENAME.split('.')[0] + suffix_tran))
    print('Всего блоков в файле {}: {}'.format(FILENAME, score_rpy))
    print('Всего строк в файле {}: {}'.format(FILENAME, score_word))
    print()


# проверка на непарные кавычки
def check(filename):
    a = [filename, ]
    with open(filename, 'r', encoding='utf-8') as f:
        # проверка на кавычки
        for i, line in enumerate(f.readlines(), start=1):
            if line.count('"') % 2 != 0:
                a.extend((i, line))
    # вывод строк с непарными кавычками
    if len(a) > 1:
        print(filename)
        for x in range(1, len(a), 2):
            print(a[x], a[x+1])
            stop()


# проверка на русские буквы
def miss_letter(filename):
    lett = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    a = True
    print(filename)
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines(), start=1):
            for w in line:
                if w.isalpha():
                    if lett.find(w.lower()) != -1:
                        print(i, line)
                        a = False
                        break
    if a: print("Ok")


def reverse(filename):
    try:
        mydir = os.path.join(
            os.getcwd(), 
            timez)
        try:
            os.makedirs(mydir)
        except FileExistsError:
            print('Папка {} уже существует'.format(mydir))

        FILENAME = filename
        TRANSLATE = FILENAME.split('.')[0] + suffix_orig
        score_rpy = score_word = 0
        str_f = str_tr = 0

        with open(FILENAME, "r", encoding='utf-8') as f:
            massiv = f.readlines()
            for i, line in enumerate(massiv, start=0):
                if ".rpy:" in line:
                    str_f += 1

        with open(TRANSLATE, "r", encoding='utf-8') as tr:
            trans = tr.readlines()
            str_tr = len(trans)

        # проверка на равенство строк
        if str_f == str_tr:
            for i, line in enumerate(massiv, start=0):
                if ".rpy:" in line:
                    score_rpy += 1

                    if "translate" in massiv[i + 1]:
                        str_zamena = trans.pop(0)
                        # удаление хеша из строки
                        str_zamena = str_zamena[:4] + str_zamena[5:]
                        massiv.pop(i + 4)
                        massiv.insert(i + 4, str_zamena)

                        score_word += 1

                    elif "old" in massiv[i + 1]:
                        str_zamena = trans.pop(0)
                        # замена old на new в строке
                        str_zamena = str_zamena[:4] + 'new' + str_zamena[7:]
                        massiv.pop(i + 2)
                        massiv.insert(i + 2, str_zamena)

                        score_word += 1

            # возвращаем список в файл
            try:
                with open('{}\{}{}'.format(mydir, FILENAME.split('.')[0], '.rpy'), 'a', encoding='utf-8') as frev:
                    frev.writelines(massiv)
            except FileExistsError:
                print('Папка с именем {} уже существует'.format(mydir))

            print('\nСоздан файл {}\{}{}\nOK'.format(mydir, FILENAME.split('.')[0], '.rpy'))
        elif str_f == 0 or str_tr == 0:
            print("Файлы пусты")
        else:
            print('{}\n{}:{}\n{}:{}\n'.format('File length mismatch!',
                                                FILENAME, score_rpy,
                                                TRANSLATE, score_word))
            exit()

    except FileNotFoundError:
        print('Файл {} не найден'.format(FILENAME.split('.')[0] + suffix_orig))


# создание дерева папок и файлов

def tree():
    for address, papka, files in os.walk(os.getcwd()):
        print("Адрес: {}".format(address))

        if papka != []:
            papka = ', '.join(papka)
        else:
            papka = 0
        print("Папки: {}".format(papka))

        print("Файлы: ")
        if files:
            for i in files:
                print(i)
        else:
            print('0')
        print('_________________\n')


# выдирание строк из всех файлов в каталоге

def tree2():
    for address, papka, files in os.walk(os.getcwd()):
        if files:
            print(address, '\n', papka, '\n', files)
            for i in files:
                if "rpy" in str(i):
                    parser(address + '\\' + i)
            print('_________________\n')


# выдирание строк перевода из всех файлов в каталоге

def tree2_tran():
    for address, papka, files in os.walk(os.getcwd()):
        if files:
            print(address, '\n', papka, '\n', files)
            for i in files:
                if "rpy" in str(i):
                    parser_tran(address + '\\' + i)
            print('_________________\n')


# вставить правильный перевод во все файлы в каталоге

def tree2_reverse():
    for address, papka, files in os.walk(os.getcwd()):
        if files:
            print(address, '\n', papka, '\n', files)
            for i in files:
                if "rpy" in str(i):
                    reverse(address + '\\' + i)
            print('_________________\n')


# основное меню

def folders():
    os.system('cls')
    print('Содержимое текущей папки:\n')
    fd = os.listdir()
    for i in fd:
        if i.split('.')[-1] == 'rpy':
            print(i)
    choose()


# меню
def choose():
    b = input('\nВыберите пункт меню:'
              '\n1. Выдернуть из всех файлов в текущей папке дорожку оригинала'
              '\n2. Выдернуть из всех файлов в текущей папке дорожку перевода'
              '\n3. Проверить файл на незакрытые кавычки и русские буквы'
              '\n4. Проверить файлы на русские буквы в переводе'
              '\n5. Вставить правильный перевод в файлы оригинала'
              '\n6. Выход из программы\n'
              '\n7. Создать дерево папок'
              '\n11. Выдернуть дорожку оригинала из всех файлов в каталоге'
              '\n22. Выдернуть дорожку перевода из всех файлов в каталоге'
              '\n55. Вставить правильный перевод во все файлы в каталоге'
              '\n')

    if b == '1':
        for i in os.listdir():
            if i.split('.')[-1] == 'rpy':
                parser(i)
        choose()

    elif b == '2':
        for i in os.listdir():
            if i.split('.')[-1] == 'rpy':
                parser_tran(i)
        choose()

    elif b == '3':
        for i in os.listdir():
            if suffix_orig in i:
                check(i)
        choose()

    elif b == '4':
        for i in os.listdir():
            if suffix_orig in i:
                miss_letter(i)
        choose()

    elif b == '5':
        for i in os.listdir():
            if i.split('.')[-1] == 'rpy':
                try:
                    reverse(i)
                except FileExistsError:
                    print('Сорян')
        choose()

    elif b == '7':
        tree()
        choose()

    elif b == '11':
        tree2()
        choose()

    elif b == '22':
        tree2_tran()
        choose()

    elif b == '55':
        reverse()
        choose()

    elif b == '6':
        exit()

    else:
        print('Шта?')
        choose()


def screen():
    os.system('cls')

    while True:
        folders()


if __name__ == '__main__':
    screen()



''' 
v.1.4.2
- добавлен пункт массового извлечения строк с переводом
- добавлен пункт массовой замены первода во всех файлах каталога
 
v.1.4.1
- добавлен пункт отрисовки дерева каталогов
- добавлен пункт массового извлечения строк из всех папок, начиная с корня программы

v.1.3.3
- добавлено стоп-слово для ручного управления процессами

v.1.3.2
- проверка на совпадение строк при извлечении русских строк из файла и при слиянии перевода с оригиналом
- косметические улучшения в парсере

v. 1.3.1
- проверка файла с переводом на наличие кириллици

v.1.2.1
- при проверке на непарные кавычки выводит имя файла, номер строки и строку
'''
