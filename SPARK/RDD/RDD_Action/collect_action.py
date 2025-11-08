# collect

# converting an rdd into a python list


from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
rdd=sc.parallelize(i for i in range(1,31))
rdd.foreach(print)

print('x'*100)

# syntax  :- new_variablename=oldrdd_name.collect()

collect_data=rdd.collect()
print(collect_data)























