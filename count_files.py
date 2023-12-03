import os
import move_down


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


if __name__ == '__main__':
    countFiles()
