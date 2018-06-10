import requests


class PeopleClient:


    def __init__(self, base_url):
        self.base_url = base_url

    def get_all(self, limit):
        response = requests.get(self.base_url)

        if limit is None:
            return response.json()

        if limit <= 0:
            raise ValueError('Limit has to be positive.')

        response = requests.get(self.base_url, params = {'_limit': limit})
        people = response.json()

        x_total = int(response.headers['X-Total-Count'])

        if x_total % limit == 0:
            pages = x_total // limit

        else:
            pages = x_total // limit + 1

        for page in range(2, pages + 1):
            people.append(requests.get(self.base_url, params = {'_limit': limit, '_page': page }).json())
            #źle jeszcze trzeba podać extend bo [1,2] [3,4] zrobi [1,2, [3, 4]] a chcemy [1,2,3,4]
        return people


if __name__ == '__main__':
    client = PeopleClient('http://polakow.eu:3000/people/')


    print(client.get_all(200))



