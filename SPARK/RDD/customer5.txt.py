from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd = sc.textFile('/home/harisanker/Downloads/customer5.txt')
rdd.foreach(print)

print('x'*100)

rdd1=rdd.map(lambda x:x.split(' '))
rdd1.foreach(print)

# age 2 incriment

print('x'*100)

rdd2=rdd1.map(lambda x:(x[0:2],int(x[3]+2)))
rdd2.foreach(print)
print(rdd2)