
# A function that accepts any number of integers and returns the sum of all of them
def add(*numbers):
    sum=0
    for numb in numbers:
        sum+=numbers
    return sum

def multiply(*numbers):
    numb=1
    for number in numbers:
        numb*=numbers
    return numb
