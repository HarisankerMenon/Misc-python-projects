import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
ss=SparkSession.builder.master("local[1]").appName("jan").getOrCreate()

emp=[(101,'arun','k',26,'bigdata',1000), \
     (102,'arjun','p',27,'python',1500), \
     (103,'vijay','s',29,'bigdata',1250), \
     (104,'amal','p',25,'python',1500), \
     (105,'vineeth','r',24,'bigdata',1750)]

colums=['empid','efname','elname','age','prof','salary']


# dataframe

# dataframe_name= sparaksession_name.createDataFrame(data=datavariable_name,schema=variable name)


df=ss.createDataFrame(data=emp,schema=colums)
df.show()# only print defalt only 20 rows

# count no of row

print(df.count())

df.show(3)

# print schema

df.printSchema()

#............................................................

# add new columns in data frame

# syntax  :- new_dataframe_name=old_dataframe_name.withColumn("newcolname","value")
# lit :- to add same values in a dataframe


# new column add == designation
# bonus :- 10% of salary
# fixed_salary

df1=df.withColumn("Designation",lit("software_engineer"))\
      .withColumn("bonus",col("salary")/10)\
      .withColumn("fixed_salary",col("salary")+500)\
      .withColumn("fixed_salary",col("fixed_salary")+100) # alter existing col
df1.show()

#........................................................................................


# change name of a col in a dataframe

#  withColumnRenamed :- .withColumnRename("oldcolname","newcolname")


df2=df1.withColumnRenamed("fixed_salary","total_salary")
df2.show()


#...........................................................................

# select(operator) :- to select needed col

# eg :- empid,efname,age,prof,total_salary

df3=df2.select("empid","efname","elname","prof","total_salary")
df3.show()


#.............................................................................

# to delete a col

# drop(operator)  :- to delete a col

# syntax :- new df name=old df name.drop("col name")

df4=df1.drop("bonus")
df4.show()


#..............................................................................

# filter

# used to collect needed data from a df to a new data frame

# syntax  :- new df name = old df name.filter(col("col name")condition)

df6=df1.filter(col("salary")>'1500')
df6.show()

df7=df1.filter(col("age")>'25').select("empid","efname","age","salary","fixed_salary").show()


df8=df1.filter((col("salary")>'1500')&(col("age")>'25')).show()
