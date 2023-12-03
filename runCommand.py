import os


def runCommand(command):
    path = os.getcwd()

    if command == '1':
        print(os.listdir(path="."))

    if command == '2':
        print(os.chdir(path=".."))

    if command == '3':
        pass
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
