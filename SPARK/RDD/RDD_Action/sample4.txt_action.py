from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
rdd=sc.textFile('/home/harisanker/Downloads/Work_files/sample4.txt')
rdd.foreach(print)

print('x'*100)


# 1) age above 23 data
rdd1=rdd.filter(lambda x:x[3]=='22')
rdd1.foreach(print)
'''age_lst=rdd1.take(3)
print(age_lst)'''


# 2) age above 23 location chennai

# 3) age max 2 employee fname,lname,age,loc

# 4) age min 1 employee fname,lname,age,loc















