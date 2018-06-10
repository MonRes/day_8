import copy
import json

class TabularData:

    def __init__(self, column_names):
        self.column_names = list(column_names)
        self._columns = {}
        for idx, name in enumerate(column_names):
            self._columns[name] = idx
        # wyrażenie słownikowe self._columns={name: idx for idx, name in enumerate(column_names)}
        if len(column_names) > len(self._columns):
            raise ValueError('Column names have to be uniqe')
        self._rows = [] #możemy definiować ile chcemy danych a nie musimy ich mieć w atrybucie metody, column names jest wymagane

# taki zapis _rows = to pole prywatne

    def to_dict(self):
        return {'columns': self.column_names, 'rows': self._rows}

    @staticmethod
    def from_dict(data):
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_json(json_data):
        return TabularData.from_dict(json.loads(json_data))


    def to_json_file(self, output_file):
        return json.dump(self.to_dict(), output_file)

    @staticmethod
    def from_json_file(json_file):
        return TabularData.from_dict(json.load(json_file))


    def get_row(self, row_no):
        if row_no < 0 or row_no >= len(self._rows):
            raise IndexError('Invalid row number: ', row_no)
        return self._rows[row_no]


    def get_column(self, col_name):
        if col_name not in self._columns:
            raise KeyError('Unknow column: ', col_name)
        idx = self._columns[col_name]
        # return [row[idx] for row in self.rows] - wyrażenie listowe dla pętli poniżej
        values = []
        for row in self._rows:
            values.append(row[idx])
        return values


    def append(self, new_row):
        if len(new_row) != len(self._columns):
            raise ValueError('to many elements')
        self._rows.append(list(new_row))

    def rows_count(self):
        return len(self._rows)

    def to_list(self):
        return copy.deepcopy(self._rows)

    def __len__(self): #jak ktoś wywoła len na mnie to ty wywołaj len
        return len(self._rows)

    def __str__(self): #zmieniamy całą tabelkę na str
        return str(self._rows)

table = TabularData(['name', 'surname', 'age'])

json_dict = table.to_json() #serializacja tabelki
table2 = TabularData.from_json(json_dict)
print(table2.column_names == table.column_names)
print(table2._rows == table._rows)


table.append(['John', 'Doe', 30])
table.append(['Joe', 'Dragon', 20])
table.append(['Ann', 'Philips', 10])
table.append(['Christopher', 'Carmen', 12])
print(table.to_json())

with open('dict.json', 'wt') as json_dict:
    table.to_json_file(json_dict)

with open('dict.json', 'rt') as json_dict:
    table4 = TabularData.from_json_file(json_dict)

print(table4.column_names == table.column_names)
print(table4._rows == table._rows)