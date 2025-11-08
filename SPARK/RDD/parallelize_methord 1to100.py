# create rdd of 1 to 100

'''from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize([i for i in range(1,101)])

rdd.foreach(print)'''



# 1 to 100 even numbers

'''from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize([i for i in range(1,101) if i%2==0])

rdd.foreach(print)'''


# 1to 100 , number even print square, number odd print number :-

# pari RDD

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize([(i,i**2) if i%2==0 else i for i in range(1,101)])

rdd.foreach(print)