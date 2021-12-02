
def fibonacci(n):
    a = 0
    b = 1
    if n==1:
        return a
    if n==2:
        return b
    else:
        i = 3
        while i<=n:
            a, b = b, a+b
            i += 1
        return b

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Animal:

    def __init__(self, type):
        self.type = type

X = 100
_y = 20         
    