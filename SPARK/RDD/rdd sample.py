# sample

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

# textFile:- operation used to create a RDD from a textfile (textFile "F" capital)

rdd = sc.textFile("/home/harisanker/PycharmProjects/SPARK/RDD/sample")

rdd.foreach(print)






























