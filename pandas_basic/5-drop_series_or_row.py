import pandas as pd

filename = 'olympics_1896_2004.csv'
oo = pd.read_csv(filename, skiprows=5)
print(oo.head(3))
#  Year      City       Sport  Discipline                 Athlete Name  NOC Gender       Event Event Gender   Medal  Position
# 15763  1980    Moscow  Basketball  Basketball  BARISHEVA-KOROSTELEVA, Olga  URS  Women  basketball            W    Gold         1
# 22397  1996   Atlanta    Football    Football                    LIU, Ying  CHN  Women    football            W  Silver         2
# 14815  1976  Montreal      Hockey      Hockey          MAISTER, Barry John  NZL    Men      hockey            M    Gold         1

# drop a column by name, columns are axis=1
print(oo.drop('Position', axis=1))

print(pd.read_csv(filename, skiprows=5).sample(3).drop('Position', axis=1))


oo = (pd.read_csv(filename, skiprows=5)
      .drop('Position', axis=1) # seperate line for debugging (comment this line to see the output of the previous line)
)
print(oo.sample(3))

# better not use inplace=ture, because:
#   - it modifies the original DataFrame, which may not be what you want
#   - not possible to chain method calls, because it returns None
#   - some methods do not have inplace parameter, like merge, join, concat, pivot_table, groupby, etc.

# drop rows by index, rows are axis=0
oo = (pd.read_csv(filename, skiprows=5)
      .drop([0, 2], axis=0) 
)
print(oo.head(3))

# drop clumns by name, columns are axis=1
oo = (pd.read_csv(filename, skiprows=5)
      .drop(['Position', 'Event Gender'], axis=1)
)
print(oo.head(3))