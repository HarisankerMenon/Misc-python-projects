from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile('/home/harisanker/Downloads/sample4.txt')
rdd.foreach(print)

print('x'*100)

rdd1=rdd.map(lambda x:x.split(','))
rdd1.foreach(print)

print('x'*100)

rdd2=rdd1.filter(lambda x:x[5]=='chennai')
rdd2.foreach(print)


print('x'*100)

rdd3=rdd1.filter(lambda x:x[3]>'22')
rdd3.foreach(print)

print('x'*100)

rdd4=rdd1.filter(lambda x:x[3]>'22' and x[3]<'24')
rdd4.foreach(print)

print('x'*100)

rdd5=rdd1.filter(lambda x:x[5]=='chennai' and x[3]>'23')
rdd5.foreach(print)

