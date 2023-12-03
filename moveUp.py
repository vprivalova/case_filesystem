import os


def moveUP():
    return os.chdir(path="..")


if __name__ == '__main__':
    moveUP()
