#Stwórz dekorator, który pozwala funkcji być wywołaną maksymalnie określoną liczbę razy. Po przekroczeniu limitu wyświetla komunikat i nie wykonuje funkcji.

def decorator(func): #tworzymy dekorator który jako argument przyjmuje funkcje
    count=0 #zaczynamy liczyć
    limit=3 # ustawiamy limit
    def wrapper(*args, **kwargs): # tworzymy dekorator ktory jako argument przyjmuje argumenty funkcji
        nonlocal count      
        if count>limit: # warunek jeżeli liczenie przekroczy limit wypluwamy komunikat 
            print ("Limit exceeded")
        else:
            count+=1 # zwiekszamy o 1 
            result=func(*args,**kwargs) # wynik funkcji
            return result
    return wrapper 
@decorator
def add(a,b):
    return a+b

print(add(14,45))
print(add(13,23))
print(add(12,23))
print(add(231,34))
