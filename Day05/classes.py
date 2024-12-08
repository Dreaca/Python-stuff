class Car:
    category = "motor vehicle" #class attribute

    def displayCategory(self):
        print(f"This is a {self.category}")
    
    def display(self):
        print("This is a ",self.model)
        print("Color: ",self.color)

    def update(self,model,color):
        self.model = model
        self.color = color
        print("Updated model : ",self.model)
        print("Updated Color : ",self.color)
    def __init__(self,model,color):
        self.model = model
        self.color = color

#new_car = Car()

#print(new_car.category) # accessing class attribute

#new_car.display() # accessing method attribute with instance object

car_2 = Car("Toyota","black")

car_2.display()
print("\n================================\n")
car_2.update("Tesla","red")

print(f"Printing {car_2.category}")