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

print(oo.City.str.upper().sample(3))
print(oo.Athlete_Name.str.lower().sample(3))
print(oo.Event.unique())
print(oo.Event.str.replace(" ", "_").sample(3))
print(oo.Event.str.capitalize().sample(3))

print(dir(oo.Event.str))
# ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__frozen', '__ge__', '__getattribute__', 
# '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__','__weakref__', '_data', '_doc_args', 
# '_freeze', '_get_series_list', '_index', '_inferred_dtype', '_is_categorical', '_is_string', '_name', '_orig', '_parent', '_validate', '_wrap_result', 
# 'capitalize','casefold', 'cat', 'center', 'contains', 'count', 'decode', 'encode', 'endswith', 'extract', 'extractall', 'find', 'findall', 'fullmatch', 
# 'get', 'get_dummies', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper', 'join', 'len', 
# 'ljust', 'lower', 'lstrip', 'match', 'normalize', 'pad', 'partition', 'removeprefix', 'removesuffix', 'repeat', 'replace', 'rfind', 'rindex', 'rjust', 
# 'rpartition', 'rsplit', 'rstrip', 'slice', 'slice_replace', 'split', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'wrap', 'zfill']

contains_xu_haifeng = oo.Athlete_Name.str.contains("Haifeng") # contrains returns a boolean series, which can be used to filter the DataFrame
print(contains_xu_haifeng.sample(3))
# 1215     False
# 14681    False
# 8087     False
# Name: Athlete_Name, dtype: bool
print(type(contains_xu_haifeng))
# <class 'pandas.core.series.Series'>
print(oo[contains_xu_haifeng])
#        Year         City     Sport Discipline Athlete_Name  NOC Gender                      Event Event_Gender   Medal  Position
# 16908  1984  Los Angeles  Shooting   Shooting  XU, Haifeng  CHN    Men      50m pistol (60 shots)            M    Gold         1
# 18133  1988        Seoul  Shooting   Shooting  XU, Haifeng  CHN    Men  10m air pistol (60 shots)            M  Bronze         3

city_upper = oo.City.str.upper()
print(city_upper.unique())
# ['ATHENS' 'PARIS' 'ST LOUIS' 'LONDON' 'STOCKHOLM' 'ANTWERP' 'AMSTERDAM'
#  'LOS ANGELES' 'BERLIN' 'HELSINKI' 'MELBOURNE / STOCKHOLM' 'ROME' 'TOKYO'
#  'MEXICO' 'MUNICH' 'MONTREAL' 'MOSCOW' 'SEOUL' 'BARCELONA' 'ATLANTA'
#  'SYDNEY']

# city_upper is a Series, not a DataFrame, so it does not modify the original DataFrame oo
print(oo.City.unique())
# ['Athens' 'Paris' 'St Louis' 'London' 'Stockholm' 'Antwerp' 'Amsterdam'
#  'Los Angeles' 'Berlin' 'Helsinki' 'Melbourne / Stockholm' 'Rome' 'Tokyo'
#  'Mexico' 'Munich' 'Montreal' 'Moscow' 'Seoul' 'Barcelona' 'Atlanta'
#  'Sydney']

# apply the city_upper to the oo.City column, which will modify the original DataFrame oo
oo.City = city_upper
print(oo.City.unique())
# ['ATHENS' 'PARIS' 'ST LOUIS' 'LONDON' 'STOCKHOLM' 'ANTWERP' 'AMSTERDAM'
#  'LOS ANGELES' 'BERLIN' 'HELSINKI' 'MELBOURNE / STOCKHOLM' 'ROME' 'TOKYO'
#  'MEXICO' 'MUNICH' 'MONTREAL' 'MOSCOW' 'SEOUL' 'BARCELONA' 'ATLANTA'
#  'SYDNEY']