# flatmap

# 2 dimentional array into 1 dimentional array


from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile("/home/harisanker/PycharmProjects/SPARK/RDD/sample")
rdd.foreach(print)

print("x"*100)

rdd1=rdd.map(lambda x:x.split(' '))
rdd1.foreach(print)


# syntax

# newrdd_name=oldrdd.flatmap(condition)
print("x"*100)

rdd2=rdd1.flatMap(lambda x:x)
rdd2.foreach(print)

































