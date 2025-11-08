# spark_data_frame
#.................

# dataframe used for processing structured and semi_structured

# row oriented data like table structure

# spark sql(component) :- to perform semi structured and structured data

#.................................................................



# features of data frame

# 1) distributed
# 2) fault tolerance
# 3) speed
# 4) immutable
# 5) lazy evaluation


# spark session : entry point of spark

# syntax :-

import pyspark
from pyspark.sql import SparkSession
ss=SparkSession.builder.master("local[1]").appName("jan").getOrCreate()

#.............................................

# how to create a data frame

# 3 methods

# 1)manually
# 2)external data set
# 3)rdd to data frame


#   1) manually

# 101,arjun,t,26,bigdata
# 102,rahul,s,23,python

#   2) external data set

# customer,sample,movies.txt

#   3) rdd to data frame



























