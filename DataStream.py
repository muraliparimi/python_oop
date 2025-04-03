class DataStream:
    def __init__(self, data):
        self.data = data

    def project_data(self, keys):
        projected_data = [{key: d.get(key, None) for key in keys} for d in self.data]
        return DataStream(projected_data)  # Return a new DataStream object for chaining

    def filter_data(self, test_func):
        filtered_data = list(filter(test_func, self.data))
        return DataStream(filtered_data)  # Return a new DataStream object for chaining

    def aggregate_data(self, key, agg_func):
        values = [d.get(key, None) for d in self.data]
        return agg_func(values)

# Example usage
ds = DataStream([
    {'name': 'Alice', 'age': 25, 'profession': 'Engineer', 'salary': 70000},
    {'name': 'Bob', 'age': 30, 'profession': 'Doctor', 'salary': 120000},
    {'name': 'Carol', 'age': 35, 'profession': 'Artist', 'salary': 50000},
    {'name': 'David', 'age': 40, 'profession': 'Engineer', 'salary': 90000},
])

# Step 1: Project the data to include only 'name', 'age', and 'salary'
projected_ds = ds.project_data(['name', 'age', 'salary'])

# Step 2: Filter the projected data to include only those with age > 30
filtered_ds = projected_ds.filter_data(lambda x: x['age'] > 30)

# Step 3: Aggregate the filtered data to compute the average salary
average_salary = filtered_ds.aggregate_data('salary', lambda salaries: sum(salaries) / len(salaries))
print(average_salary)  # Outputs: 70000.0

# Another version without returning objects of DataStream type

# Define the DataStream class with methods for data manipulation
# class DataStream:
#     def __init__(self, data):
#         self.data = data

#     def project_data(self, keys):
#         return [{key: item.get(key, None) for key in keys} for item in self.data]

#     def filter_by_department(self, department):
#         return [item for item in self.data if item['department'] == department]

#     def calculate_average_salary(self):
#         return sum(item['salary'] for item in self.data) / len(self.data)

# # Sample dataset of employees
# employees = DataStream([
#     {'name': 'Alice', 'department': 'Sales', 'age': 27, 'salary': 56000},
#     {'name': 'Bob', 'department': 'R&D', 'age': 45, 'salary': 108000},
#     {'name': 'Eve', 'department': 'Sales', 'age': 33, 'salary': 68000},
# ])

# # TODO: Create a DataStream object with employees filtered by the Sales department
# print(employees.filter_by_department('Sales'))
# sales = DataStream(employees.filter_by_department('Sales'))
# #print(sales.data)
# # TODO: Project the 'salary' information from the filtered data
# salary = DataStream(sales.project_data(['salary']))

# # TODO: Calculate the average salary of employees in the Sales department
# avg_salary = salary.calculate_average_salary()
# # TODO: Print the average salary in Sales department
# print(avg_salary)