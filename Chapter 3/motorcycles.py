motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0]='ducati'

# add item at the end

motorcycles.append('kawasaki')
print(motorcycles)
#initialization of the list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# insert at certain position

motorcycles.insert(2, 'ducati')
print(motorcycles)

# deletion

del motorcycles[0]
print(motorcycles)

# popping and using

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

# Example

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Pop by a position

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Remove by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# Example
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive} was too expensive for me.")
print(motorcycles)