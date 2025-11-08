# filter

# rdd will convert into new rdd when the filter condition satisfy


# syntax

#  new_rdd_name = old_rdd.filter(condition)


# 1 to 30

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize(i for i in range(1,31))
rdd.foreach(print)

print("x"*100)



rdd1=rdd.filter(lambda x:x%2==0)
rdd1.foreach(print)






















