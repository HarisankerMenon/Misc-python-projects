from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.parallelize([2,2,3,3,4,4,5,5,6,7,8,9,10,9,10])
rdd.foreach(print)

print('x'*100)

# distinct :- operator used for removing rows or values in rdd


# syntax
# newrdd_name=oldrddname.distinct()

rdd1=rdd.distinct()
rdd1.foreach(print)
