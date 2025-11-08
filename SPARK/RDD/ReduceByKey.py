# reduseByKey

# reduseByKey transformation used to group and reduse in spark

# syntax

# newrdd_name=oldrddname.reduceByKey(condition)

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/sample')
rdd.foreach(print)

print('x'*100)

word_data=rdd.flatMap(lambda x:x.split(' '))
word_data.foreach(print)

print('x'*100)

word_data1=word_data.map(lambda x:(x,1))
word_data1.foreach(print)

print('x'*100)

word_count=word_data1.reduceByKey(lambda x,y:x+y)
word_count.foreach(print)


