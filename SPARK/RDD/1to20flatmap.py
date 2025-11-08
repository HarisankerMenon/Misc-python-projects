from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize(i for i in range(1,21))
rdd.foreach(print)

print("x"*100)

rdd1=rdd.map(lambda x:[x,x+1,x**2])
rdd1.foreach(print)

print("x"*100)

rdd2=rdd1.flatMap(lambda x:x)
rdd2.foreach(print)
