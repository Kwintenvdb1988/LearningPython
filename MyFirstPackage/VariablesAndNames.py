this_is_a_number = 5
this_is_also_a_number = 10
print(this_is_a_number - this_is_also_a_number)
this_is_a_boolean = True
print(this_is_a_boolean)
this_is_a_string = "String here"
print(this_is_a_string)
can_i_declare_it_like_this = 'also a String'
print(can_i_declare_it_like_this, ' ', this_is_a_string)
print("Hey there %s" % "you")
print("this is another way of doing it %d %s" % (35, "something"))
print("also, we can use something with an r like this %r" % "something")
print("or this %r" % False)
print("this" * 10)
first = "first"
second = "second"
third = "third"
print(first, second, third),
print(first, second, third)

formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (formatter, formatter, formatter, formatter))
print("""
this works too
""")
print('''
and this
''')