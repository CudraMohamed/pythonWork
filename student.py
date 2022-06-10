class Student :
    # name = 'Effence'
    # age = 20
    # country = 'Kenya'
    school = 'AkiraChix'
    def __init__(self,first_name,second_name,age,country): #class attribute
        self.first_name=first_name                      #instance variables
        self.second_name=second_name
        self.age=age
        self.country=country

    def greeting(self):
        return f'Hello {self.first_name} {self.second_name}, from {self.country}, welcome to {self.school}'

    def full_name(self):
        return f'Hello, my full name is {self.first_name} {self.second_name}'

    def year_of_birth(self):
        birth_year= 2022 - self.age
        return f'Hello {self.first_name} {self.second_name},your year of birth is ',birth_year

    def initials(self):
        # return f'My name initials are {self.first_name[0],self.second_name[0]}'
        name_initials=f"{self.first_name[0]} {self.second_name[0]}"
        return name_initials.upper()