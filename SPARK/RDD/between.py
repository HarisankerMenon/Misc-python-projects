# 1 to 50 element
# 1 to 15 : small
# 16 to 30 :medium
# above 30 : large

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize([i for i in range(1,51)])

rdd.foreach(print)

rdd1=rdd.map(lambda x:(x,'small') if x<=15 else (x,'medium') if 15<x<=30 else (x,'large'))
rdd1.foreach(print)
