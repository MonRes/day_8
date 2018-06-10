import os

if __name__ == '__main__':

    path = '/home/student'

    for file in os.listdir('.'):
        stat = os.stat(file)
        print(file, ': ', stat.st_size)

    for file in os.listdir(path):
        try:
            stat = os.stat(os.path.join(path, file))
            print(file, stat.st_atime, stat.st_size)
        except FileNotFoundError:
            print('Plik nie istnieje', file)