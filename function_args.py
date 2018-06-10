def foo(x, y, *args,  **kwargs): #może być tylko jeden argument, który ma dwie gwiazdki i można dopisywać tutaj argumenty
    print(kwargs)
    print(args)
    print(x, y)

#* args - argumenty pozycyjne, których nie znam w krotce
#** argumenty kluczowe jako słownik
# x, y wypisuje normalnie
#kolejność - najpier x, y, potem args, a potem kwargs

foo(1, 2, 20, 30, first_name='Adam', age=100)