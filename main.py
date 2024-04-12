# Get the Nth row in a Pandas DataFrame

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'experience': [1, 3, 5, 7, 9],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

print(df)

print('-' * 50)

first_row = df.iloc[[0]]
print(first_row)

print('-' * 50)

second_row = df.iloc[[1]]
print(second_row)