#object oriented programming OOP
#OOP allows you to combine attributes and methods into an object to represent real world things

#object - a bundle of related attributes and methods
#class - a class is a blueprint for creating objects
#an object is an instance of a class

class Car:
    #first we need a constructor
    #a constructor is what is called when we first create an object from our class
    #used to initializa any necessary values.
    def __init__(self, model, year, color, for_sale):
        #"self" referse to the current instance of the object being created
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    #methods for the class
    def drive(self): #if you wish to access instance values, pass in self
        print(f"you drive the {self.color} {self.model}")

    def stop(self): #if you wish to access instance values, pass in self
        print(f"you drive the {self.color} {self.model}")

    def describe(self): #if you wish to access instance values, pass in self
        print(f"you drive the {self.color} {self.model}")
