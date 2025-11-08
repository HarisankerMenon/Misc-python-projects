# union_intersection

# rdd 1 = 1 to 30
# rdd2 = 10 to 50

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd1=sc.parallelize([i for i in range(1,31)])
rdd1.foreach(print)

print('x'*100)

rdd2=sc.parallelize([i for i in range(10,51)])
rdd2.foreach(print)

print('x'*100)



# union

# syntax :- newrdd_name=oldrdd_name.union(2nd rdd_name)

union_data=rdd1.union(rdd2)
union_data.foreach(print)

print('x'*100)

union_data1=rdd1.union(rdd2).distinct()
union_data1.foreach(print)


# intersection

# syntax :- newrdd_name=oldrdd_name.intersection(2nd rdd_name)



inter_data=rdd1.intersection(rdd2)
inter_data.foreach(print)








