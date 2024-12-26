def decorator(func):
    count=0
    def wrapper(*args, **kwargs):
        nonlocal count
        count+=1
        limit=3
        result=func(*args,**kwargs)
        if count>limit:
            print ("Limit exceeded")
        else:
            return result
    return wrapper 
@decorator
def add(a,b):
    return a+b

print(add(14,45))
print(add(13,23))
print(add(12,23))
print(add(231,34))