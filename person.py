class Person:

    # constructor or initializer
    def __init__(self, name):
        self.name = name  # name is data field also commonly known as instance variables

    # method which returns a string
    def whoami(self):
        return "You are " + self.name


def main():
    p = Person("Tom")
    print(p.whoami())
    print(p.name)


if __name__ == "__main__":
    main()

