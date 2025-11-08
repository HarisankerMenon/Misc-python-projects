# reduse

# to calculate total sum

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
rdd=sc.parallelize(i for i in range(1,31))
rdd.foreach(print)

# syntax  :- new_relation_name=old_rdd_name.reduce(lambda x,y:x+y)

lst=rdd.reduce(lambda x,y:x+y)
print(lst)

