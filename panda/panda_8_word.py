"""
作者：RINO
日期: 2022年03月21日
时间: 08:49
"""

# 格式化字符
# str.upper(); str.lower(); str.len()
# str.strip(); str.lstrip(); str.rstrip()
# str.split()
import pandas as pd

# py_s = "A,B,C,Aaba,Baca,CABA,dog,cat"
# pd_s = pd.Series(
#     ["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"],
#     dtype="string")

# print("python:\n", py_s.upper())
# print("\npandas:\n", pd_s.str.upper())

# 注意如果要用到 Pandas 丰富的文字处理功能，你要确保 Series 或者 DataFrame 的 dtype="string"
# pd_not_s = pd.Series(
#     ["A", "B", "C", "Aaba", "Baca", "CABA", "dog", "cat"],
# )
# print("pd_not_s type:", pd_not_s.dtype)
# pd_s = pd_not_s.astype("string")
# print("pd_s type:", pd_s.dtype)

# print("python lower:\n", py_s.lower())
# print("\npandas lower:\n", pd_s.str.lower())
# print("python len:\n", [len(s) for s in py_s.split(",")])
# print("\npandas len:\n", pd_s.str.len())

# py_s = ["   jack", "jill ", "    jesse    ", "frank"]
# pd_s = pd.Series(py_s, dtype="string")
# print("python strip:\n", [s.strip() for s in py_s])
# print("\npandas strip:\n", pd_s.str.strip())
#
# print("\n\npython lstrip:\n", [s.lstrip() for s in py_s])
# print("\npandas lstrip:\n", pd_s.str.lstrip())
#
# print("\n\npython rstrip:\n", [s.rstrip() for s in py_s])
# print("\npandas rstrip:\n", pd_s.str.rstrip())
#
# py_s = ["a_b_c", "jill_jesse", "frank"]
# pd_s = pd.Series(py_s, dtype="string")
# print("python split:\n", [s.split("_") for s in py_s])
# print("\npandas split:\n", pd_s.str.split("_"))
# print("\npandas split:\n", pd_s.str.split("_", expand=True))
#
# pd_df = pd.DataFrame([["a", "b"], ["C", "D"]])
# print(pd_df)
# print(pd_df.iloc[0, :].str.upper())
# 正则方案
# str.contains(); str.match(); str.startswith(); str.endswith()
# str.replace()
# str.extract(); str.extractall()

# pattern = r"[0-9][a-z]"
# s = pd.Series(["1", "1a", "11c", "abc"], dtype="string")
# print(s.str.contains(pattern))
# pattern = r"[0-9]+?[a-z]"
# s.str.match(pattern)
#
# py_s = ["1", "1a", "21c", "abc"]
# pd_s = pd.Series(py_s, dtype="string")
# print("py_s startswith '1':\n", [s.startswith("1") for s in py_s])
# print("\npy_s endswith 'c':\n", [s.endswith("c") for s in py_s])
#
# print("\n\npd_s startswith '1':\n", pd_s.str.startswith("1"))
# print("\npd_s endswith 'c':\n", pd_s.str.endswith("c"))
#
# py_s = ["1", "1a", "21c", "abc"]
# pd_s = pd.Series(py_s, dtype="string")
# print("py_s replace '1' -> '9':\n", [s.replace("1", "9") for s in py_s])
#
# print("\n\npd_s replace '1' -> '9':\n", pd_s.str.replace("1", "9"))
#
# print("pd_s replace -> 'NUM':")
# pd_s.str.replace(r"[0-9]", "NUM", regex=True)
#
# s = pd.Series(['a1', 'b2', 'c3'])
# s.str.extract(r"([ab])(\d)")

# 拼接
# str.cat()
# 格式化字符
s1 = pd.Series(["A", "B", "C", "D"], dtype="string")
s2 = pd.Series(["1", "2", "3", "4"], dtype="string")
print(s1.str.cat(s2))
