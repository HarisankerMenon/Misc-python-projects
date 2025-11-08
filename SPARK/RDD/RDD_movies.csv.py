# movies.csv

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile("/home/harisanker/Downloads/movies.csv")

rdd.foreach(print)