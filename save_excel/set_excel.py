import pandas as pd

# 读取Excel表格1和表格2
df1 = pd.read_excel('C:/Users/86185/Desktop/表格1.xlsx')
df2 = pd.read_excel('C:/Users/86185/Desktop/表格2.xlsx')

# 使用merge函数将两个表格匹配，根据相同的列进行匹配
df3 = pd.merge(df1, df2, on=list(df1.columns), how='inner')

# 将结果保存到Excel表格3
df3.to_excel('C:/Users/86185/Desktop/表格3.xlsx', index=False)