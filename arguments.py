# def my_country(Country="Kenya"):
#     return f"Hello you are from {Country}"
def my_country(Country="Kenya",Student="Susan"):
    return f"Hello {Student} you are from {Country}"

def greet_multiple(*names):
    print(names)

def greet_multiple2(*names):
 for name in names:
    print(f"Hello {names}")
