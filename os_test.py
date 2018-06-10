import os # metody do operowania na plikach, katalogach itp
from datetime import datetime

if __name__ == '__main__':
    print(os.name)
    print(os.uname())
    print(os.listdir('.')) # listę rzeczy w tym katalogu
    print(os.stat('data.json')) # zwraca info o pliku np. tryb uprawnień, wielkość w bajtach, st_atime: czas dostępu
    print(os.stat('data.json')[-4])
    stat = os.stat('data.json')
    print('Rozmiar: ', stat.st_size)
    atime = datetime.fromtimestamp(stat.st_atime)
    print('Ostatni dostęp: ', atime)
    print(os.getcwd()) #wypisuje bieżącą ścieżkę



