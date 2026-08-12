import pandas as pd

filename = 'olympics_1896_2004.csv'

# read the CSV file, returning a DataFrame
print(pd.read_csv(filename))
#       This is a list of medallists at the Summer Olympic Games (1896-2004) with details of the year of the olympics, city, sport, discipline, athlete name, gender, event and medal  ... Unnamed: 10
# 0                                                    NaN                                                                                                                             ...         NaN
# 1      DISCLAIMER: No guarantees, express or implied,...                                                                                                                             ...         NaN
# 2                                                    NaN                                                                                                                             ...         NaN
# 3                                                    NaN                                                                                                                             ...         NaN
# 4                                                   Year                                                                                                                             ...    Position
# ...                                                  ...                                                                                                                             ...         ...
# 27174                                               2004                                                                                                                             ...           1
# 27175                                               2004                                                                                                                             ...           1
# 27176                                               2004                                                                                                                             ...           2
# 27177                                               2004                                                                                                                             ...           2
# 27178                                               2004                                                                                                                             ...           2
# [27179 rows x 11 columns]

# read the CSV file, skipping the first 5 rows, returning a DataFrame
print(pd.read_csv(filename, skiprows=5))
# Year    City      Sport     Discipline        Athlete Name  NOC Gender      Event Event Gender   Medal  Position
# 0      1896  Athens    Cycling  Cycling Track       FLAMENG, Léon  FRA    Men      100km            M    Gold         1
# 1      1896  Athens    Cycling  Cycling Track  KOLETTIS, Georgios  GRE    Men      100km            M  Silver         2
# 2      1896  Athens  Athletics      Athletics       LANE, Francis  USA    Men       100m            M  Bronze         3
# 3      1896  Athens  Athletics      Athletics    SZOKOLYI, Alajos  HUN    Men       100m            M  Bronze         3
# 4      1896  Athens  Athletics      Athletics       BURKE, Thomas  USA    Men       100m            M    Gold         1
# ...     ...     ...        ...            ...                 ...  ...    ...        ...          ...     ...       ...
# 27169  2004  Athens    Fencing        Fencing  LOGOUNOVA, Tatiana  RUS  Women  épée team            W    Gold         1
# 27170  2004  Athens    Fencing        Fencing       SIVKOVA, Anna  RUS  Women  épée team            W    Gold         1
# 27171  2004  Athens    Fencing        Fencing      BOKEL, Claudia  GER  Women  épée team            W  Silver         2
# 27172  2004  Athens    Fencing        Fencing     DUPLITZER, Imke  GER  Women  épée team            W  Silver         2
# 27173  2004  Athens    Fencing        Fencing   HEIDEMANN, Britta  GER  Women  épée team            W  Silver         2