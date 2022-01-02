import pandas as pd

df = pd.read_excel(r"F:\mangshe\panda\课表.xlsx")
print(df)

# df.loc[2, "体重"] = 50
# print(df)
# df.to_excel(r"F:\mangshe\panda\课表.xlsx")

# df_csv = pd.read_csv(r"F:\mangshe\panda\课表.csv", index_col=0)
# print(df_csv)

with open(r"F:\mangshe\panda\课表_sep.csv", "r", encoding="utf-8") as f:
    print(f.read())

df_csv = pd.read_csv(r"F:\mangshe\panda\课表_sep.csv", index_col=0, sep="=")
print(df_csv)

with open(r"F:\mangshe\panda\课表.txt", "r", encoding="utf-8") as f:
    print(f.read())
df_txt = pd.read_csv(r"F:\mangshe\panda\课表.txt", index_col=0, sep="=")
print(df_txt)

# df_txt.to_csv(r"F:\mangshe\panda\课表_修改.csv")
# df_txt.to_excel(r"F:\mangshe\panda\课表_修改.xlsx")
#
# print("读保存后的 csv")
# print(pd.read_csv(r"F:\mangshe\panda\课表_修改.csv"))
#
# print("读保存后的 xlsx")
# print(pd.read_excel(r"F:\mangshe\panda\课表_修改.xlsx"))
