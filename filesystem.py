"""
Team:
Nizovtseva Anastasia 90
Privalova Viktoria 95
"""


import os
import ru_local as ru


def main():
    """
    The function displays the path to the current directory,
    the menu and calls the command request and execution function.
    :return: None
    """

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
    """
    The function inquires the number of the command.
    In case of incorrect entry, the function outputs an error message and
    continues requesting the number until the correct entry is done.
    :return: apropriate selected command number
    """

    numbers_point = ["1", "2", "3", "4", "5", "6", "7"]
    command = input(ru.CHOICE)
    while command not in numbers_point:
        command = input(ru.CHOICE_AGAIN)
    return command


def moveUp():
    """
    The function makes the parent directory current.
    :return: None
    """
    os.chdir(path="..")


def moveDown(currentDir):
    """
    The function makes the currentDir directory the current directory.
    If the value of the variable is incorrect,
    it prints an error message and makes a request for a new value of the variable.
    :param currentDir: directory
    :return: None
    """

    path = os.getcwd()
    catalogs = os.listdir(path)
    while currentDir not in catalogs:
        currentDir = input(ru.SUBDIRECTORY_AGAIN)
    new_catalog = path + "\\" + currentDir
    os.chdir(new_catalog)


def countBytes(path):
    """
    The function calculates the total size (in bytes) of all files in the given directory.
    :param path: iven directory
    :return: total number of bytes
    """

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
    """
    The function generates a list of file paths from all 'path' subdirectories whose name contains 'target'.
    :param target: string
    :param path: directory
    :return: list of file paths
    """

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
    """
    The function counts the number of files in the given directory.
    :param path: given directory
    :return: number of files
    """

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
    """
    The function determines by the command number which command should be executed and calls it.
    :param command: number of command to be done
    :return: None
    """

    path = os.getcwd()

    if command == '1':
        print(os.listdir(path))

    if command == '2':
        moveUp()

    if command == '3':
        currentDir = input(ru.SUBDIRECTORY)
        moveDown(currentDir)

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
