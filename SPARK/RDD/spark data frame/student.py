import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss=SparkSession.builder.master("local[1]").appName("jan").getOrCreate()

st=[(101,'vinay',25,40,45), \
     (102,'amal',40,32,35), \
     (103,'arjun',50,43,20), \
     (104,'vineeth',40,45,32), \
     (105,'aneesh',40,41,21), \
     (106,'ravi',50,20,35), \
     (107,'rohith',20,30,45)]

colums=['id','name','sub1','sub2','sub3']


df=ss.createDataFrame(data=st,schema=colums)
df.show()


df1=df.withColumn("Total_mark",col("sub1")+col("sub2")+col("sub3"))
df1.show()


df2=df1.filter((col("sub3")>'40')&(col("Total_mark")>='80')).select("id","name","sub3","Total_mark").show()

















