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