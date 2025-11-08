'''from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.textFile('/home/harisanker/Downloads/Work_files/customer')
rdd.foreach(print)

print('x'*100)

word_data=rdd.map(lambda x:x.split(','))
word_data.foreach(print)

print('x'*100)

word_data1=word_data.map(lambda x:(x[4],1))
word_data1.foreach(print)

print('x'*100)

word_count=word_data1.reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
word_count.foreach(print)'''


from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.textFile('/home/harisanker/Downloads/Work_files/customer')
rdd.foreach(print)

print('x'*100)

word_data=rdd.flatMap(lambda x:x.split(','))
word_data.foreach(print)

print('x'*100)

word_data1=word_data.map(lambda x:(x[5],1))
word_data1.foreach(print)




