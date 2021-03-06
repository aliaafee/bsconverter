"""
BS Converter
"""
import sys
import getopt

import datetime


startBSYear = 1970

daysInBSMonths = [
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #1970
    ( 31, 31, 32, 31, 32, 30, 30, 29, 30, 29,30, 30 ), #1971
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 30 ), #1972
    ( 30, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #1973
    ( 31, 31, 32, 30, 31, 31, 30, 29, 30, 29,30, 30 ), #1974
    ( 31, 31, 32, 32, 30, 31, 30, 29, 30, 29,30, 30 ), #1975
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #1976
    ( 30, 32, 31, 32, 31, 31, 29, 30, 29, 30,29, 31 ), #1977
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #1978
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #1979
    ( 30, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #1980
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,30, 30 ), #1981
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #1982
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #1983
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #1984
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,30, 30 ), #1985
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #1986
    ( 31, 32, 31, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #1987
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #1988
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #1989
    ( 30, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #1990
    ( 31, 32, 31, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #1991
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 30 ), #1992
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #1993
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #1994
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #1995
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #1996
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #1997
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #1998
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #1999
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,29, 31 ), #2000
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2001
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2002
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2003
    ( 30, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2004
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2005
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2006
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2007
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,29, 31 ), #2008
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2009
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2010
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2011
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,30, 30 ), #2012
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2013
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2014
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2015
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,30, 30 ), #2016
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2017
    ( 31, 32, 31, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2018
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2019
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #2020
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2021
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 30 ), #2022
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2023
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #2024
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2025
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2026
    ( 30, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2027
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2028
    ( 31, 31, 32, 31, 32, 30, 30, 29, 30, 29,30, 30 ), #2029
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2030
    ( 30, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2031
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2032
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2033
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2034
    ( 30, 32, 31, 32, 31, 31, 29, 30, 30, 29,29, 31 ), #2035
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2036
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2037
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2038
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,30, 30 ), #2039
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2040
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2041
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2042
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,30, 30 ), #2043
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2044
    ( 31, 32, 31, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2045
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2046
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #2047
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2048
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 30 ), #2049
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2050
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #2051
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2052
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 30 ), #2053
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2054
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2055
    ( 31, 31, 32, 31, 32, 30, 30, 29, 30, 29,30, 30 ), #2056
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2057
    ( 30, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2058
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2059
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2060
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2061
    ( 30, 32, 31, 32, 31, 31, 29, 30, 29, 30,29, 31 ), #2062
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2063
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2064
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2065
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,29, 31 ), #2066
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2067
    ( 31, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2068
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2069
    ( 31, 31, 31, 32, 31, 31, 29, 30, 30, 29,30, 30 ), #2070
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2071
    ( 31, 32, 31, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2072
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 31 ), #2073
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #2074
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2075
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 30 ), #2076
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,29, 31 ), #2077
    ( 31, 31, 31, 32, 31, 31, 30, 29, 30, 29,30, 30 ), #2078
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 29,30, 30 ), #2079
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 29,30, 30 ), #2080
    ( 31, 31, 32, 32, 31, 30, 30, 30, 29, 30,30, 30 ), #2081
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,30, 30 ), #2082
    ( 31, 31, 32, 31, 31, 30, 30, 30, 29, 30,30, 30 ), #2083
    ( 31, 31, 32, 31, 31, 30, 30, 30, 29, 30,30, 30 ), #2084
    ( 31, 32, 31, 32, 31, 31, 30, 30, 29, 30,30, 30 ), #2085
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,30, 30 ), #2086
    ( 31, 31, 32, 31, 31, 31, 30, 30, 29, 30,30, 30 ), #2087
    ( 30, 31, 32, 32, 30, 31, 30, 30, 29, 30,30, 30 ), #2088
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,30, 30 ), #2089
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,30, 30 ), #2090
    ( 31, 31, 32, 31, 31, 31, 30, 30, 29, 30,30, 30 ), #2091
    ( 31, 31, 32, 32, 31, 30, 30, 30, 29, 30,30, 30 ), #2092
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,30, 30 ), #2093
    ( 31, 31, 32, 31, 31, 30, 30, 30, 29, 30,30, 30 ), #2094
    ( 31, 31, 32, 31, 31, 31, 30, 29, 30, 30,30, 30 ), #2095
    ( 30, 31, 32, 32, 31, 30, 30, 29, 30, 29,30, 30 ), #2096
    ( 31, 32, 31, 32, 31, 30, 30, 30, 29, 30,30, 30 ), #2097
    ( 31, 31, 32, 31, 31, 31, 29, 30, 29, 30,30, 31 ), #2098
    ( 31, 31, 32, 31, 31, 31, 30, 29, 29, 30,30, 30 ), #2099
    ( 31, 32, 31, 32, 30, 31, 30, 29, 30, 29,30, 30 )  #2100
]
    
newYearBS = [
    datetime.datetime(1913, 4, 13), #1970
    datetime.datetime(1914, 4, 13), #1971
    datetime.datetime(1915, 4, 13), #1972
    datetime.datetime(1916, 4, 13), #1973
    datetime.datetime(1917, 4, 13), #1974
    datetime.datetime(1918, 4, 12), #1975
    datetime.datetime(1919, 4, 13), #1976
    datetime.datetime(1920, 4, 13), #1977
    datetime.datetime(1921, 4, 13), #1978
    datetime.datetime(1922, 4, 13), #1979
    datetime.datetime(1923, 4, 13), #1980
    datetime.datetime(1924, 4, 13), #1981
    datetime.datetime(1925, 4, 13), #1982
    datetime.datetime(1926, 4, 13), #1983
    datetime.datetime(1927, 4, 13), #1984
    datetime.datetime(1928, 4, 13), #1985
    datetime.datetime(1929, 4, 13), #1986
    datetime.datetime(1930, 4, 13), #1987
    datetime.datetime(1931, 4, 13), #1988
    datetime.datetime(1932, 4, 13), #1989
    datetime.datetime(1933, 4, 13), #1990
    datetime.datetime(1934, 4, 13), #1991
    datetime.datetime(1935, 4, 13), #1992
    datetime.datetime(1936, 4, 13), #1993
    datetime.datetime(1937, 4, 13), #1994
    datetime.datetime(1938, 4, 13), #1995
    datetime.datetime(1939, 4, 13), #1996
    datetime.datetime(1940, 4, 13), #1997
    datetime.datetime(1941, 4, 13), #1998
    datetime.datetime(1942, 4, 13), #1999
    datetime.datetime(1943, 4, 14), #2000
    datetime.datetime(1944, 4, 13), #2001
    datetime.datetime(1945, 4, 13), #2002
    datetime.datetime(1946, 4, 13), #2003
    datetime.datetime(1947, 4, 14), #2004
    datetime.datetime(1948, 4, 13), #2005
    datetime.datetime(1949, 4, 13), #2006
    datetime.datetime(1950, 4, 13), #2007
    datetime.datetime(1951, 4, 14), #2008
    datetime.datetime(1952, 4, 13), #2009
    datetime.datetime(1953, 4, 13), #2010
    datetime.datetime(1954, 4, 13), #2011
    datetime.datetime(1955, 4, 14), #2012
    datetime.datetime(1956, 4, 13), #2013
    datetime.datetime(1957, 4, 13), #2014
    datetime.datetime(1958, 4, 13), #2015
    datetime.datetime(1959, 4, 14), #2016
    datetime.datetime(1960, 4, 13), #2017
    datetime.datetime(1961, 4, 13), #2018
    datetime.datetime(1962, 4, 13), #2019
    datetime.datetime(1963, 4, 14), #2020
    datetime.datetime(1964, 4, 13), #2021
    datetime.datetime(1965, 4, 13), #2022
    datetime.datetime(1966, 4, 13), #2023
    datetime.datetime(1967, 4, 14), #2024
    datetime.datetime(1968, 4, 13), #2025
    datetime.datetime(1969, 4, 13), #2026
    datetime.datetime(1970, 4, 14), #2027
    datetime.datetime(1971, 4, 14), #2028
    datetime.datetime(1972, 4, 13), #2029
    datetime.datetime(1973, 4, 13), #2030
    datetime.datetime(1974, 4, 14), #2031
    datetime.datetime(1975, 4, 14), #2032
    datetime.datetime(1976, 4, 13), #2033
    datetime.datetime(1977, 4, 13), #2034
    datetime.datetime(1978, 4, 14), #2035
    datetime.datetime(1979, 4, 14), #2036
    datetime.datetime(1980, 4, 13), #2037
    datetime.datetime(1981, 4, 13), #2038
    datetime.datetime(1982, 4, 14), #2039
    datetime.datetime(1983, 4, 14), #2040
    datetime.datetime(1984, 4, 13), #2041
    datetime.datetime(1985, 4, 13), #2042
    datetime.datetime(1986, 4, 14), #2043
    datetime.datetime(1987, 4, 14), #2044
    datetime.datetime(1988, 4, 13), #2045
    datetime.datetime(1989, 4, 13), #2046
    datetime.datetime(1990, 4, 14), #2047
    datetime.datetime(1991, 4, 14), #2048
    datetime.datetime(1992, 4, 13), #2049
    datetime.datetime(1993, 4, 13), #2050
    datetime.datetime(1994, 4, 14), #2051
    datetime.datetime(1995, 4, 14), #2052
    datetime.datetime(1996, 4, 13), #2053
    datetime.datetime(1997, 4, 13), #2054
    datetime.datetime(1998, 4, 14), #2055
    datetime.datetime(1999, 4, 14), #2056
    datetime.datetime(2000, 4, 13), #2057
    datetime.datetime(2001, 4, 14), #2058
    datetime.datetime(2002, 4, 14), #2059
    datetime.datetime(2003, 4, 14), #2060
    datetime.datetime(2004, 4, 13), #2061
    datetime.datetime(2005, 4, 14), #2062
    datetime.datetime(2005, 4, 14), #2063
    datetime.datetime(2007, 4, 14), #2064
    datetime.datetime(2008, 4, 13), #2065
    datetime.datetime(2009, 4, 14), #2066
    datetime.datetime(2010, 4, 14), #2067
    datetime.datetime(2011, 4, 14), #2068
    datetime.datetime(2012, 4, 13), #2069
    datetime.datetime(2013, 4, 14), #2070
    datetime.datetime(2014, 4, 14), #2071
    datetime.datetime(2015, 4, 14), #2072
    datetime.datetime(2016, 4, 13), #2073
    datetime.datetime(2017, 4, 14), #2074
    datetime.datetime(2018, 4, 14), #2075
    datetime.datetime(2019, 4, 14), #2076
    datetime.datetime(2020, 4, 13), #2077
    datetime.datetime(2021, 4, 14), #2078
    datetime.datetime(2022, 4, 14), #2079
    datetime.datetime(2023, 4, 14), #2080
    datetime.datetime(2024, 4, 13), #2081
    datetime.datetime(2025, 4, 14), #2082
    datetime.datetime(2026, 4, 14), #2083
    datetime.datetime(2027, 4, 14), #2084
    datetime.datetime(2028, 4, 13), #2085
    datetime.datetime(2029, 4, 14), #2086
    datetime.datetime(2030, 4, 14), #2087
    datetime.datetime(2031, 4, 15), #2088
    datetime.datetime(2032, 4, 14), #2089
    datetime.datetime(2033, 4, 14), #2090
    datetime.datetime(2034, 4, 14), #2091
    datetime.datetime(2035, 4, 13), #2092
    datetime.datetime(2036, 4, 14), #2093
    datetime.datetime(2037, 4, 14), #2094
    datetime.datetime(2038, 4, 14), #2095
    datetime.datetime(2039, 4, 15), #2096
    datetime.datetime(2040, 4, 13), #2097
    datetime.datetime(2041, 4, 14), #2098
    datetime.datetime(2042, 4, 14), #2099
    datetime.datetime(2043, 4, 14)  #2100
]

def bs2ad(year, month, day):
    """
    Convert BS date to AD date, valid date range 1970/1/1 to 2100/12/30.
    Returns python datetime object.
    """
    if year < startBSYear or year > (startBSYear + len(newYearBS) - 1) :
        raise Exception

    if month < 1 or month > 12:
        raise Exception

    offset = year - startBSYear

    newYearDayAD = newYearBS[offset]
    daysInCurrentBSMonths = daysInBSMonths[offset]

    if day < 1 or day > daysInCurrentBSMonths[month - 1]:
        #print(daysInCurrentBSMonths)
        #print(daysInCurrentBSMonths[month - 1])
        raise Exception

    dayDelta = 0
    for i in range(0, month-1):
        dayDelta += daysInCurrentBSMonths[i]
    dayDelta += day

    timeDelta = datetime.timedelta(days=dayDelta-1)

    return newYearDayAD + timeDelta


def ad2bs(date):
    """
    Convert AD date to BS date, valid date range 1913/4/13 to 2044/04/12.
    Returns a tuple in the form (year, month, day)
    """

    bsYear = 0
    currentnewYearDayAD = None
    for i, newYearDayAD in reversed(list(enumerate(newYearBS))):
        if date >= newYearDayAD:
            bsYear = i+startBSYear
            currentnewYearDayAD = newYearDayAD
            break

    if currentnewYearDayAD == None:
        raise Exception

    timeDelta = date - currentnewYearDayAD
    timeDeltaDays = timeDelta.days

    offset = bsYear - startBSYear

    daysInCurrentBSMonths = daysInBSMonths[offset]

    bsMonth = None
    bsDay = None
    for i in range(0, len(daysInCurrentBSMonths)):
        currentDays = daysInCurrentBSMonths[i]
        if timeDeltaDays < daysInCurrentBSMonths[i]:
            bsMonth = i + 1
            bsDay = timeDeltaDays + 1
            break

        timeDeltaDays -= daysInCurrentBSMonths[i]

    if bsMonth == None:
        raise Exception

    return (bsYear, bsMonth, bsDay)


def convert_file(filename):
    with open(filename) as f:
        for line in f:
            str_date_bs = line.strip()
            year, month, day = tuple(str_date_bs.split("/"))
            print("{0}".format(bs2ad(int(year), int(month), int(day)).strftime("%Y/%m/%d")))
            
            
def convert_ad2bs(date_str):
    date_array = date_str.split("/")
    
    if not(len(date_array) == 3):
        print("{} invalid date formate")
        return
        
    date_input = datetime.datetime(
        int(date_array[0]),
        int(date_array[1]),
        int(date_array[2])
    )
    
    date_bs = ad2bs(date_input)
    
    print("{:04d}/{:02d}/{:02d} AD => {:04d}/{:02d}/{:02d} BS".format(
        date_input.year,
        date_input.month,
        date_input.day, 
        date_bs[0],
        date_bs[1],
        date_bs[2]
    ))

def convert_bs2ad(date_str):
    date_array = date_str.split("/")
    
    if not(len(date_array) == 3):
        print("{} invalid date formate")
        return
    
    date_ad = bs2ad(
        int(date_array[0]),
        int(date_array[1]),
        int(date_array[2])
    )
    
    print("{:04d}/{:02d}/{:02d} BS => {:04d}/{:02d}/{:02d} AD".format(
        int(date_array[0]),
        int(date_array[1]),
        int(date_array[2]), 
        date_ad.year,
        date_ad.month,
        date_ad.day
    ))


def _license():
    print("BS to AD Converter")
    print("--------------------------------")
    print("Copyright (C) 2017 Ali Aafee")
    print("")


def _usage():
    _license()
    print( "Usage:")
    print( "    -h, --help")
    print( "       Displays this help")
    print( "    -d, --datead")
    print( "       Date in Gregorian YYYY/MM/DD.")
    #print( "    -b, --datebs") #TODO: Implement This
    #print( "       Date in Bikram Sambath YYYY/MM/DD.")
    print( "    -i, --inputfile")
    print( "       Plain text file with each line containing")
    print( "       BS date in the format YYYY/MM/DD, valid")
    print( "       date range 1970/1/1 to 2100/12/30")
    print( " ")
            
    
def _main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:b:i:", ["help", "datead=", "datebs=", "input="])
    except getopt.GetoptError:
        _usage()
        sys.exit(2)
    
    date_ad = None
    date_bs = None
    input_file = None
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            _usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-d", "--datead"):
            date_ad = arg
        elif opt in ("-b", "--datebs"):
            date_bs = arg
            
    if date_ad is not None:
        convert_ad2bs(date_ad)
        sys.exit()

    if date_bs is not None:
        convert_bs2ad(date_bs)
        sys.exit()
        
    if input_file is None:
        _usage()
        sys.exit()

    convert_file(input_file)



if __name__ == '__main__':
    _main(sys.argv[1:])

