class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, number):
        if number != self.data:
            if number > self.data:
                if not self.right:
                    self.right = Node(number)
                else:
                    self.right.add(number)
            else:
                if not self.left:
                    self.left = Node(number)
                else:
                    self.left.add(number)
        else:
            self.data = number

    def print(self):
        if self.left:
            self.left.print()

        print(self.data)

        if self.right:
            self.right.print()

    def find(self, number):
        if number == self.data:
            print('1self.data=', self.data)
            print('1self.right=', self.right)
            print('1self.left=', self.left)
            return True
        elif number > self.data and self.right:
            print('2self.data=', self)
            print('2self.right=', self.right)
            print('2self.left=', self.left)
            return self.right.find(number)
        elif number < self.data and self.left:
            print('3self.data=', self)
            print('3self.right=', self.right)
            print('3self.left=', self.left)
            return self.left.find(number)
        else:
            print('4self.data=', self)
            print('4self.right=', self.right)
            print('4self.left=', self.left)
            return False

    def __str__(self):
        return str(self.data)

    def remove (self,number):
        if number == self.data:
            self.data = self.right




def main():
    root = Node(22)
    root.add(10)
    root.add(27)
    root.add(16)
    root.print()
    print(root.find(10))
    print(root.find(101))


if __name__ == "__main__":
    main()
