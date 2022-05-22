def sum_and_greet(*args,**kwargs):
    sum=0
    for num in args:
        sum+=num
    keys=kwargs.keys()
    if 'name' in keys:
        print(f"Hello {kwargs['name']}, the answer is {sum}")
    elif"country" in keys:
        print(f"Hello from {kwargs['country']}, the answer is {sum}")
    elif not kwargs:
        print(f"Hello Annonymous the answer is {sum}")