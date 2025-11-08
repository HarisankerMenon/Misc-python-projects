from data import Spark_Core
from data import Spark_SQL
from data import Spark_Mlib
from data import Spark_Streaming
from data import Graph_X
graphx = Graph_X() # Spark_Graph_X
core = Spark_Core() # Spark_Core
sql = Spark_SQL() # Spark_SQL
mlib = Spark_Mlib() # Spark_Mlib
stream = Spark_Streaming() # Spark_Streaming

# Spark_Core file Analysis
from pyspark import SparkContext
sc = SparkContext(master="local",appName="jan")
core_rdd = sc.parallelize(core)
count_core = core_rdd.map(lambda x : (x,1)).reduceByKey(lambda x,y:x+y)
sort_core = count_core.sortBy(lambda x:x[1],ascending=False)
top_five_core = sort_core.take(5)
count_above_five_core = count_core.filter(lambda x:x[1] > 5)
# count_above_five_core.foreach(print)

# Spark_SQL File Analysis
sql_rdd = sc.parallelize(sql)
count_sql = sql_rdd.map(lambda x : (x,1)).reduceByKey(lambda x,y:x+y)
sort_sql = count_sql.sortBy(lambda x:x[1],ascending=False)
top_five_sql = sort_sql.take(5)
count_above_five_sql = count_sql.filter(lambda x:x[1] > 5)

# Spark_Mlib File Analysis
mlib_rdd = sc.parallelize(mlib)
count_mlib = mlib_rdd.map(lambda x : (x,1)).reduceByKey(lambda x,y:x+y)
sort_mlib = count_mlib.sortBy(lambda x:x[1],ascending=False)
top_five_mlib = sort_mlib.take(5)
count_above_five_mlib = count_mlib.filter(lambda x:x[1] > 5)

# Spark_GraphX file Analysis
graphx_rdd = sc.parallelize(graphx)
count_graphx = graphx_rdd.map(lambda x : (x,1)).reduceByKey(lambda x,y:x+y)
sort_graphx = count_graphx.sortBy(lambda x:x[1],ascending=False)
top_five_graphx = sort_graphx.take(5)
count_above_five_graphx = count_graphx.filter(lambda x:x[1] > 5)

# Spark_Streaming File Analysis
stream_rdd = sc.parallelize(stream)
count_stream = stream_rdd.map(lambda x : (x,1)).reduceByKey(lambda x,y:x+y)
sort_stream = count_stream.sortBy(lambda x:x[1],ascending=False)
top_five_stream = sort_stream.take(5)
count_above_five_stream = count_stream.filter(lambda x:x[1] > 5)

# Combining all the Files
combined_data = core_rdd.union(sql_rdd).union(graphx_rdd).union(stream_rdd).union(mlib_rdd) # Combine files
count_combined_data = combined_data.map(lambda x:(x,1)).reduceByKey(lambda x,y : x+y).sortBy(lambda x:x[1],ascending=False) # 4. find word count (count in descending order)
top_three_words = count_combined_data.take(3) # 5.Collect Top 3 words


# Remove Stoping Words
def stopping_word_removal():
    f = open("/home/harisanker/Downloads/stop_words_english.txt","r")
    combined_data1 = combined_data.collect()
    new_combined_data = []
    stopping_words = []
    for i in f:
        data = i.rstrip("\n").split("\n")
        for j in data:
            data1 = j.rstrip("]").lstrip("[")
            stopping_words.append(data1)
    for i in combined_data1:
        if i not in stopping_words:
            new_combined_data.append(i)
    return new_combined_data

new_combined_data = stopping_word_removal()

# new_combined_data File Analysis after removing stopping words

combined_rdd = sc.parallelize(new_combined_data)
combined_rdd.foreach(print)
combined_rdd_count = combined_rdd.map(lambda x:(x,1)).reduceByKey(lambda x,y : x+y).sortBy(lambda x:x[1],ascending=False) # Word Count
combined_rdd_count.foreach(print)
























