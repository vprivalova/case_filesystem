import os
import accept_command
import run_command
import ru_local as ru


def main():
    while True:
        path = os.getcwd()
        print(ru.PATH, path)
        print(ru.MENU)
        command = accept_command.aссeptСommand()
        run_command.runCommand(command)
        if command == '7':
            print(ru.END)
            break


if __name__ == '__main__':
    main()
