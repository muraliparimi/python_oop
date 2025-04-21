import numpy as np
from scipy import stats
import pandas as pd
from sklearn.preprocessing import StandardScaler
from datetime import datetime


# arr1D = np.array([1, 2, 3, 4, 5]
# print(f"Our first 1D array: {arr1D}"
# zeros = np.zeros(5
# print(zeros
# ones = np.ones(5
# print(ones
# sequence = np.arange(0,10,1)
# print(sequence
# sales_month1 = np.array([120, 150, 90])
# sales_month2 = np.array([130, 160, 80])
# total_sales = sales_month1 + sales_month2
# print(total_sales
# prices = np.array([20, 30, 50])
# quantities = np.array([100, 200, 150]
# total_prices = prices * quantities
# total_price = np.dot(prices, quantities)
# print(total_price
# arr_multi = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr_multi)
# print(arr_multi[1,1])

# print(arr_multi[:3, :3])
# print(arr_multi.shape)
# new_arr = arr_multi.reshape(3,2)
# print(new_arr)

# data = np.array([12, 43, 36, 32, 51, 18, 79, 7, 7])
# print(data[(data>30) & (data <40)])
# print(f"mean: {data.mean()}, mean_with_np: {np.mean(data)}, median: {np.median(data)}, mode: {stats.mode(data)[0]}, variance: {np.var(data)} and standard deviation: {np.std(data)}")

# import pandas as pd

# data_list = ["apple", "banana", "kiwi"]

# df = pd.DataFrame(data_list, columns=['Fruit'])

# print(df.shape)
# data_dict = {'Fruit': ['apple', 'banana', 'cherry'], 'Count': [10, 20, 15]}
# df = pd.DataFrame(data_dict)


# data2 = {'Fruit': [10, 'date'], 'Count': [15, 25]}
# df2 = pd.DataFrame(data2)
# combined_df = pd.concat([df, df2], ignore_index=True)
# print(combined_df)

#print(pd.Series(["apples", "banana", "kiwi"]
#df = pd.DataFrame({
#  "Name": ["Alice", "Bob", "John"],
#  "Age": [25, 22, 30],
#  "City": ["New York", "Los Angeles", "Chicago"]
#})
#print(df)
#df.set_index("Name", inplace=Tru
#print(d
#df.reset_index(inplace=True)
#print(d
#Rename colum
#df.rename(columns={"Name": "Student_Name", "Age": "Student_Age"}, inplace=True)
#print(f"after changing names: {df}
#print(df.iloc[[0,2],2
#Filteri
#data = {
#    'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
#    'age': [12, 13, 14, 13, 12],
#    'grade_level': [6, 7, 8, 7, 6]
#
#students_df = pd.DataFrame(dat
# Filter 7th grade studen
#grade_seven_students = students_df[students_df["grade_level"] == 
# print(grade_seven_student
# Boolean Series for 7th grade
# s_grade_seven = students_df['grade_level'] ==
# print(is_grade_seve
# print(students_df[is_grade_seven
# Mutliple conditio
#grade_senv_and_older = students_df[(students_df["age"] == 13) & (students_df['grade_level'] == 7)]
# print(grade_senv_and_olde
# Older than 
#older_students = students_df[students_df["age"] > 1
#  print(older_student
# is_in usa
# middle_school_students = students_df[students_df['grade_level'].isin([6, 7])]
# print(middle_school_student
# Analys
# data =  {'Name': ['Tommy', 'Rex', 'Bella', 'Charlie', 'Lucy', 'Cooper'],
#          'Type': ['Dog', 'Dog', 'Cat', 'Cat', 'Dog', 'Bird']}
# pets_df = pd.DataFrame(data)

# print(pets_df['Type'].value_counts())
# print(pets_df.describe())

# Grouping and Aggregating with `groupby()` and `agg()` methods

# data =  {'Name': ['Tommy', 'Rex', 'Bella', 'Charlie', 'Lucy', 'Cooper'],
#          'Type': ['Dog', 'Dog', 'Cat', 'Cat', 'Dog', 'Bird'],
#          'Weight': [12, 15, 8, 9, 14, 1]}

# pets_df = pd.DataFrame(data)

# print(pets_df.groupby('Type').agg({'Weight': 'mean'}))

# print(pets_df.sort_values('Weight'))


# grades = pd.DataFrame({'Student': ['Alex', 'Tina', 'John', 'Lily'],
#                        'Math': [78, 82, None, 90],
#                        'Science': [87, None, 93, 88]})

# # Fill NaN values with a constant value, 60 in this case
# grades_filled = grades.fillna(60)
# print(grades_filled)


# Detecting and Filtering Outliers
# Scanning for outliers, or exceptional values, is the next step. Outliers can distort the analytical outcome. One common method to detect outliers is using the Interquartile Range (IQR).
# As a short reminder, IQR method suggests that any value below 
# Q1 − 1.5⋅IQR  and above Q3 + 1.5 IQR  are considered outliers
# Where:
# Q1 – The first quartile
# Q3 – The third quartile
# IQR – The Interquartile Range
# Let's use the IQR method to identify and filter out outliers in a dataset.

# A dataset with an outlier
# data = [1, 1.2, 1.1, 1.05, 1.5, 1.4, 9]
# df = pd.DataFrame(data, columns=['Values'])

# Q1 = df['Values'].quantile(.25)
# Q3 = df['Values'].quantile(.75)
# IQR = Q3 - Q1
# print(IQR)

# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# # FIlter out outliers
# df_1 = df[(df['Values'] >= lower_bound) & (df['Values'] <= upper_bound)]
# print(df_1)

# Transformations

# data = {'Feature1': [0.5, 0.6, 0.9], 'Feature2': [10, 12, 15]}
# df = pd.DataFrame(data)

# scaler = StandardScaler()

# Scaling just 'Feature2'
# df['Feature2_scaled'] = scaler.fit_transform(df[['Feature2']])
# print(f"sclaer: {scaler}")
# print(df)


# sizes = ['small', 'Large', 'medium', 'sm', 'lg', 'S', 'l', 'M']
# df = pd.DataFrame(sizes, columns = ['TShirtSize'])

# size_replacements = {'sm': 'small', 'S': 'small', 'lg': 'large', 'Large': 'large', 'l': 'large', 'm': 'medium', 'M': 'medium'}
# df['TShirtSize'] = df['TShirtSize'].replace(size_replacements)
# print(df['TShirtSize'].value_counts())

# prices = [19.99, 25.99, 22.50, 27.99, 250.00, 23.49, 19.45]
# df = pd.DataFrame(prices, columns=['Price'])
# Q1, Q3 = df['Price'].quantile([.25, .75])
# IQR = Q3 - Q1
# lowerbound = Q1 - 1.5*IQR
# upperbound = Q3 + 1.5*IQR
# df = df[(df['Price'] >= lowerbound) & (df['Price'] <= upperbound)]
# print(df)

# students = pd.DataFrame({
#     'student_id': [1, 2, 3],
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'age': [15, 16, 17]
# })


# performance = pd.DataFrame({
#     'student_id': [1, 3, 4],
#     'grade': ['A', 'B', 'A'],
#     'attendance': [95, 85, 100]
# })

# students_merged = pd.merge(students, performance, on='student_id', how= 'outer')

# print(students_merged)

# data = {
#     'Representative': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie'],
#     'Region': ['East', 'West', 'West', 'East', 'East', 'West'],
#     'Sales': [150, 200, 100, 250, 175, 300]
# }

# df = pd.DataFrame(data)

# grouped = df.groupby('Representative')

# total_sales = grouped['Sales'].sum()

# print(total_sales)

# Correlations

# data = {
#     'Price': [300000, 450000, 200000, 350000, 500000],
#     'Size': [1500, 2000, 1000, 1700, 2200],
#     'Bedrooms': [3, 4, 2, 3, 4],
#     'Age': [20, 15, 40, 10, 5]
# }

# houses = pd.DataFrame(data)

# houses_corr = houses.corr()

# print(houses_corr)


# import seaborn as sns

# # Load Titanic dataset
# titanic = sns.load_dataset('titanic')

# # TODO: one-hot encode the 'embarked' column and add the new columns to the titanic DataFrame
# titanic_onehot_embarked = pd.get_dummies(titanic['embarked'], prefix='origin')
# titanic = pd.concat([titanic, titanic_onehot_embarked], axis=1)

# print(titanic.head())


# Dates and times in pandas

# data = {
#     'order_date': ['2023-10-01', '2023-10-02','10/02/2023', 'October 3 2023', '2023.10.04']
# }

# sales = pd.DataFrame(data)

# print(sales['order_date'])

# sales['order_date'] = pd.to_datetime(sales['order_date'], format='mixed')
# print(sales['order_date'])

# $ With a column in datetime format, we can extract components like the year, month, or day using the ".dt" accessor. Here’s how to extract the year, month, and day:
# sales['year'] = sales['order_date'].dt.year
# sales['month'] = sales['order_date'].dt.month
# sales['date'] = sales['order_date'].dt.day
# sales['day_of_week'] = sales['order_date'].dt.day_of_week
# sales['week_day'] = sales['order_date'].dt.weekday
# sales['time_since_order'] = datetime.now() - sales['order_date']

# sales['order_rank'] = sales['order_date'].rank(method='min')
#  method='min' skips one rank
# method='max' skips one rank
# print(sales)

# sorted_sales = sales.sort_values(by='order_date')
# print(sorted_sales)

# Pivot tables

# A pivot table allows us to summarize data by grouping it in a way that makes it easier to extract meaningful insights. Think of it like organizing toys in a toy store. Instead of having all toys mixed up, you sort them by category and then further by different attributes. Pivot tables help us do something similar with our data.

# The Pandas library provides a function called pivot_table() that makes creating pivot tables in Python straightforward. One reason pivot tables are so useful is that they allow us to easily perform aggregate functions like mean, sum, and count on data.

# Here are the important parameters of the pivot_table() function:

# index: The column(s) to group by, like aisles in a store.
# columns: The column whose distinct values will form the columns of the pivot table.
# values: The columns containing the data you want to aggregate, like toy prices.
# aggfunc: The function used to aggregate the data (e.g., mean or sum).

# data = {
#     'Product': ['Toy', 'Toy', 'Book', 'Book', 'Electronic'],
#     'Category': ['A', 'B', 'A', 'B', 'A'],
#     'Price': [10, 15, 7, 12, 100]
# }
# df = pd.DataFrame(data)

# pivot_table = df.pivot_table(index='Product', values='Price', aggfunc='mean')
# print(pivot_table)


# data = {
#     'student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
#     'subject': ['Math', 'Math', 'Math', 'English', 'English', 'English'],
#     'score': [85, 90, 95, 88, 93, 97]
# }

# df = pd.DataFrame(data)

# grouped = df.groupby(df['student'])['score'].mean()
# print(grouped)

# Load Titanic dataset
# titanic = sns.load_dataset('titanic')

# Load Titanic dataset
# titanic = sns.load_dataset('titanic')

# Complex groupby operation
# grouped = titanic.groupby(['class', 'sex'], observed=True).agg({
#     'fare': ['mean', 'max'],
#     'age': ['mean', 'count']
# })

# print(grouped)

