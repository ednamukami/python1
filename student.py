class Student:
    school="Akiachix"
    def __init__(self,first_name,last_name,age,initials,year_of_birth):
        
        self.age=age
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.year_of_birth=year_of_birth
        self.intials=initials

    def greet (self):
        return  f"hello my name is {self.first_name} {self.last_name}"  
    def year_of_birth(self):
        return

    def initials (self):
        return f"{self.first_name[0]} {self.last_name[0]}"

    