import os


def countBytes(path):
    overall_bytes = 0
    current_directory = os.listdir(path)
    for elem in current_directory:
        path2 = os.path.join(path, elem)
        if os.path.isdir(path2) is True:
            overall_bytes = overall_bytes + countBytes(path2)
        elif os.path.isfile(path2) is True:
            overall_bytes = overall_bytes + os.path.getsize(path2)
    return overall_bytes


if __name__ == '__main__':
    countBytes()
