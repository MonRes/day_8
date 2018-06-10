import copy
import json

class Stock:

    def __init__(self, initial):
        self.products = copy.deepcopy(initial)


    def resupply(self, product, count):

        if count <=0:
            raise ValueError('Can ressuply only with possitive count')

        self.products[product] = self.products.get(product, 0) + count #przypisanie nie pobranie


    def withdraw(self, product, count):
        if count <=0:
            raise ValueError('Can ressuply only with possitive count')
        if product not in self.products:
            raise ValueError('Unknown product ' + product)
        if self.products[product] < count:
            raise ValueError('Insufficient number of items in stock')

        self.products[product] -= count

    def to_json(self):
        return json.dumps(self.products)

    @staticmethod
    def from_json(json_str):
        products = json.loads(json_str)
        return Stock(products)

    def to_json_file(self, output_file):
        return json.dump(self.products, output_file)

    @staticmethod
    def from_json_file(json_file):
        return(Stock(json.load(json_file)))


    def available_items(self):
        items = {}
        for product, count in self.products.items():
            if count > 0:
                items[product] = count
        return items


# products = {'orange': 2, 'bananas': 3} #przypisanie obiektu do zmiennej nie tworzy jego kopii, nie robić tak
stock = Stock({'orange': 2, 'bananas': 3})
stock.resupply('lemon', 1)

print(stock.products)
#products['orange'] = -500 # tak nie robić
print((stock.products))
print(stock.to_json())

stock_json = stock.to_json()
stock2 = Stock.from_json(stock_json)
print(stock2.available_items() == stock.available_items())
print(stock2.products == stock.products)

with open('data2.json', 'wt') as json_file:
    json.dump(stock.products, json_file)

with open('data2.json', 'rt') as json_file:
    print(json.load(json_file))

#lub z użyciem stworoznych metod

with open('stock.json', 'wt') as stock_json:
    stock.to_json_file(stock_json)

with open('stock.json', 'rt') as stock_json:
    stock4 = Stock.from_json_file(stock_json) #żeby zapisać te dane

print(stock.products)