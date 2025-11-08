# How to create RDD

#    1) parallelize


'''from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()


rdd=sc.parallelize([1,5,7,8,10,'hadoop','spark','bigdata'])
rdd.foreach(print)'''


#................................................................

#  list to RDD

'''from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()

rdd=sc.parallelize({2,3,4,5,2,3,4})

rdd.foreach(print)'''

#..................................................................

#  dictionary to RDD


from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
dic={"id":101,"fname":'harisanker',"lname":'v'}
rdd=sc.parallelize(dic)

rdd.foreach(print)































