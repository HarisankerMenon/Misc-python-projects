# movies.csv

# 1) sort data by release year
# 2) 1975-2010 [year sort]
# 3) rating above 4 full data
# 4) rating above 3 and year above 2005


from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.textFile('/home/harisanker/Downloads/Work_files/movies.csv')
rdd.foreach(print)

print("x"*100)

rdd1=rdd.map(lambda x:x.split(','))
rdd1.foreach(print)

# 1)

rdd2=rdd1.sortBy(lambda x:x[2])
rdd2.foreach(print)

print('x'*100)

# 2)

rdd3=rdd.filter(lambda x: x[2]>='1975' and x[2]<='2010')
rdd3.foreach(print)

print('x'*100)

# 3)

rdd4=rdd.filter(lambda x: x[3]>'4')
rdd4.foreach(print)


# 4)

rdd5=rdd.filter(lambda x:x[3]>'5' and x[2]>'2005')
rdd5.foreach(print)















