'''
Team:
Nizovtseva Anastasia 86
Privalova Viktoria 91
'''


import os
import ru_local as ru


def main():
    while True:
        path = os.getcwd()
        print(ru.PATH, path)
        print(ru.MENU)
        command = aссeptСommand()
        runCommand(command)
        if command == '7':
            print(ru.END)
            break


def aссeptСommand():
    numbers_point = ["1", "2", "3", "4", "5", "6", "7"]
    command = input(ru.CHOICE)
    while command not in numbers_point:
        command = input(ru.CHOICE_AGAIN)
    return command


def moveUp():
    return os.chdir(path="..")


def moveDown(currentDir):
    path = os.getcwd()
    catalogs = os.listdir(path)
    while currentDir not in catalogs:
        currentDir = input(ru.SUBDIRECTORY_AGAIN)
    new_catalog = path + "\\" + currentDir
    return os.chdir(new_catalog)


def countBytes(path):
    overall_bytes = 0
    current_directory = os.listdir(path)
    for elem in current_directory:
        path2 = os.path.join(path, elem)
        if os.path.isdir(path2) is True:
            overall_bytes = overall_bytes + countBytes(path2)
        elif os.path.isfile(path2) is True:
            overall_bytes = overall_bytes + os.path.getsize(path2)
    return overall_bytes


def findFiles(target, path):
    current_directory = os.listdir(path)
    list_paths = []
    for elem in current_directory:
        if target in elem:
            path2 = os.path.join(path, elem)
            if os.path.isfile(path2) is True:
                list_paths.append(path2)
    if len(list_paths) == 0:
        list_paths.append(ru.NO_FILE)
    return list_paths


def countFiles(path):
    files = 0
    current_directory = os.listdir(path)
    for elem in current_directory:
        path2 = os.path.join(path, elem)
        if os.path.isdir(path2) is True:
            files = files + countFiles(path2)
        elif os.path.isfile(path2) is True:
            files = files + 1
    return files


def runCommand(command):
    path = os.getcwd()

    if command == '1':
        print(os.listdir(path))

    if command == '2':
        print(moveUp())

    if command == '3':
        currentDir = input(ru.SUBDIRECTORY)
        print(moveDown(currentDir))

    if command == '4':
        print(countFiles(path))

    if command == '5':
        print(countBytes(path))

    if command == '6':
        target = input(ru.INPUT_NAME)
        result = findFiles(target, path)
        for elem in result:
            print(elem)


if __name__ == '__main__':
    main()
