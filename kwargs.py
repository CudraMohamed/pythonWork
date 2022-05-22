def greet_multiple(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

def greet_multiples(**kwargs):
    keys=kwargs.keys()
    if "Country" in keys:
        print(f"Hello {kwargs['name']} you are from {kwargs['Country']}")
    elif "age" in keys:
        year=2022-kwargs["age"]
        print (f"Hello {kwargs['name']} you were born in{year}")
    elif not kwargs:
        print("Hello Annonymous")
