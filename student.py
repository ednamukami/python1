class Student:
    school="Akiachix"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def speak(self):
        return f"hello class, my name is {self.name}"
    
    def year_of_birth(self):
        return f"She was born on {2021-self.age}"
