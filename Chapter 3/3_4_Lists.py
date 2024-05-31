# 3-4

list = ['Einstein', 'Stalin', 'Lenin']
print(list[0])
print(list[1])
print(list[2])

# 3-5
print(f"{list[0]} can not make it to the dinner")
list[0] = 'Putin'
print(list[0])
print(list[1])
print(list[2])

# 3-6
print("Bigger table is found!")
list.insert(0, 'Masyana')
list.insert(2, 'Arnold')
list.append("Lincoln")
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])

# 3-7
removed_one = list.pop()
print(f"{removed_one} get out!")
removed_one = list.pop()
print(f"{removed_one} get out!")
removed_one = list.pop()
print(f"{removed_one} get out!")
removed_one = list.pop()
print(f"{removed_one} get out!")

del list[0]
del list[0]

print(list)
