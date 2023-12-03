import os

import move_down
import move_up


def runCommand(command):
    path = os.getcwd()

    if command == '1':
        print(os.listdir(path="."))

    if command == '2':
        print(move_up.moveUp())

    if command == '3':
        currentDir = input('Введите имя подкаталога: ')
        print(move_down.moveDown(currentDir))
    if command == '4':
        pass
    if command == '5':
        pass
    if command == '6':
        pass
    if command == '7':
        pass


if __name__ == '__main__':
    runCommand()
