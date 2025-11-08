# text file to RDD

# e present ==> yes
# e not present==> no



from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile("/home/harisanker/PycharmProjects/SPARK/RDD/sample")
rdd.foreach(print)

print("x"*100)

rdd1=rdd.map(lambda x: 'yes' if 'e' in x else 'no' )
rdd1.foreach(print)