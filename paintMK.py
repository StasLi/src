import math
import abc


class Shape:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    @abc.abstractmethod
    def get_area(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_perimeter(self):
        raise NotImplementedError

    @abc.abstractmethod
    def is_inside(self, px, py):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, a, b, r):
        super().__init__(a, b)
        self.__radius = r

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return math.pi * (self.get_radius()**2)

    def get_perimeter(self):
        return 2 * math.pi * self.get_radius()

    def is_inside(self, px, py):
        # checking distance from point to center
        distance = math.sqrt((px-super().get_x())**2 + (py-super().get_y())**2)
        # checking if distance smaller than radius
        return distance <= self.get_radius()


class Rectangle(Shape):
    def __init__(self, a, b, h, w):
        super().__init__(a, b)
        self.__width = w
        self.__height = h

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_perimeter(self):
        return 2*(self.get_width() + self.get_height())

    def get_area(self):
        return self.get_width() * self.get_height()

    def is_inside(self, px, py):
        range_x = range(super().get_x(), super().get_x()+self.get_width()+1)
        range_y = range(super().get_y(), super().get_y()+self.get_height()+1)
        return (px in range_x) and (py in range_y)


class Square(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b, h, h)


class Line(Shape):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.__end_x = c
        self.__end_y = d
        self.__m = Line.__calc_slope(a, b, c, d)
        self.__b = Line.__calc_offset(a, b, self.__m)

    @staticmethod
    def __calc_slope(x1, y1, x2, y2):
        if x2 == x1:
            return 0
        return (y2 - y1) / (x2 - x1)

    @staticmethod
    def __calc_offset(x1, y1, m):
        return y1 - (m * x1)

    def get_end_x(self):
        return self.__end_x

    def get_end_y(self):
        return self.__end_y

    def get_perimeter(self):
        return 0

    def get_area(self):
        return 0

    def is_inside(self, px, py):
        # check if it's a vertical line: y=c
        if super().get_x() == self.get_end_x():
            if px != self.get_end_x():
                return False
        # check if point is on the line using the equation: y = mx+b
        elif py != (self.__m * px + self.__b):
            return False

        # check if given point is in the defined area of the initial points
        return (px >= min(super().get_x(), self.get_end_x())) \
               and (px <= max(super().get_x(), self.get_end_x())) \
               and (py >= min(super().get_y(), self.get_end_y())) \
               and (py <= max(super().get_y(), self.get_end_y()))


# ############################## TESTS ############################## #
def main():
    # check Line
    l1 = Line(1, 1, 3, 3)
    assert (l1.get_x() == 1), "Expected 1 but got " + str(l1.get_x())
    assert (l1.get_perimeter() == 0), "Expected 0 but got " + str(l1.get_perimeter())
    assert (l1.get_area() == 0), "Expected 0 but got " + str(l1.get_area())
    assert (l1.is_inside(2, 2)), "Expected 2,2 to be inside line"
    assert (l1.is_inside(1.23, 1.23)), "Expected 1.23,1.23 to be inside line"
    assert (not l1.is_inside(7, 2)), "Expected 7,2 to not be inside line"
    assert (not l1.is_inside(4, 4)), "Expected 4,4 to not be inside line"

    l2 = Line(1, 0, 3, 0)
    assert (l2.is_inside(2, 0)), "Expected 0,2 to be inside line"
    assert (l2.is_inside(1.23, 0)), "Expected 0.23,1.23 to be inside line"
    assert (not l2.is_inside(7, 2)), "Expected 7,2 to not be inside line"
    assert (not l2.is_inside(4, 4)), "Expected 4,4 to not be inside line"

    l3 = Line(0, 1, 0, 3)
    assert (l3.is_inside(0, 2)), "Expected 0,2 to be inside line"
    assert (l3.is_inside(0, 1.23)), "Expected 0,0.23 to be inside line"
    assert (not l3.is_inside(7, 2)), "Expected 7,2 to not be inside line"
    assert (not l3.is_inside(0, 4)), "Expected 0,4 to not be inside line"

    l4 = Line(8, 2, 8, 2)
    assert (l4.is_inside(8, 2)), "Expected 8,2 to be inside line"
    assert (not l4.is_inside(0, 0)), "Expected 0,0 to not be inside line"
    assert (not l4.is_inside(2, 8)), "Expected 2,8 to not be inside line"

    # check Circle
    c1 = Circle(1, 1, 5)
    assert (c1.get_radius() == 5), "Expected 5 but got " + str(c1.get_radius())
    assert (c1.get_perimeter() == (2*math.pi*5)), "Expected 10*pi but got " + str(c1.get_perimeter())
    assert (c1.get_area() == (math.pi*25)), "Expected 25*pi but got " + str(c1.get_area())
    assert (c1.is_inside(2, 2)), "Expected 2,2 to be inside circle"
    assert (not c1.is_inside(7, 2)), "Expected 7,2 to not be inside circle"
    assert (not c1.is_inside(3, 20)), "Expected 3,20 to not be inside circle"

    # check rectangle
    r1 = Rectangle(-10, 20, 100, 100)
    assert (r1.get_x() == -10), "Expected -10 but got " + str(r1.get_x())
    assert (r1.get_y() == 20), "Expected 20 but got " + str(r1.get_y())
    assert (r1.get_perimeter() == 400), "Expected 400 but got " + str(r1.get_perimeter())
    assert (r1.get_area() == 10_000), "Expected 10,000 but got " + str(r1.get_area())
    assert (r1.is_inside(50, 60)), "Expected 50, 60 to be inside rectangle"
    assert (not r1.is_inside(40, 0)), "Expected 40, 0 to not be inside rectangle"


if __name__ == "__main__":
    main()
