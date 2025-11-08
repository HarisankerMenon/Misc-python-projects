from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.textFile('/home/harisanker/Downloads/Work_files/sample.txt')
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

print('x'*100)

word_sort=word_count.sortBy(lambda x:x[1], ascending=False)
word_sort.foreach(print)


print('x'*100)

count_data=word_count.filter(lambda x:x[1]>50)
count_data.foreach(print)













