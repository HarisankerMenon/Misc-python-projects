# vowels



'''from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.textFile("/home/harisanker/PycharmProjects/SPARK/RDD/sample")
rdd.foreach(print)

print("x"*100)

rdd1=rdd.flatMap(lambda x:x.split(' '))
rdd1.foreach(print)


print("x"*100)
vowels='aeiouAEIOU'

rdd2=rdd1.map(lambda x: (x,[1 if c in vowels else 0 for c in x]))
rdd2.foreach(print)
'''


#vowels count



from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.textFile("/home/harisanker/PycharmProjects/SPARK/RDD/sample")
rdd.foreach(print)

print("x"*100)

rdd1=rdd.flatMap(lambda x:x.split(' '))
rdd1.foreach(print)


print("x"*100)
vowels='aeiouAEIOU'

rdd2=rdd1.map(lambda x: (x,sum([1 if c in vowels else 0 for c in x])))
rdd2.foreach(print)














