from car import Car
#create instance of a class (an object)
car1=Car("Mustang", 2024, "red", False) #object created
car2=Car("corvette", 2025, "blue", True)
car3=Car("charger", 2026, "yellow", True)

#each car has its own atributes. we can access them with dot notation
print(car1.model)
print(f"{car2.year} {car2.color} {car2.model}")

car1.drive()
car3.drive
