import pandas as pd

# df = pd.read_excel(r"F:/mangshe/panda/体检数据.xlsx")
# df.loc[2, "体重"] = 1
# print(df)
# df.to_excel(r"F:/mangshe/panda/体检数据_修改.xlsx")
# # 以学号作为索引 单加一列
# df = pd.read_excel(r"F:/mangshe/panda/体检数据_修改.xlsx", index_col=0)

# with open(r"F:/mangshe/panda/体检数据.csv", "r", encoding="utf-8") as f:
#     print(f.read())
# df_csv = pd.read_csv(r"F:/mangshe/panda/体检数据.csv", index_col=0)
# print(df_csv)

# with open(r"F:/mangshe/panda/体检数据_sep.csv", "r", encoding="utf-8") as f:
#     print(f.read())
# df_csv = pd.read_csv(r"F:/mangshe/panda/体检数据_sep.csv", index_col=0, sep="=")
# print(df_csv)
#
# with open(r"F:/mangshe/panda/体检数据_sep.txt", "r", encoding="utf-8") as f:
#     print(f.read())
# df_txt = pd.read_csv(r"F:/mangshe/panda/体检数据_sep.txt", index_col=0, sep="=")
#
# df_txt.to_csv(r"F:/mangshe/panda/体检数据_sep_修改.csv")
# df_txt.to_excel(r"F:/mangshe/panda/体检数据_sep_修改.xlsx")
#
# print("读保存后的 csv")
# print(pd.read_csv(r"F:/mangshe/panda/体检数据_sep_修改.csv"))
#
# print("读保存后的 xlsx")
# print(pd.read_excel(r"F:/mangshe/panda/体检数据_sep_修改.xlsx"))

# 从剪贴板读取数据
df = pd.read_clipboard()
print(df)
