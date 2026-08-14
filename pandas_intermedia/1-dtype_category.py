import pandas as pd

filename = 'olympics_1896_2004.csv'
oo = pd.read_csv(filename, skiprows=5).rename(columns={'Athlete Name': 'Athlete_Name', 'Event Gender': 'Event_Gender'})
print(oo.head(3))
# Year    City      Sport     Discipline        Athlete_Name  NOC Gender      Event Event_Gender   Medal  Position
# 15763  1980    Moscow  Basketball  Basketball  BARISHEVA-KOROSTELEVA, Olga  URS  Women  basketball            W    Gold         1
# 22397  1996   Atlanta    Football    Football                    LIU, Ying  CHN  Women    football            W  Silver         2
# 14815  1976  Montreal      Hockey      Hockey          MAISTER, Barry John  NZL    Men      hockey            M    Gold         1

# set series astype category 
print(oo.Medal.unique())
oo.Medal = oo.Medal.astype("category")
print(type(oo.Medal.astype("category")))
# <class 'pandas.core.series.Series'>
print(oo.Medal.head(3))
# 0      Gold
# 1    Silver
# 2    Bronze
# Name: Medal, dtype: category
# Categories (3, object): ['Bronze', 'Gold', 'Silver']

# change order of a category 
ordered_medal = pd.Categorical(oo.Medal, categories=["Bronze", "Silver", "Gold"], ordered=True)
print(type(ordered_medal))
# <class 'pandas.core.arrays.categorical.Categorical'>
print(ordered_medal)
# ['Gold', 'Silver', 'Bronze', 'Bronze', 'Gold', ..., 'Gold', 'Gold', 'Silver', 'Silver', 'Silver']
# Length: 27174
# Categories (3, object): ['Bronze' < 'Silver' < 'Gold']

print(oo.Medal.head(3)) #not yet changed 
# 0      Gold
# 1    Silver
# 2    Bronze
# Name: Medal, dtype: category
# Categories (3, object): ['Bronze', 'Gold', 'Silver']

# need to apply new categarical to orignal series
oo.Medal = ordered_medal
print(oo.Medal.head(3))
# 0      Gold
# 1    Silver
# 2    Bronze
# Name: Medal, dtype: category
# Categories (3, object): ['Bronze' < 'Silver' < 'Gold']

print(oo.sort_values(by=["Year", "Event", "Medal"], ascending=[True, True, False]).head(10))
#     Year    City      Sport     Discipline        Athlete_Name  NOC Gender                       Event Event_Gender   Medal  Position
# 0   1896  Athens    Cycling  Cycling Track       FLAMENG, Léon  FRA    Men                       100km            M    Gold         1
# 1   1896  Athens    Cycling  Cycling Track  KOLETTIS, Georgios  GRE    Men                       100km            M  Silver         2
# 4   1896  Athens  Athletics      Athletics       BURKE, Thomas  USA    Men                        100m            M    Gold         1
# 5   1896  Athens  Athletics      Athletics      HOFMANN, Fritz  GER    Men                        100m            M  Silver         2
# 2   1896  Athens  Athletics      Athletics       LANE, Francis  USA    Men                        100m            M  Bronze         3
# 3   1896  Athens  Athletics      Athletics    SZOKOLYI, Alajos  HUN    Men                        100m            M  Bronze         3
# 6   1896  Athens   Aquatics       Swimming       HAJOS, Alfred  HUN    Men              100m freestyle            M    Gold         1
# 7   1896  Athens   Aquatics       Swimming    HERSCHMANN, Otto  AUT    Men              100m freestyle            M  Silver         2
# 9   1896  Athens   Aquatics       Swimming  MALOKINIS, Ioannis  GRE    Men  100m freestyle for sailors            M    Gold         1
# 10  1896  Athens   Aquatics       Swimming  CHASAPIS, Spiridon  GRE    Men  100m freestyle for sailors            M  Silver         2
