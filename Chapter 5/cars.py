cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())

car = 'bmw'
check = (car=='bmw')
print(check)

car = 'bmw'
check = (car=='audi')
print(check)