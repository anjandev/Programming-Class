# Problem S3: The Geneva Confection
# Senior Division


T = int(input("Enter the number of tests"))

cars = []

for carnum in range(T):
    car = int(input("Enter car #"))
    cars.append(car)
    
lake = []
branch = []

while len(cars) > 0:
    if len(lake) == 0 and car[0] == 1:
        lake.append(car[0])
        cars.remove(car[0])
    elif car[0] - 1 == lake[-1]:
        lake.append(car[0])
        cars.remove(car[0])
    
