# Employee.py

from datetime import datetime
class Employee:
    company = "Pavel Inc"

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
    
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = datetime.fromisoformat(value)

    def compute_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        birthday = datetime(today.year, self.birth_date.month, self.birth_date.day)

        if today < birthday:
            age -=1
        return age
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def __str__(self):
        return f"{self.name} is {self.compute_age()} years old."
    
    def __repr__(self):
        return (
            "Employee("
            f"""name="{self.name}", """
            f"""birth_date="{self.birth_date.strftime('%Y-%m-%d')}")"""
        )
    

print(Employee.company)

employee1 = Employee("Chad", '1986-06-15')
print(employee1)
employee1

data = {
    "name" : "Jennifer",
    "birth_date" : "1990-08-02"
}

Jen = Employee.from_dict(data)
print(Jen)
Jen