import pandas as pd

filename = 'olympics_1896_2004.csv'
oo = pd.read_csv(filename, skiprows=5).rename(columns={'Athlete Name': 'Athlete_Name', 'Event Gender': 'Event_Gender'})
print(oo.head(3))
# Year    City      Sport     Discipline        Athlete_Name  NOC Gender      Event Event_Gender   Medal  Position
# 15763  1980    Moscow  Basketball  Basketball  BARISHEVA-KOROSTELEVA, Olga  URS  Women  basketball            W    Gold         1
# 22397  1996   Atlanta    Football    Football                    LIU, Ying  CHN  Women    football            W  Silver         2
# 14815  1976  Montreal      Hockey      Hockey          MAISTER, Barry John  NZL    Men      hockey            M    Gold         1
print(oo.shape)
# (27174, 11)

# sorting series(a single column)
print(oo.Athlete_Name.sort_values().head(3))
# 611              AABYE, Edgar
# 3060    AALTONEN, Arvo Ossian
# 2963    AALTONEN, Arvo Ossian
# Name: Athlete_Name, dtype: object
print(type(oo.Athlete_Name.sort_values()))
# <class 'pandas.core.series.Series'>   

# sorting dataframe by a column
print(oo.sort_values('Athlete_Name').head(3))
#       Year     City       Sport  Discipline           Athlete_Name  NOC Gender              Event Event_Gender   Medal  Position
# 611   1900    Paris  Tug of War  Tug of War           AABYE, Edgar  ZZX    Men         tug of war            M    Gold         1
# 3060  1920  Antwerp    Aquatics    Swimming  AALTONEN, Arvo Ossian  FIN    Men  400m breaststroke            M  Bronze         3
# 2963  1920  Antwerp    Aquatics    Swimming  AALTONEN, Arvo Ossian  FIN    Men  200m breaststroke            M  Bronze         3
print(type(oo.sort_values('Athlete_Name')))
# <class 'pandas.core.frame.DataFrame'>

# not inplace, because it returns a new DataFrame, and does not modify the original DataFrame oo
print(oo.head(3))
#    Year    City      Sport     Discipline        Athlete_Name  NOC Gender  Event Event_Gender   Medal  Position
# 0  1896  Athens    Cycling  Cycling Track       FLAMENG, Léon  FRA    Men  100km            M    Gold         1
# 1  1896  Athens    Cycling  Cycling Track  KOLETTIS, Georgios  GRE    Men  100km            M  Silver         2
# 2  1896  Athens  Athletics      Athletics       LANE, Francis  USA    Men   100m            M  Bronze         3

# sorting dataframe by multiple columns
print(oo.sort_values(by=['Year', 'Discipline', 'NOC', 'Position'], ascending=[False, True, True, True]).head(30))
#        Year    City       Sport   Discipline        Athlete_Name  NOC Gender                                  Event Event_Gender   Medal  Position
# 26604  2004  Athens     Archery      Archery        CUDDIHY, Tim  AUS    Men  individual (FITA Olympic round - 70m)            M  Bronze         3
# 26937  2004  Athens     Archery      Archery            HE, Ying  CHN  Women        team (FITA Olympic round - 70m)            W  Silver         2
# 26938  2004  Athens     Archery      Archery           LIN, Sang  CHN  Women        team (FITA Olympic round - 70m)            W  Silver         2
# 26939  2004  Athens     Archery      Archery    ZHANG, Juan Juan  CHN  Women        team (FITA Olympic round - 70m)            W  Silver         2
# 26607  2004  Athens     Archery      Archery  WILLIAMSON, Alison  GBR  Women  individual (FITA Olympic round - 70m)            W  Bronze         3
# 26605  2004  Athens     Archery      Archery     GALIAZZO, Marco  ITA    Men  individual (FITA Olympic round - 70m)            M    Gold         1
# 26606  2004  Athens     Archery      Archery   YAMAMOTO, Hiroshi  JPN    Men  individual (FITA Olympic round - 70m)            M  Silver         2
# 26608  2004  Athens     Archery      Archery     PARK, Sung-Hyun  KOR  Women  individual (FITA Olympic round - 70m)            W    Gold         1
# 26925  2004  Athens     Archery      Archery       IM, Dong Hyun  KOR    Men        team (FITA Olympic round - 70m)            M    Gold         1
# 26926  2004  Athens     Archery      Archery       JANG, Yong-Ho  KOR    Men        team (FITA Olympic round - 70m)            M    Gold         1
# 26927  2004  Athens     Archery      Archery      PARK, Kyung Mo  KOR    Men        team (FITA Olympic round - 70m)            M    Gold         1
# 26934  2004  Athens     Archery      Archery       LEE, Sung Jin  KOR  Women        team (FITA Olympic round - 70m)            W    Gold         1
# 26935  2004  Athens     Archery      Archery     PARK, Sung-Hyun  KOR  Women        team (FITA Olympic round - 70m)            W    Gold         1
# 26936  2004  Athens     Archery      Archery         YUN, Mi-Jin  KOR  Women        team (FITA Olympic round - 70m)            W    Gold         1
# 26609  2004  Athens     Archery      Archery       LEE, Sung Jin  KOR  Women  individual (FITA Olympic round - 70m)            W  Silver         2
# 26928  2004  Athens     Archery      Archery      CHEN, Szu Yuan  TPE    Men        team (FITA Olympic round - 70m)            M  Silver         2
# 26929  2004  Athens     Archery      Archery     LIU, Ming Huang  TPE    Men        team (FITA Olympic round - 70m)            M  Silver         2
# 26930  2004  Athens     Archery      Archery    WANG, Cheng Pang  TPE    Men        team (FITA Olympic round - 70m)            M  Silver         2
# 26931  2004  Athens     Archery      Archery         CHEN, Li Ju  TPE  Women        team (FITA Olympic round - 70m)            W  Bronze         3
# 26932  2004  Athens     Archery      Archery          WU, Hui Ju  TPE  Women        team (FITA Olympic round - 70m)            W  Bronze         3
# 26933  2004  Athens     Archery      Archery       YUAN, Shu Chi  TPE  Women        team (FITA Olympic round - 70m)            W  Bronze         3
# 26922  2004  Athens     Archery      Archery     HRACHOV, Dmytro  UKR    Men        team (FITA Olympic round - 70m)            M  Bronze         3
# 26923  2004  Athens     Archery      Archery       RUBAN, Viktor  UKR    Men        team (FITA Olympic round - 70m)            M  Bronze         3
# 26924  2004  Athens     Archery      Archery  SERDYUK, Oleksandr  UKR    Men        team (FITA Olympic round - 70m)            M  Bronze         3
# 26723  2004  Athens  Gymnastics  Artistic G.    IOVTCHEV, Iordan  BUL    Men                                  rings            M  Silver         2
# 26237  2004  Athens  Gymnastics  Artistic G.    IOVTCHEV, Iordan  BUL    Men                        floor exercises            M  Bronze         3
# 26238  2004  Athens  Gymnastics  Artistic G.      SHEWFELT, Kyle  CAN    Men                        floor exercises            M    Gold         1
# 26695  2004  Athens  Gymnastics  Artistic G.        TENG, Haibin  CHN    Men                           pommel horse            M    Gold         1
# 26613  2004  Athens  Gymnastics  Artistic G.          ZHANG, Nan  CHN  Women                   individual all-round            W  Bronze         3
# 26682  2004  Athens  Gymnastics  Artistic G.        LI, Xiaopeng  CHN    Men                          parallel bars            M  Bronze         3