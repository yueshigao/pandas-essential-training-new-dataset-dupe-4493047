import pandas as pd

filename = 'olympics_1896_2004.csv'
oo = pd.read_csv(filename, skiprows=5).rename(columns={'Athlete Name': 'Athlete_Name', 'Event Gender': 'Event_Gender'})
print(oo.head(3))
# Year    City      Sport     Discipline        Athlete_Name  NOC Gender      Event Event_Gender   Medal  Position
# 15763  1980    Moscow  Basketball  Basketball  BARISHEVA-KOROSTELEVA, Olga  URS  Women  basketball            W    Gold         1
# 22397  1996   Atlanta    Football    Football                    LIU, Ying  CHN  Women    football            W  Silver         2
# 14815  1976  Montreal      Hockey      Hockey          MAISTER, Barry John  NZL    Men      hockey            M    Gold         1

oo.Medal = pd.Categorical(oo.Medal, categories=["Gold", "Silver", "Bronze"], ordered=True)
categoriy_memory = oo.Medal.memory_usage(deep=True) 
# deep : bool, default False
#    If True, introspect the data deeply by interrogating object dtypes for system-level memory consumption, and include it in the returned value.
print(f"Medal series memory usage using dtype categoriy: {categoriy_memory}")

df = pd.read_csv(filename, skiprows=5).rename(columns={'Athlete Name': 'Athlete_Name', 'Event Gender': 'Event_Gender'})
object_memory = df.Medal.memory_usage(deep=True)
print(f"Medal series memory usage using dtype object: {object_memory}")

print(categoriy_memory / object_memory) 
# Medal series memory usage using dtype categoriy: 27577
# Medal series memory usage using dtype object: 1476340
# 0.01867930151591097

oo.NOC = oo.NOC.astype("string")
print(oo.dtypes)
print(f"Medal series memory usage using dtype string: {oo.NOC.memory_usage(deep=True)}")
print(f"Medal series memory usage using dtype object: {df.NOC.memory_usage(deep=True)}")
# Medal series memory usage using dtype string: 1413180
# Medal series memory usage using dtype object: 1413180