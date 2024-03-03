print("Q1")
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


my_vehicle = Vehicle(240, 18)
print(my_vehicle.max_speed, my_vehicle.mileage)

#Vehicle class without any variables and methods
class Vehicle2:
    pass

my_vehicle2 = Vehicle2()

print("Q2.1")
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

my_bus = Bus("School Volvo", 180, 12)

print("Vehicle Name:", my_bus.name)
print("Speed:", my_bus.max_speed, "Mileage:", my_bus.mileage)

print("Q2.2")
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

my_bus = Vehicle("School Volvo", 180, 12)

print(my_bus.seating_capacity())

print("Q3.1")
class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# create instances of Bus and Car
bus = Bus("School Bus", 120, 5000)
car = Car("Audi Q5", 240, 18000)

# print the color of each instance
print(f"{bus.color} {bus.name} Speed: {bus.max_speed} Mileage: {bus.mileage}")
print(f"{car.color} {car.name} Speed: {car.max_speed} Mileage: {car.mileage}")
print("Q3.2")
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.1
        final_amount = total_fare + maintenance_charge
        return final_amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

print("Q4.1")
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))
