class Car():
    def __init__(self, myColor, type, isUnlocked, myModel, myMake):
        self.make = myMake
        self.model = myModel
        self.color = myColor
        self.type = type
        self.numWheels = 4
        self.isUnlocked = isUnlocked

    def drive(self):
        print("Vroom vroom...")
    
    def paint(self, newColor):
        self.color = newColor


myCar = Car("Hyundai", "Ioniq", "Gray", "Electric", True)

myDreamCar = Car("Tesla", "Cybertruck", "Space Gray", "Electric", False)

print("My Car Make", myCar.make)
print("My Dream Car Make", myDreamCar.make)

myCar.drive()

myCar.paint("Blue")
print(myCar.color)
print(myDreamCar.color)

print(myCar.type)

