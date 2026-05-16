import os 
from config import PYTHON_PATH

os.environ["PYSPARK_PYTHON"] = PYTHON_PATH
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON_PATH

from pyspark.sql import SparkSession
from pyspark.sql.functions import col,isnull

spark=SparkSession.builder \
    .appName("PySpark Test")\
    .master("local[*]") \
    .getOrCreate()

df=spark.read.csv("data/employees_with_nulls.csv",
                    header=True,
                    inferSchema=True)

print("===Original DataFrame===")

df.show()

print("=== Rows with Null Values===")

df.filter(col("salary").isNull()).show()

"""
Spark:

creates a NEW temporary DataFrame
removes null rows
shows result

BUT…

You did NOT save it.

So original df remains unchanged.
"""
print("=== Drop Null Rows===")

df.dropna().show()

print("=== Fill Null Values with 0===")

df.fillna({"salary":0}).show()


print("=== Fill Multiple Null Values ===")

df.fillna({
    "department": "Unknown",
    "name": "No Name",
    "age": 0
}).show()
