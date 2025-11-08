# 1)calculate each file word count [count dec]

from pyspark import SparkContext
sc=SparkContext(master='local',appName='jan').getOrCreate()
spark_core=sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/sparkcore')
spark_sql=sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/spark_SQL')
spark_streaming=sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/spark_streaming')
ml=sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/sparkMLIB')
graphx=sc.textFile('/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/GraphX')

spark_core.foreach(print)
print('--'*150)

rdd1=spark_core.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd1.foreach(print)
print('--'*150)
rdd2=spark_sql.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd2.foreach(print)
print('--'*150)
rdd3=spark_streaming.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd3.foreach(print)
print('--'*150)
rdd4=ml.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd4.foreach(print)
print('--'*150)
rdd5=graphx.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
rdd5.foreach(print)
print('--'*150)



#2)collect top 5 words from each file

lim1=rdd1.take(5)
print(lim1)
print('--'*150)
lim2=rdd2.take(5)
print(lim2)
print('--'*150)
lim3=rdd3.take(5)
print(lim3)
print('--'*150)
lim4=rdd4.take(5)
print(lim4)
print('--'*150)
lim5=rdd5.take(5)
print(lim5)
print('--'*150)




# 3)collect words count above 5 data

fil1=rdd1.filter(lambda x:x[1]>5)
fil1.foreach(print)
print('--'*150)
fil2=rdd2.filter(lambda x:x[1]>5)
fil2.foreach(print)
print('--'*150)
fil3=rdd3.filter(lambda x:x[1]>5)
fil3.foreach(print)
print('--'*150)
fil4=rdd4.filter(lambda x:x[1]>5)
fil4.foreach(print)
print('--'*150)
fil5=rdd5.filter(lambda x:x[1]>5)
fil5.foreach(print)
print('--'*150)



# 4)combine all file then find word count[dec order]
print('Q',4)
combine=rdd1.union(rdd2).union(rdd3).union(rdd4).union(rdd5).reduceByKey(lambda x,y:x+y).sortBy(lambda x:x[1],ascending=False)
combine.foreach(print)
print('--'*150)

# 5)top 3 words
print('Q',5)
lim6=combine.take(3)
print(lim6)
print('--'*150)

print ("h")







































