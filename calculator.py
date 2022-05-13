def add(a, b):
    answer = a + b
    return(answer)
def subtract(a, b):
    answer = a - b
    return(answer)
def multiply(a, b):
    answer = a * b
    return(answer)
def divide(a, b):
    answer = a / b
    return(answer)
def modulus(a, b):
    answer = a % b
    return(answer)
def exponent(a, b):
    answer = a ** b
    return(answer)
def int_divide(a, b):
    answer = a // b
    return(answer)
def square(a):
    answer = a** 2
    return(answer)
def cube(a):
    answer = a **3
    return(answer)

def factorial(l):
    factor =1
    for a in range(1,l+1):
        factor*=a
    return(factor)