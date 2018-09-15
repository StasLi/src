class Vehicle:

    def __init__(self, n, c):
        self.__name = n  # __name is private to Vehicle class
        self.__color = c

    def getColor(self):  # getColor() function is accessible to class Car
        return self.__color

    def setColor(self, color):  # setColor is accessible outside the class
        self.__color = color

    def getName(self):  # getName() is accessible outside the class
        return self.__name


class Car(Vehicle):

    def __init__(self, nn, cc, mm):
        # call parent constructor to set name and color
        super().__init__(nn, cc)
        self.__model = mm

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"

    def getName(self):  # getName() is accessible outside the class
        return super().getName() + self.__model


def main():
    v = Vehicle("Toy", "grey")
    print(v.getName())

    x=Car("toyota", "blue", "XYZ")
    print(x.getName())

    print(type(x)== Vehicle)
    print(type(1)==int)

if __name__ == "__main__":
    main()