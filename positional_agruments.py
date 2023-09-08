def add(*args):
    sum = 0
    for numb in args:
        sum += numb
    print(sum)
    print(args)

add(3,5,6,1,4,6)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
my_car = Car( make = "Nissan", seats = "4")

print(my_car.seats)
