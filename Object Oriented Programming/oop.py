class Car():
    make = "Hyundai"

    def __init__(self, myModel, myColor, type, isUnlocked, numWheels=4, mpg=None):
        self.model = myModel
        self.color = myColor
        self.type = type
        self.numWheels = numWheels
        self.isUnlocked = isUnlocked

        if numWheels == 2:
            self.body = "Motorcycle"
        else:
            self.body = "Car"

        self.mpg = mpg


    def drive(self):
        print("Vroom vroom...")
    
    def paint(self, newColor):
        self.color = newColor
    
    def checkEfficiency(self):
        if (self.mpg != None and self.mpg > 25) or self.type == "Electric":
            return True
        else:
            return False



carModel = input("What is the model? ")

myCar = Car(carModel, "Gray", "Electric", True)
myOtherCar = Car("Sonata", "Silver", "Gas", False, 2, 16)

print(myCar.checkEfficiency())
