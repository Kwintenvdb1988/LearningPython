# the (object) is the same as extends in Java. It implies an "is-a" relationship
# this can be removed and simply writen as "class Person:" if object is the super


class Person(object):

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Hi, I'm ", self.name)


myself = Person("Kwinten")
myself.print_name()


# default arguments are a thing but not a singleton. It only gets initialised once and then reused.
def extend_list(val, list=[]):
    list.append(val)
    return list


list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)