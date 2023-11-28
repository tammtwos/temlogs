import temlogs
l = temlogs.Logger("test.txt")

com1 = input()
com2 = input()
com3 = input()

l.log(com1)
print("com1 done, check ur file.")
input()
l.log(com2)
print("com2 done, check ur file.")
input()
l.log(com3)
print("com3 done, check ur file.")
input()


