import os 
from config import PYTHON_PATH

os.environ["PYSPARK_PYTHON"] = PYTHON_PATH
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON_PATH

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark=SparkSession.builder \
    .appName("PySpark Test")\
    .master("local[*]") \
    .getOrCreate()


df=spark.read.csv("data/employees.csv",
                  header=True,
                  inferSchema=True)

print("===Original DataFrame===")

df.show()


print("===Selected Columns===")

df.select("name","salary").show()


print("===Filter Columns===")

df.filter(col("salary")>50000).show()


print ("==== Average Salary ====")

df.groupBy("department").avg("salary").show()


print ("=== Order by Salary ====")

df.orderBy(col("salary").desc()).show


spark.stop()
