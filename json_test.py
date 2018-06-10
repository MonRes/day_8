import json

data = {'spam': (1,2,3), 'eggs': {'a': 2, 'b': 3}} #krotka zmienia się na listę w jsonie
serialized = json.dumps(data)
print(data)
print(serialized)

#serializować można prawie wszystko, nie da się liczb spolonych
#zobaczyć sobie customer coder

data2 = json.loads(serialized)
print(data2)

## loadS i dumpS jest do stringów (wczytuje z łańcucha znaków) do plików load i dump

with open('data.json', 'wt') as json_file:
    json.dump(data, json_file) #obietk (co zapisać) i file pointer (gdzie zapisać)

with open('data.json', 'rt') as json_file:
    print(json.load(json_file)) #ładuje z pliku (obiekt plikowy nie jego ścieżkę)