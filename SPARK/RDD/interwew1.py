from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.parallelize([2,3,4])
rdd.foreach(print)

print("x"*100)

rdd1=rdd.flatMap(lambda x:range(1,x))
rdd1.foreach(print)



print("x"*100)

rdd1=rdd.map(lambda x:range(1,x))
rdd1.foreach(print)





















