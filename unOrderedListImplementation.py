from unOrderedList import unOrderedList

mylist = unOrderedList()

mylist.addItem(31)
mylist.addItem(77)
mylist.addItem(17)
mylist.addItem(93)
mylist.addItem(26)
mylist.addItem(54)

print(mylist.listSize())
print(mylist.listSearch(93))
print(mylist.listSearch(100))

mylist.addItem(100)
print(mylist.listSearch(100))
print(mylist.listSize())

mylist.listRemove(54)
print(mylist.listSize())
mylist.listRemove(93)
print(mylist.listSize())
mylist.listRemove(31)
print(mylist.listSize())
print(mylist.listSearch(93))

