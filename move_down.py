import os
import ru_local as ru


def moveDown(currentDir):
    path = os.getcwd()
    catalogs = os.listdir(path)
    while currentDir not in catalogs:
        currentDir = input(ru.SUBDIRECTORY_AGAIN)
    new_catalog = path + "\\" + currentDir
    return os.chdir(new_catalog)


if __name__ == '__main__':
    moveDown()
