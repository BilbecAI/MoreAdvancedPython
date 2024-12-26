#Dekorator rejestrujący czas i liczbę wywołań. 

import time 
def decorator2(func): #tworzymy dekorator ktory jako argument przyjmnie funkcje
    def wrapper(*args, **kwargs): #tworzymy funckje wewnetrzna ktora jako argument przyjmie argumenty
        start = time.time() #definiujemy poczatek i koniec
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end-start:.5f} seconds") #oblicamy czas
        return result
    return wrapper
def decorator (func): #tworzymy dekorator ktory jako argument przyjmnie funkcje
    count=0 #rozpoczynami odlicznaie od 0 
    def wrapper(*args, **kwargs): #tworzymy funckje wewnetrzna ktora jako argument przyjmie argumenty
        nonlocal count
        count+=1 #liczymy ile razy zostala wywolana fukncja
        result=func(*args, **kwargs) # wszędzie musimy dodc result i go wypluć
        print(f"Function {func.__name__} was called {count} times")
        return result
    return wrapper
@decorator2
@decorator
def add (a,b):
    return a+b

print(add(3,5))
print(add(56,43))