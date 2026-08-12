import pandas as pd

filename = 'olympics_1896_2004.csv'
oo = pd.read_csv(filename, skiprows=5)

# Return a tuple representing the dimensionality of the DataFrame.
print(oo.shape) 
# (27174, 11) 
# 27179 rows and 11 columns

print(oo.head(5))
#    Year    City      Sport     Discipline        Athlete Name  NOC Gender  Event Event Gender   Medal  Position
# 0  1896  Athens    Cycling  Cycling Track       FLAMENG, Léon  FRA    Men  100km            M    Gold         1
# 1  1896  Athens    Cycling  Cycling Track  KOLETTIS, Georgios  GRE    Men  100km            M  Silver         2
# 2  1896  Athens  Athletics      Athletics       LANE, Francis  USA    Men   100m            M  Bronze         3
# 3  1896  Athens  Athletics      Athletics    SZOKOLYI, Alajos  HUN    Men   100m            M  Bronze         3
# 4  1896  Athens  Athletics      Athletics       BURKE, Thomas  USA    Men   100m            M    Gold         1

print(oo.tail(5))
#        Year    City    Sport Discipline        Athlete Name  NOC Gender      Event Event Gender   Medal  Position
# 27169  2004  Athens  Fencing    Fencing  LOGOUNOVA, Tatiana  RUS  Women  épée team            W    Gold         1
# 27170  2004  Athens  Fencing    Fencing       SIVKOVA, Anna  RUS  Women  épée team            W    Gold         1
# 27171  2004  Athens  Fencing    Fencing      BOKEL, Claudia  GER  Women  épée team            W  Silver         2
# 27172  2004  Athens  Fencing    Fencing     DUPLITZER, Imke  GER  Women  épée team            W  Silver         2
# 27173  2004  Athens  Fencing    Fencing   HEIDEMANN, Britta  GER  Women  épée team            W  Silver         2

print(oo.sample(n=5))
#        Year    City       Sport       Discipline                    Athlete Name  NOC Gender         Event Event Gender   Medal  Position
# 25059  2000  Sydney  Volleyball       Volleyball                   TORRES, Regla  CUB  Women    volleyball            W    Gold         1
# 26872  2004  Athens    Aquatics  Synchronized S.                KISSELEVA, Maria  RUS  Women          team            W    Gold         1
# 26431  2004  Athens    Handball         Handball               RAMOTA, Christian  GER    Men      handball            M  Silver         2
# 25651  2004  Athens   Taekwondo        Taekwondo                        LUO, Wei  CHN  Women    57 - 67 kg            W    Gold         1
# 11907  1968  Mexico   Athletics        Athletics  IGNATYEVA-SAMOTESOVA, Lyudmila  URS  Women  4x100m relay            W  Bronze         3

print(oo.columns)
# Index(['Year', 'City', 'Sport', 'Discipline', 'Athlete Name', 'NOC', 'Gender', 'Event', 'Event Gender', 'Medal', 'Position'], dtype='object')
# column's data type is object, which means it is a string

print("========================================")
print(oo.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 27174 entries, 0 to 27173
# Data columns (total 11 columns):
#  #   Column        Non-Null Count  Dtype 
# ---  ------        --------------  ----- 
#  0   Year          27174 non-null  int64 
#  1   City          27174 non-null  object
#  2   Sport         27174 non-null  object
#  3   Discipline    27174 non-null  object
#  4   Athlete Name  27174 non-null  object
#  5   NOC           27174 non-null  object
#  6   Gender        27174 non-null  object
#  7   Event         27174 non-null  object
#  8   Event Gender  27174 non-null  object
#  9   Medal         27174 non-null  object
#  10  Position      27174 non-null  int64 
# dtypes: int64(2), object(9)
# memory usage: 2.3+ MB
# None

print("========================================")
print(oo.describe())
#                Year      Position
# count  27174.000000  27174.000000
# mean    1964.685803      1.992566
# std       31.590396      0.817469
# min     1896.000000      1.000000
# 25%     1936.000000      1.000000
# 50%     1972.000000      2.000000
# 75%     1992.000000      3.000000
# max     2004.000000      3.000000