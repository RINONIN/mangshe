import pandas as pd
import numpy as np

# print(pd.Series([1, 2, 3]))

a_list = [1, 2, 3]
a_dict = {"a": 1, "b": 2, "c": 3}
print("list:", a_list)
print("dict:", a_dict)

a_array = np.array([
    [1, 2],
    [3, 4]
])
a_df = pd.DataFrame(
    {"a": [1, 3],
     "b": [2, 4],
     "c": [3, 6]}
)

print("numpy array:\n", a_array)
print("\npandas df:\n", a_df)
