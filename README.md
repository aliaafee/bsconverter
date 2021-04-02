# bsconverter

Bikram Sambat to Gregorian Date Converter
-----------------------------------------

Valid date range 1970/1/1 to 2100/12/30 AD.

Command line utility and library to convert dates in Bikram Sambat
to Gregorian format.

Use the -h switch to see the help for the command line utility which
can be used to convert dates from text files where each line contains
a Bikram Sambat dates in the format YYYY/MM/DD.

The python library can be used to include conversion functionality in
your python app. bs2ad(year, month, day) to get python date object, and 
ad2bs(date) to convert a python date object to bikram sambat.

Enjoy
