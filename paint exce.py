
import math


class shape:
    def __init__(self, x, y, p1, p2):
        self._CenterX = x
        self._CenterY = y
        self._PointX = p1
        self._PointY = p2

    def getCenterX(self):
        return self._CenterX

    def getCenterY(self):
        return self._CenterY

    def getPointX(self):
        return self._PointX

    def getPointY(self):
        return self._PointY


class circle(shape):
    def __init__(self, a, b, p1, p2, r):
        super().__init__(a, b, p1, p2)
        self._Radius = r

    def getCircleArea(self):
        return math.pi*(self._Radius**2)

    def getCirclePerimeter(self):
        return 2 * math.pi * self._Radius

    def checkPoint(self):
        #checking distance from point to center
        distance = math.sqrt(((super().getPointX()-super().getCenterX())**2)+((super().getPointY()-super().getCenterY()**2)))
        #checking if distance smaller than radius

        return distance <= self._Radius


class Rectangle(shape):
    def __init__(self, a, b, p1, p2, h, w):
        super().__init__(a, b, p1, p2)
        self._Width = w
        self._Height = h
    def getRecPerimeter(self):
        return(2*(self._Width+self._Height))
    def getRecArea(self):
        return (self._Width*self._Height)

    def checkPoint(self):
        rangeX = range(super().getCenterX(), super().getCenterX()+self._Width+1)
        rangeY = range(super().getCenterY(), super().getCenterY()+self._Height+1)
        return (super().getPointX() in rangeX) and (super().getPointY() in rangeY)




class Square(shape):
    def __init__(self, a, b, p1, p2, h):
        super().__init__(a, b, p1, p2)
        self._Height = h
    def getSquareArea(self):
        return self._Height**2
    def getSquarePerimeter(self):
        return self._Height*4

    def checkPoint(self):
        rangeX = range(super().getCenterX(), super().getCenterX() + self._Height+1)
        rangeY = range(super().getCenterY(), super().getCenterY() + self._Height+1)
        return (super().getPointX() in rangeX) and (super().getPointY() in rangeY)

class line(shape):
    def __init__(self, a, b, p1, p2, c, d):
        super().__init__(a, b, p1, p2)
        self.__EndX = c
        self.__EndY = d
        #self._StartX = a
        #self._StartY=b

    #LineLegth = 0
    def getLineLength(self):
       # global LineLength
        LineLength = math.sqrt(((self.__EndX -super().getCenterX())**2)+((self.__EndY-super().getCenterY())**2))
        return LineLength
    def checkPoint(self):
        #checking if point lie in range of my x and y
        if (super().getPointY() in range(super().getCenterY(),(self.__EndY)+1)) and (super().getPointX() in range(super().getCenterY(),(self.__EndX)+1)):
            #checking if line parallel to Y (division by zero),if its true checking pointX on same axis and return true
            if super().getCenterX()== self.__EndX == super().getPointX():
                return True
            else:


                #y=mx+k , m = (y1-y2)/(x1-x2)
                m = (self.__EndY - super().getCenterY())/(self.__EndX - super().getCenterX())
                #k= y - mx
                k = self.__EndY - m*self.__EndX
                #check if equation is true
                return (super().getPointY() == m * super().getPointX() + k)
        else:
            return False









def main():
    firstLine = line(0,0,3,0,5,0)
    print("line length =",firstLine.getLineLength())
    print("Point is on the line = ",firstLine.checkPoint())
    print(".......................................................")
    firstCircle = circle(1, 1,5,1,5)
    print ("Circle Area =", firstCircle.getCircleArea())
    print("Circle perimeter = ", firstCircle.getCirclePerimeter())
    print("Point is in the Circle = ", firstCircle.checkPoint())
    print(".......................................................")


    firstRectangle = Rectangle (1,1,2,2,3,3)
    print ("Rectangle area = ", firstRectangle.getRecArea())
    print("Rectangle Perimeter = ", firstRectangle.getRecPerimeter())
    print ("point is in the area=",firstRectangle.checkPoint())
    print(".......................................................")

    firstSquare = Square (1,1,2,5,5)
    print("Square area=", firstSquare.getSquareArea())
    print("Square perimeter=", firstSquare.getSquarePerimeter())
    print("point is in the area=",firstSquare.checkPoint())
    print(".......................................................")




if __name__ == "__main__":
     main()

