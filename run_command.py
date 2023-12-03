import os
import count_bytes
import count_files
import find_files
import move_down
import move_up
import ru_local as ru
import find_files


def runCommand(command):
    path = os.getcwd()

    if command == '1':
        print(os.listdir(path))

    if command == '2':
        print(move_up.moveUp())

    if command == '3':
        currentDir = input(ru.SUBDIRECTORY)
        print(move_down.moveDown(currentDir))

    if command == '4':
        print(count_files.countFiles(path))

    if command == '5':
        print(count_bytes.countBytes(path))

    if command == '6':
        target = input(ru.INPUT_NAME)
        result = find_files.findFiles(target, path)
        print(*result, sep='\n')



if __name__ == '__main__':
    runCommand()
