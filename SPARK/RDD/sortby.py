# sortBy

# syntax
# new_rdd_name=oldrddname.sortBy(condition)


from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile('/home/harisanker/Downloads/sample4.txt')
rdd.foreach(print)

print('x'*100)

rdd1=rdd.map(lambda x:x.split(','))
rdd1.foreach(print)

print('x'*100)

# ascending orderr

rdd2=rdd1.sortBy(lambda x:x[3])
rdd2.foreach(print)


# descending order

print('x'*100)

rdd2=rdd1.sortBy(lambda x:x[3], ascending=False)
rdd2.foreach(print)













