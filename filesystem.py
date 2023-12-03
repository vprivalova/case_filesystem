import os
import acceptCommand

MENU = '''
    Меню:
    1. Просмотр каталога
    2. На уровень вверх
    3. На уровень вниз
    4. Количество файлов и катаогов
    5. Размер текущего каталога (в байтах)
    6. Поиск файла
    7. Выход из программы
    '''


def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == '7':
            print('Работа программы завершена.')
            break

    if __name__ == '__main__':
        main()