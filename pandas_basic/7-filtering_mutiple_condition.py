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

print(oo[(oo.Year == 1896) & (oo.Medal == 'Gold')])
print(oo[(oo.Year == 1896) | (oo.Year == 1900)])
print(oo[(oo.City == 'Athens') & ~(oo.Year == 1896)]) # Athens hold twice

first_men_100m = oo[(oo.Year == 1896) & (oo.Gender == 'Men') & (oo.Event == '100m')]
print(first_men_100m)
print(first_men_100m[["Athlete Name", "NOC", "Medal"]])

chinese_gold = oo[(oo.NOC == 'CHN') & (oo.Medal == 'Gold')]
print(chinese_gold[["Year", "City", "Sport", "Athlete Name", "Event"]].head(20))
print(chinese_gold.shape)
# (160, 11)

chinese_metals= oo[(oo.NOC == 'CHN')]
print(chinese_metals[["Year", "City", "Sport", "Athlete Name", "Event", "Medal"]])
print(chinese_metals.shape)
# (495, 11)