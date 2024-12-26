#Swtórz dekortor, który przechwytuje wyjątki wypluwane przez funkcje i wyświetla odpowiedni komunikat. 


def decorator(func): #Tworzymy dekorator który za argument przyjmuje funkcje
    def wrapper(*args, **kwargs): #Musimy stworzyc funkcje wewnetrzną która za argumenty przyjmuje dowolne argumenty z funkcji divide
        if any(arg == 0 for arg in args): #Sprawdzamy czy któryś z argumentów jest równy zero
            print("Nie można dzielić przez 0")
        else:
            return func(*args, **kwargs)
    return wrapper


@decorator #Można to czytać jako decorator= decorator(divide (a,b))
def divide (a,b):
    return a/b
print(divide(10,5))
print(divide(10,0))
