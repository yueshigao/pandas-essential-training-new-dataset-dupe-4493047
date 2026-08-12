import pandas as pd

filename = 'olympics_1896_2024.csv'
oo = pd.read_csv(filename)

print(oo.shape)

print(oo.head())
#    Year Rank            NOC  Gold  Silver  Bronze  Total
# 0  2024    1  United States    40      44      42    126
# 1  2024    2          China    40      27      24     91
# 2  2024    3          Japan    20      12      13     45
# 3  2024    4      Australia    18      19      16     53
# 4  2024    5         France    16      26      22     64

print(oo.sample(3))
#       2024   5    France  16  26  22  64
# 1358  1912   9    Norway   3   2   5  10
# 224   2016  45  Slovenia   1   2   1   4
# 204   2016  25    Greece   3   1   2   6

type(oo)
# pandas.core.frame.DataFrame

type(oo['NOC'])
# # pandas.core.series.Series

print(oo.NOC) # directly with dot notation
print(oo["NOC"]) # directly with bracket notation, double quotes
print(oo['NOC']) # directly with bracket notation, single quotes
# 0       United States
# 1               China
# 2               Japan
# 3           Australia
# 4              France
#             ...      
# 1431          Austria
# 1432        Australia
# 1433          Denmark
# 1434      Switzerland
# 1435       Mixed team
# Name: NOC, Length: 1436, dtype: object

# print(oo['noc'])
# # KeyError: 'noc', not matching 'NOC'

# Return unique values of Series object.
year_unique = oo.Year.unique()
print(year_unique)
# [2024 2020 2016 2012 2008 2004 2000 1996 1992 1988 1984 1980 1976 1972
#  1968 1964 1960 1956 1952 1948 1936 1932 1928 1924 1920 1912 1908 1904
#  1900 1896]

print(type(year_unique))
# <class 'numpy.ndarray'>

print(len(year_unique))
# 30

# Return a Series containing counts of unique values.
# The resulting object will be in descending order so that the
# first element is the most frequently-occurring element.
# Excludes NA values by default.
print(oo.Year.value_counts())
# Year
# 2020    93
# 2024    92
# 2008    87
# 2016    86
# 2012    86
# 2000    80
# 1996    79
# 2004    74
# 1992    64
# 1988    52
# 1972    48
# 1984    47
# 1960    44
# 1968    44
# 1952    43
# 1964    41
# 1976    41
# 1956    38
# 1948    38
# 1980    36
# 1928    33
# 1936    32
# 1932    28
# 1924    27
# 1920    22
# 1912    19
# 1908    19
# 1900    19
# 1904    13
# 1896    11
# Name: count, dtype: int64

noc_unique = oo.NOC.unique()
print(len(noc_unique))
# 217

# Return a Series containing counts of unique values.
# normalize : bool, default False
# If True then the object returned will contain the relative
# frequencies of the unique values.
print(oo.NOC.value_counts().head(50))
# NOC
# Switzerland            27
# France                 27
# Great Britain          27
# Denmark                26
# United States          26
# Australia              26
# Sweden                 25
# Hungary                25
# Belgium                25
# Italy                  25
# Canada                 24
# Norway                 24
# Austria                24
# Netherlands            24
# Finland                23
# New Zealand            21
# Japan                  21
# Poland                 21
# Brazil                 20
# Mexico                 20
# Romania                20
# Greece                 19
# Spain                  19
# Argentina              19
# Turkey                 18
# India                  18
# South Korea            18
# Iran                   17
# Bulgaria               17
# South Africa           17
# Jamaica                17
# Cuba                   17
# Germany                16
# Portugal               16
# Ireland                15
# Kenya                  14
# Czechoslovakia         14
# Mongolia               13
# Yugoslavia             13
# Ethiopia               13
# Thailand               12
# Colombia               11
# Estonia                11
# China                  11
# North Korea            11
# Egypt                  11
# Morocco                11
# Venezuela              10
# Trinidad and Tobago    10
# Indonesia              10

france_years = oo[oo.NOC == 'France']['Year'].unique()
print(france_years)
# [2024 2020 2016 2012 2008 2004 2000 1996 1992 1988 1984 1980 1976 1972 1968 1964 1956 1952 1948 1936 1928 1924 1920 1912 1904 1900 1896]
print(len(france_years))
# 27

# Return a Series containing counts of unique values.
# normalize : bool, default False
# If True then the object returned will contain the relative
# frequencies of the unique values.
print(oo.NOC.value_counts(normalize=True).head(50))
# NOC
# Switzerland            0.018802
# France                 0.018802
# Great Britain          0.018802
# Denmark                0.018106
# United States          0.018106
# Australia              0.018106
# Sweden                 0.017409
# Hungary                0.017409
# Belgium                0.017409
# Italy                  0.017409
# Canada                 0.016713
# Norway                 0.016713
# Austria                0.016713
# Netherlands            0.016713
# Finland                0.016017
# New Zealand            0.014624
# Japan                  0.014624
# Poland                 0.014624
# Brazil                 0.013928
# Mexico                 0.013928
# Romania                0.013928
# Greece                 0.013231
# Spain                  0.013231
# Argentina              0.013231
# Turkey                 0.012535
# India                  0.012535
# South Korea            0.012535
# Iran                   0.011838
# Bulgaria               0.011838
# South Africa           0.011838
# Jamaica                0.011838
# Cuba                   0.011838
# Germany                0.011142
# Portugal               0.011142
# Ireland                0.010446
# Kenya                  0.009749
# Czechoslovakia         0.009749
# Mongolia               0.009053
# Yugoslavia             0.009053
# Ethiopia               0.009053
# Thailand               0.008357
# Colombia               0.007660
# Estonia                0.007660
# China                  0.007660
# North Korea            0.007660
# Egypt                  0.007660
# Morocco                0.007660
# Venezuela              0.006964
# Trinidad and Tobago    0.006964
# Indonesia              0.006964
# Name: proportion, dtype: float64

# number of total rows
print(len(oo))
# 1436

# check switzerland rows count: total rows × 0.018802 ≈ 27
print(len(oo) * 0.018802)
# 26.999672

# sort the DataFrame by the 'Total' column in descending order
oo_sorted = oo.sort_values('Total', ascending=False)
print(oo_sorted[['NOC', 'Year', 'Total']].head(50))
# NOC  Year  Total
# 1393           United States  1904    234
# 840             Soviet Union  1980    195
# 793            United States  1984    174
# 1374  Great Britain (GBR)[a]  1908    146
# 741             Soviet Union  1988    132
# 0              United States  2024    126
# 841             East Germany  1980    126
# 876             Soviet Union  1976    125
# 185            United States  2016    121
# 92             United States  2020    113
# 358            United States  2008    112
# 677             Unified Team  1992    112
# 1406                  France  1900    112
# 1245     United States (USA)  1932    110
# 678            United States  1992    108
# 965            United States  1968    107
# 271            United States  2012    105
# 1050      Soviet Union (URS)  1960    103
# 742             East Germany  1988    102
# 598            United States  1996    101
# 444            United States  2004    101
# 1213                 Germany  1936    101
# 357                    China  2008    100
# 1306           United States  1924     99
# 917             Soviet Union  1972     99
# 1094            Soviet Union  1956     98
# 1010            Soviet Union  1964     96
# 1333           United States  1920     95
# 878            United States  1976     94
# 743            United States  1988     94
# 918            United States  1972     94
# 518            United States  2000     93
# 272                    China  2012     92
# 1                      China  2024     91
# 966             Soviet Union  1968     91
# 877             East Germany  1976     90
# 446                   Russia  2004     90
# 1009           United States  1964     90
# 519                   Russia  2000     89
# 93                     China  2020     89
# 1175           United States  1948     84
# 679                  Germany  1992     82
# 1132           United States  1952     76
# 1095           United States  1956     74
# 1133            Soviet Union  1952     71
# 1051     United States (USA)  1960     71
# 96                       ROC  2020     71
# 187                    China  2016     70
# 186            Great Britain  2016     67
# 919             East Germany  1972     66


# sort the DataFrame by the 'Gold' column in descending order
oo_sorted = oo.sort_values('Gold', ascending=False)
print(oo_sorted[['NOC', 'Year', 'Gold']].head(50))
#                          NOC  Year  Gold
# 793            United States  1984    83
# 840             Soviet Union  1980    80
# 1393           United States  1904    77
# 1374  Great Britain (GBR)[a]  1908    56
# 741             Soviet Union  1988    55
# 917             Soviet Union  1972    50
# 876             Soviet Union  1976    49
# 357                    China  2008    48
# 271            United States  2012    48
# 841             East Germany  1980    47
# 185            United States  2016    46
# 965            United States  1968    45
# 1306           United States  1924    45
# 677             Unified Team  1992    45
# 1245     United States (USA)  1932    44
# 598            United States  1996    44
# 1050      Soviet Union (URS)  1960    43
# 1333           United States  1920    41
# 0              United States  2024    40
# 877             East Germany  1976    40
# 1132           United States  1952    40
# 1                      China  2024    40
# 272                    China  2012    39
# 92             United States  2020    39
# 1213                 Germany  1936    38
# 1175           United States  1948    38
# 93                     China  2020    38
# 518            United States  2000    37
# 678            United States  1992    37
# 742             East Germany  1988    37
# 1094            Soviet Union  1956    37
# 358            United States  2008    36
# 444            United States  2004    36
# 1009           United States  1964    36
# 743            United States  1988    36
# 878            United States  1976    34
# 1051     United States (USA)  1960    34
# 679                  Germany  1992    33
# 918            United States  1972    33
# 1095           United States  1956    32
# 519                   Russia  2000    32
# 445                    China  2004    32
# 1406                  France  1900    31
# 1010            Soviet Union  1964    30
# 273            Great Britain  2012    29
# 966             Soviet Union  1968    29
# 520                    China  2000    28
# 446                   Russia  2004    28
# 94                     Japan  2020    27
# 186            Great Britain  2016    27
