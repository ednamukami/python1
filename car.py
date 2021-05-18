class Car:

    def __init__(self,make,model):
        self.make=make
        self.model=model

    def porche(self):
        return f"The new {self.model} is one of the fastest cars"

    def make(self):
        return f"The one of most famous porsche brands is {self.make}"