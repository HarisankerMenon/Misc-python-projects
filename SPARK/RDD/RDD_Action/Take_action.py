#  Take

# to take only needed elements from an rdd

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
rdd=sc.parallelize(i for i in range(1,31))
rdd.foreach(print)

print('x'*100)

# syntax  :-new_variable_name=old_rdd_name.take(number of elements)

lst=rdd.take(5)
print(lst)