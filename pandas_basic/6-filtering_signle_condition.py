import pandas as pd

filename = 'olympics_1896_2004.csv'
oo = pd.read_csv(filename, skiprows=5)
print(oo.head(3))
#  Year      City       Sport  Discipline                 Athlete Name  NOC Gender       Event Event Gender   Medal  Position
# 15763  1980    Moscow  Basketball  Basketball  BARISHEVA-KOROSTELEVA, Olga  URS  Women  basketball            W    Gold         1
# 22397  1996   Atlanta    Football    Football                    LIU, Ying  CHN  Women    football            W  Silver         2
# 14815  1976  Montreal      Hockey      Hockey          MAISTER, Barry John  NZL    Men      hockey            M    Gold         1
print(oo.shape)
# (27174, 11)

oo_of_1896 = oo[oo.Year == 1896] 
# oo_of_1896 = oo[oo['Year'] == 1896] 
# oo_of_1896 = oo.query('Year == 1896')
print(type(oo_of_1896))
# <class 'pandas.core.frame.DataFrame'>
print(oo_of_1896.shape)
# (151, 11)
print(oo_of_1896)

print(oo[oo.Year > 1896].shape)
# (27023, 11)
print(oo[oo.Year < 1896].shape)
# (0, 11)