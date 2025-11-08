# customer



from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile("/home/harisanker/Downloads/customer")

rdd.foreach(print)
