from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile("/home/harisanker/PycharmProjects/SPARK/RDD/sample")
rdd.foreach(print)

print("x"*100)

rdd1=rdd.flatMap(lambda x:x.split(' '))
rdd1.foreach(print)