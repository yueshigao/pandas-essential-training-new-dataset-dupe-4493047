import pandas as pd

filename = 'olympics_1896_2004.csv'
oo = pd.read_csv(filename, skiprows=5)
print(oo.sample(3))
#        Year    City     Sport Discipline              Athlete Name  NOC Gender               Event Event Gender   Medal  Position
# 6896   1936  Berlin  Handball   Handball          TAUSCHER, Johann  AUT    Men            handball            M  Silver         2
# 4480   1924   Paris  Shooting   Shooting  MONTGOMERY, Robert James  CAN    Men  clay pigeons, team            M  Silver         2
# 18874  1988   Seoul   Fencing    Fencing         WEIDNER, Thorsten  FRG    Men           foil team            M  Silver         2

# Answer the following questions. Indicate the Pandas command where relevant.

# 1.   What is the time range covered in this dataset?
year_min = oo.Year.min()
print(year_min)
year_max = oo.Year.max()
print(year_max)
# 1896
# 2004

# 2.   The Olympics take place every 4 years. Why are there missing years?
print((year_max - year_min)/4)
print(len(oo.Year.unique()))
print(oo.Year.unique())
# 27.0
# 25
# [1896 1900 1904 1908 1912 1920 1924 1928 1932 1936 1948 1952 1956 1960
#  1964 1968 1972 1976 1980 1984 1988 1992 1996 2000 2004]
# - World War 1: 1914-1918
# - World War 2: 1939-1945

# 3.   What are the types of medals awarded?
print(oo.Medal.unique())
# ['Gold' 'Silver' 'Bronze']

# 4.   Across all of the Olympic Games, how many Gold, Silver and Bronze medals have there been?
print(oo.Medal.value_counts())
# Medal
# Gold      9181
# Silver    9014
# Bronze    8979
# Name: count, dtype: int64

# 5.   Why are there not an equal number of Gold, Silver and Bronze medals?
# - Tied results
# - Team events
# - Disqualifications

# 6.   There are more Gold medals than Silver, and more Silver than Bronze. Why might that be?
print(oo.head(10))
#    Year    City      Sport     Discipline        Athlete Name  NOC Gender                       Event Event Gender   Medal  Position
# 0  1896  Athens    Cycling  Cycling Track       FLAMENG, Léon  FRA    Men                       100km            M    Gold         1
# 1  1896  Athens    Cycling  Cycling Track  KOLETTIS, Georgios  GRE    Men                       100km            M  Silver         2  no Bronze medal was awarded for this event
# 2  1896  Athens  Athletics      Athletics       LANE, Francis  USA    Men                        100m            M  Bronze         3
# 3  1896  Athens  Athletics      Athletics    SZOKOLYI, Alajos  HUN    Men                        100m            M  Bronze         3
# 4  1896  Athens  Athletics      Athletics       BURKE, Thomas  USA    Men                        100m            M    Gold         1
# 5  1896  Athens  Athletics      Athletics      HOFMANN, Fritz  GER    Men                        100m            M  Silver         2
# 6  1896  Athens   Aquatics       Swimming       HAJOS, Alfred  HUN    Men              100m freestyle            M    Gold         1
# 7  1896  Athens   Aquatics       Swimming    HERSCHMANN, Otto  AUT    Men              100m freestyle            M  Silver         2  no Bronze medal was awarded for this event
# 8  1896  Athens   Aquatics       Swimming   DRIVAS, Dimitrios  GRE    Men  100m freestyle for sailors            M  Bronze         3

# 7.   What are the different NOCs (National Olympic Committees)
print(oo.NOC.unique())
# ['FRA' 'GRE' 'USA' 'HUN' 'GER' 'AUT' 'GBR' 'AUS' 'DEN' 'ZZX' 'SUI' 'IND'
#  'NED' 'CAN' 'NOR' 'BEL' 'ESP' 'BOH' 'ITA' 'SWE' 'CUB' 'RU1' 'FIN' 'RSA'
#  'ANZ' 'LUX' 'EST' 'BRA' 'JPN' 'TCH' 'NZL' 'ARG' 'HAI' 'POL' 'URU' 'YUG'
#  'ROU' 'POR' 'EGY' 'PHI' 'IRL' 'CHI' 'MEX' 'LAT' 'TUR' 'KOR' 'PAN' 'JAM'
#  'SRI' 'PER' 'PUR' 'IRI' 'TRI' 'URS' 'LIB' 'BUL' 'VEN' 'EUA' 'PAK' 'ISL'
#  'BAH' 'BWI' 'GHA' 'IRQ' 'SIN' 'TPE' 'ETH' 'MAR' 'TUN' 'NGR' 'KEN' 'FRG'
#  'MGL' 'GDR' 'UGA' 'CMR' 'PRK' 'COL' 'NIG' 'BER' 'THA' 'TAN' 'GUY' 'ZIM'
#  'ZAM' 'CHN' 'CIV' 'DOM' 'ALG' 'SYR' 'SUR' 'CRC' 'SEN' 'AHO' 'DJI' 'ISV'
#  'INA' 'EUN' 'NAM' 'IOP' 'QAT' 'ISR' 'LTU' 'CRO' 'SLO' 'MAS' 'RUS' 'UKR'
#  'TGA' 'ARM' 'BLR' 'MDA' 'ECU' 'KAZ' 'AZE' 'BDI' 'SVK' 'CZE' 'UZB' 'GEO'
#  'MOZ' 'HKG' 'KGZ' 'BAR' 'KSA' 'VIE' 'MKD' 'KUW' 'ERI' 'SCG' 'UAE' 'PAR']

# 8.   What does the NOC 'ZZX' represent?
# - Mixed team (1896-1904)
