def acceptCommand():
    numbers_point = ["1", "2", "3", "4", "5", "6", "7"]
    command = input('Выберите пункт меню: ')
    while command not in numbers_point:
        command = input('Пожалуйста, повторите попытку ввода номера команды')


if __name__ == '__main__':
    acceptCommand()