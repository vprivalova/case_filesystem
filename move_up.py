import os


def moveUp():
    return os.chdir(path="..")


if __name__ == '__main__':
    moveUp()
