# countByKey
# to find wordcount from a pair rdd

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
rdd=sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/sample')
rdd.foreach(print)

print('x'*100)

rdd1=rdd.flatMap(lambda x:x.split(' '))
rdd1.foreach(print)

print('x'*100)

rdd2=rdd1.map(lambda x:(x,1))
rdd2.foreach(print)

# syntax :- new_relation_name=old_rdd_name.countByKey()

dic=rdd2.countByKey()
print(dic)
