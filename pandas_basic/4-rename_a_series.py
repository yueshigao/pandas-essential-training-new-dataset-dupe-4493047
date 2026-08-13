import pandas as pd

filename = 'olympics_1896_2004.csv'
oo = pd.read_csv(filename, skiprows=5)
print(oo.sample(3))
#        Year    City     Sport Discipline              Athlete Name  NOC Gender               Event Event Gender   Medal  Position
# 6896   1936  Berlin  Handball   Handball          TAUSCHER, Johann  AUT    Men            handball            M  Silver         2
# 4480   1924   Paris  Shooting   Shooting  MONTGOMERY, Robert James  CAN    Men  clay pigeons, team            M  Silver         2
# 18874  1988   Seoul   Fencing    Fencing         WEIDNER, Thorsten  FRG    Men           foil team            M  Silver         2

mapper = {"Athlete Name": "Athlete_Name", "Event Gender": "Event_Gender"}

# Rename the columns of the DataFrame oo.rename
# mapper : dict-like or function
#     Dict-like or function transformations to apply to
#     that axis' values. Use either ``mapper`` and ``axis`` to
#     specify the axis to target with ``mapper``, or ``index`` and
#     ``columns``.
# axis : {0 or 'index', 1 or 'columns'}, default 0
#     Axis to target with ``mapper``. Can be either the axis name
#     ('index', 'columns') or number (0, 1). The default is 'index'.
# inplace : bool, default False
#     Whether to modify the DataFrame rather than creating a new one.
#     If True then value of copy is ignored.
oo.rename(mapper, axis=1, inplace=True)
print(oo.sample(3))
#        Year       City       Sport   Discipline            Athlete_Name  NOC Gender                 Event Event_Gender   Medal  Position
# 23177  2000     Sydney        Judo         Judo  BELTRAN, Daima Mayelis  CUB  Women  + 78kg (heavyweight)            W  Silver         2
# 6991   1936     Berlin   Athletics    Athletics              SON, Kitei  JPN    Men              marathon            M    Gold         1
# 2643   1912  Stockholm  Gymnastics  Artistic G.    KULLBERG, Anders Boo  SWE    Men  team, Swedish system            M    Gold         1

# using the columns parameter
oo.rename(columns=mapper, inplace=True)
# using original dict
oo.rename(columns={"Athlete_Name": "Athlete Name", "Event_Gender": "Event Gender"}, inplace=True)
# chained method calls
print(pd.read_csv(filename, skiprows=5).rename(columns=mapper).sample(3))

# columns_names, suitable when you want to rename several or all columns of a DataFrame
columns_names = ['Year', 'City', 'Sport', 'Discipline', 'Athlete_Name', 'NOC', 'Gender', 'Event', 'Event_Gender', 'Medal', 'Position']

oo = pd.read_csv(filename, skiprows=5)
print(oo.sample(3))
#        Year    City     Sport Discipline              Athlete Name  NOC Gender               Event Event Gender   Medal  Position
# 6896   1936  Berlin  Handball   Handball          TAUSCHER, Johann  AUT    Men            handball            M  Silver         2
# 4480   1924   Paris  Shooting   Shooting  MONTGOMERY, Robert James  CAN    Men  clay pigeons, team            M  Silver         2
# 18874  1988   Seoul   Fencing    Fencing         WEIDNER, Thorsten  FRG    Men           foil team            M  Silver         2

# assign a new list of column names to oo.columns
oo.columns = columns_names
print(oo.sample(3))
#        Year      City     Sport Discipline         Athlete_Name  NOC Gender                                     Event Event_Gender   Medal  Position
# 15065  1976  Montreal   Sailing    Sailing      HANSSON, Ingvar  SWE    Men                                   tempest            X    Gold         1
# 10782  1964     Tokyo  Shooting   Shooting  KVELIASHVILI, Shota  URS    Men  300m free rifle 3 positions (3x40 shots)            M  Silver         2
# 24066  2000    Sydney   Sailing    Sailing  SENSINI, Alessandra  ITA  Women                           board (Mistral)            W    Gold         1

# using names parameter in pd.read_csv
print(pd.read_csv(filename, skiprows=5, names=columns_names).head(3))
#    Year    City    Sport     Discipline        Athlete_Name  NOC  Gender  Event  Event_Gender   Medal  Position
# 0  Year    City    Sport     Discipline        Athlete Name  NOC  Gender  Event  Event Gender   Medal  Position  //original column names are used as the first row of data
# 1  1896  Athens  Cycling  Cycling Track       FLAMENG, Léon  FRA     Men  100km             M    Gold         1
# 2  1896  Athens  Cycling  Cycling Track  KOLETTIS, Georgios  GRE     Men  100km             M  Silver         2

# using header parameter in pd.read_csv
print(pd.read_csv(filename, skiprows=5, names=columns_names, header=0).head(3))
#    Year    City      Sport     Discipline        Athlete_Name  NOC Gender  Event Event_Gender   Medal  Position
# 0  1896  Athens    Cycling  Cycling Track       FLAMENG, Léon  FRA    Men  100km            M    Gold         1
# 1  1896  Athens    Cycling  Cycling Track  KOLETTIS, Georgios  GRE    Men  100km            M  Silver         2
# 2  1896  Athens  Athletics      Athletics       LANE, Francis  USA    Men   100m            M  Bronze         3