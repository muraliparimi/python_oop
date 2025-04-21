from dataclasses import dataclass, field
from typing import Any

@dataclass
class EmployeeRow:
    name: str
    id: int
    title: str

    @classmethod
    def from_raw(cls, row: list[Any]) -> "EmployeeRow":
        def clean(val):
            if isinstance(val, str):
                return val.strip().lower().replace(" ", "_")
            return val
        
        try:
            obj = cls(
                name = clean(row[0]),
                id = int(row[1]),
                title=clean(str(row[2]))
            )
            obj.validate()
            return obj
        except Exception as e:
            print(f"Row parse failed: {row} ({e})")
            return None
        
    def validate(self):
        for field_info in fields(self):
            field_name = field_info.name
            field_type = field_info.type
            value = getattr(self, field_name)

            if not isinstance(value, field_type):
                raise TypeError(f"Field '{field_name}' expected {field_type}, got {type(value)}: {value}")

    
    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "title": self.title
        }
    

if __name__ == '__main__':
    raw = [" John Doe ", 123, int(12)]
    employee = EmployeeRow.from_raw(raw)

    print(employee.to_dict())