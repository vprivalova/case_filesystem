import os


def findFiles(target, path):
    current_directory = os.listdir(path)
    list_paths = []
    for elem in current_directory:
        if target in elem:
            path2 = os.path.join(path, elem)
            if os.path.isfile(path2) is True:
                list_paths.append(path2)
    if len(list_paths) == 0:
        return 'Файла содержащего такое название нет.'
    else:
        return list_paths


if __name__ == '__main__':
    findFiles()
