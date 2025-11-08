# countByValue

# to perform word_count directly from word by word data

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
rdd=sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/sample')
rdd.foreach(print)

rdd1=rdd.flatMap(lambda x:x.split(' '))
rdd1.foreach(print)

# syntax  :- new_relation_name=old_rdd_name.countByValue()

print('x'*100)

dic=rdd1.countByValue()
print(dic)















