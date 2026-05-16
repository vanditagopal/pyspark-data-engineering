import os 
from config import PYTHON_PATH
# this is done to tell spark which python executable to use for pyspark.


#this is used by the worker processes

os.environ["PYSPARK_PYTHON"] = PYTHON_PATH
#this is used by the driver process 
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON_PATH


#this will import the main entry point for Spark 
from pyspark.sql import SparkSession

#builder is used to configure spark 

#.appName -> this will set the name of the application 

#local -> this tells spark to run in local machine 

# local[*] -> this tells spark to use all the available cores in the local machine 

#.getOrCreate() -> this will create a new spark session if it does not exist, otherwise it will return the existing one.

#Spark data frame : 
# this is a distributed tabular like structure 

spark = SparkSession.builder \
    .appName("PySpark Test")\
    .master("local[*]") \
    .getOrCreate()


#data is a list of tuples, where each tuple represents a row of data. The first element of the tuple is the name and the second element is the age. We will create a DataFrame from this data and then show the contents of the DataFrame.

data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

# create dataframe 

#spark dataframes 
df = spark.createDataFrame(data, ["Name", "Age"])


#show the contents of the dataframe , it is an action

#Spark is lazy , untill an action is called, the transformations are not executed. When we call df.show(), it will trigger the execution of the transformations and show the contents of the dataframe.

df.show()

#shuts down the spark session, it is a good practice to stop the spark session after we are done with it. This will free up the resources used by the spark session.

spark.stop()