def Spark_Core():
    f = open("/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/sparkcore", "r")
    new_data = []
    for i in f:
        data = i.split(" ")
        for j in data:
            data1 = j.rstrip(".").rstrip(",").rstrip(")").rstrip(";").lstrip("(").strip('"').strip(':').rstrip("[16]").rstrip("[17]").rstrip(".[2]")
            new_data.append(data1)
        return new_data

def Spark_SQL():
    new_data = []
    f = open("/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/spark_SQL", "r")
    for i in f:
        data = i.split(" ")

        for j in data:
            data1 = j.strip(",").rstrip(".").rstrip("]").lstrip("[").strip("(").strip(")").strip(",").rstrip(".[16")
            data1 = data1.replace("DataFrames,[a","DataFrames")
            new_data.append(data1)
    return new_data

def Spark_Mlib():
    new_data = []
    f = open("/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/sparkMLIB", "r")
    for i in f:
        data = i.split(" ")
        for j in data:
            data1 = j.rstrip(",").lstrip("(").rstrip(")").rstrip(".[24]").rstrip(":")
            new_data.append(data1)
    return new_data

def Spark_Streaming():
    new_data = []
    f = open("/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/spark_streaming","r")
    for i in f:
        data = i.split(" ")

        for j in data:
            data1 = j.rstrip(".").rstrip(".[22]").rstrip(",").rstrip(".[21]").rstrip(".[19][20]")
            new_data.append(data1)
    return new_data

def Graph_X():
    new_data = []
    f = open("/home/harisanker/PycharmProjects/SPARK/RDD/Assignment/GraphX","r")
    for i in f:
        data = i.split(" ")

        for j in data:
            data1 = j.rstrip(",").rstrip(".").rstrip(".[26]").rstrip("):").lstrip("(").rstrip(".[27]").rstrip(".[28]").rstrip(")")
            new_data.append(data1)
    return new_data