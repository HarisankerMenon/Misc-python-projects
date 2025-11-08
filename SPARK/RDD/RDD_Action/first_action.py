# first
# to collect first value

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
rdd=sc.parallelize(i for i in range(1,31))
rdd.foreach(print)

print('x'*100)

# syntax  :-new_ralation_name=old_rdd_name.first()

lst=rdd.first()
print(lst)

