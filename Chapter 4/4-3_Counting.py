# 4-3

for value in range(0, 21):
  print(value)

# 4-4

milli = list(range(0, 1000001))
#for value in milli:
#  print(value)

# 4-5

print(max(milli))
print(min(milli))
print(sum(milli))

# 4-6
odds = [2*values+1 for values in range(1, 21)]
print(odds)

#4-7

multiples = [values*3 for values in range(4, 31)]
print(multiples)

#4-8

cubes = [values**3 for values in range(1, 11)]
print(cubes)

#4-9 same as 4-8

