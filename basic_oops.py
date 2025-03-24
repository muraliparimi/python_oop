class Dog: # type: ignore
    species = 'mammal'

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __repr__(self):
        return f"I am a dog named {self.name} and I am {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def birthday(self):
        self.age +=1

    
if __name__ == '__main__':
    philo = Dog("Phile", 3)
    mikey = Dog("Mikey", 4)



# Inheritance

class Person:
    description = "General Person"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old")
    
    def eat(self, food):
        print(f"{self.name} eats {food}")
    
    def action(self):
        print(f"{self.name} jumps")



# Inherited class from Person class
class Baby(Person):
    description = "baby"

    def speak(self):
        print("ba ba ba")

    def nap(self):
        print("sleeping")


class Person1:
    def __init__(self, first_nm, last_nm):
        self.first_nm = first_nm
        self.last_nm = last_nm
    @property
    def full_name(self):
        return f"{self.first_nm} {self.last_nm}"
    

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <=0:
            raise ValueError("Radius must be positive number")
        self._radius = value


# Class methods

class Vehicle():
    @classmethod
    def water_vehicle(cls, name, dimensions):
        vehicle = Vehicle()
        vehicle.name = name
        vehicle.dimensions = dimensions
        vehicle.floats = True
        vehicle.num_wheels = 0
        return vehicle
    
    def road_vehicle(cls, name, dimensions, num_wheels):
        vehicle = Vehicle()
        vehicle.name = name
        vehicle.dimensions = dimensions
        vehicle.floats = False
        vehicle.num_wheels = num_wheels
        return vehicle
    
    def volume(self):
        return self.dimensions[0] * self.dimensions[1] * self.dimensions[2]
    
    @staticmethod
    def all_float(*vehicles):
        for vehicle in vehicles:
            if not vehicle.floats:
                return False
        return True
    
boat = Vehicle.water_vehicle("Minnow", (30,40,10))
print(boat.name)