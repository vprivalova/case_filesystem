import ru_local as ru


def aссeptСommand():
    numbers_point = ["1", "2", "3", "4", "5", "6", "7"]
    command = input(ru.CHOICE)
    while command not in numbers_point:
        command = input(ru.CHOICE_AGAIN)
    return command


if __name__ == '__main__':
    aссeptСommand()
