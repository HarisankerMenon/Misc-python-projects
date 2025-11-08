from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/sample')
rdd.foreach(print)

print('x'*100)

rdd1=rdd.filter(lambda x:x.startswith('i'))
rdd1.foreach(print)

print('x'*100)

rdd2=rdd.flatMap(lambda x:x.split(' '))
rdd2.foreach(print)

vowels='aeiouAEIOU'

rdd3=rdd2.map(lambda x:(x,sum(1 if c in vowels else 0 for c in x)))
rdd4=rdd3.filter(lambda x:x[1]>2)
rdd4.foreach(print)






















