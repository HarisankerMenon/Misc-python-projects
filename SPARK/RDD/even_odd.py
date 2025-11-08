# 1 to 30
# even: square
# odd : cube



from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize([i for i in range(1,31)])

rdd.foreach(print)

rdd1=rdd.map(lambda x:(x,x**2) if x%2==0 else (x,x**3))
rdd1.foreach(print)