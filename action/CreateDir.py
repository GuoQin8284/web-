import os


def create_dir(fileName):
    dirName = os.path.dirname(fileName)
    print(dirName)
    if os.path.exists(dirName):
        pass
    else:
        os.makedirs(dirName)