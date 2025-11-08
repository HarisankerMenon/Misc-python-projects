# 1 to 50


from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.parallelize(i for i in range(1,51))
rdd.foreach(print)

print("x"*100)

rdd1=rdd.filter(lambda x:x%2==1)
rdd1.foreach(print)


print("x"*100)

rdd2=rdd.filter(lambda x:x%2==0)
rdd2.foreach(print)

print("x"*100)

rdd3=rdd2.map(lambda x:x**2)
rdd3.foreach(print)


















