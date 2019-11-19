class Person(object):

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Hi, I'm ", self.name)


myself = Person("Kwinten")
myself.print_name()