# 1 to 30

'''from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize([i for i in range(1,31)])

rdd.foreach(print)



# map : (tarnsformatiom)

# creating new RDD for each element in old RDD

# syntax :- newrddname=oldrddname.Map(condition)

rdd1=rdd.map(lambda x:x+1)
rdd1.foreach(print)'''




# 1 to 50


'''from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize([i for i in range(1,51)])

rdd.foreach(print)

rdd1=rdd.map(lambda x:x**2)
rdd1.foreach(print)'''


# 1 to 40

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize([i for i in range(1,41)])

rdd.foreach(print)

rdd1=rdd.map(lambda x:'even' if x%2==0 else 'odd')
rdd1.foreach(print)

