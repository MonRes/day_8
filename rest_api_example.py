import hashlib
import requests

BASE_URL = 'http://polakow.eu:3000/people/' # tak jest poprawnie (..)/people bez slesza to inna ścieżka

response = requests.get(BASE_URL, params={'_limit': 3, '_page': 2}) #podstawowa forma getu
print(response.json()) #zdekodowany obiekt, lista, w którym są słowniki itp.
print(response.text)
print(response.headers)
print(response.status_code) #z jakim kodem http się skończyła metoda, np 200 OK, 404 Not found itp.
print(response.headers['X-Total-Count']) #nagłówek który mówi o tym jaka jest całkowita liczba rekordów

md5 = hashlib.md5('relayr'.encode('ascii')) #funkcja która liczy md5, weź napis, zrob z niego bajty
token = md5.hexdigest() # info o skrócie zwraca łańcich znaków, cyfry szesnastkowe
print(token)
headers = {'Authorization': 'Bearer ' + token}
person = {'first_name': 'Janusz', 'last_name': 'Cebularz',
          'email': 'janusz.cebularz@gmail.com',
          'phone': '+485259494999',
          'ip_address': '192.168.1.1'}
response = requests.post(BASE_URL, json=person, headers=headers)
print(response.json())

url = BASE_URL + 't4y6Wrp'
print(requests.get(url).json()) #specyficzny endpoint odpowiadający jednemu rekordowi
print(requests.get(BASE_URL, params={'id': 't4y6Wrp'}).json()) #źle, że tak można to wyszukiwanie, które pobrało element z listy pasujący do tych id
cebularze = requests.get(BASE_URL, params={'first_name': 'Michas','last_name': 'Cebularz'}).json()
print(cebularze)

response = requests.get(BASE_URL, params={'email_like': '@gmail.com'})
print(response.json())
print('191.168.1.1'.startswith('191.168'))
print('abc'.startswith('123'))