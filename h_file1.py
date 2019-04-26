from random import randint

list = []

for i in range(10):
    a = randint(1,100)
    list.append(a)
print(list)

for i in list:
    print(i)

print("__________________-")
print(list[4])
print("____________")

for i in range(len(list)):
    print(list[i])