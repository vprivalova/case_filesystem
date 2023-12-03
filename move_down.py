import os


def moveDown(currentDir):
    path = os.getcwd()
    catalogs = os.listdir(path=".")
    while currentDir not in catalogs:
        currentDir = input('Пожалуйста, повторите попытку ввода имени подкаталога: ')
    new_catalog = path + "\\" + currentDir
    return os.chdir(new_catalog)


if __name__ == '__main__':
    moveDown()
