# customer5.txt


from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile('/home/harisanker/Downloads/customer5.txt')
rdd.foreach(print)

print('x'*100)

rdd1=rdd.filter(lambda x:x[5]=='india')
rdd1.foreach(print)