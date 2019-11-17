myFirstList = ['something', 'something else']

for something in myFirstList:
    print(something)

mySecondList = []
for i in range(0, 100):
    mySecondList.append(i)

print(mySecondList)

#seriously? You can go backwards with lists in Python?
print(mySecondList[-1])

#so this would be like using a list as a queue, remember that pop without argument is the last item in the list
print(mySecondList[0])
print(mySecondList.pop(0))
print(mySecondList[0])
print(mySecondList[-1])