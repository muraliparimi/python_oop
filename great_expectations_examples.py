

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", None],
    "age": [25, 30, 35, 40],
    "email": ["alice@example.com", "bob@example.com", "charlie@example.com", None]
}
df = pd.DataFrame(data)

# Now, we'll write a Great Expectations-style unit test to check:

# name and email should not be null.
# age should be between 18 and 60.
# email should match a regex pattern.

from great_expectations.dataset import PandasDataset

class MyDataSet(PandasDataset):
    pass

df_ge = MyDataSet(df)

assert df_ge.expect_column_values_to_not_be_null("name")["success"] == False
assert df_ge.expect_column_values_to_be_between("age", min_value=18, max_value=60)["success"] == True
assert df_ge.expect_column_values_to_match_regex("email", r".+@.+\..+")["success"] == False