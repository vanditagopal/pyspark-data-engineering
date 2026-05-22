import os
import sys

from config import PYTHON_PATH

os.environ["PYSPARK_PYTHON"] = PYTHON_PATH
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON_PATH

from pyspark.sql import SparkSession

from pyspark.sql.functions import(
    col, sum, avg, count, max, min)

spark=SparkSession.builder \
    .appName("PySpark Aggregations")\
    .master("local[*]") \
    .getOrCreate()

df=spark.read.csv("data/employee_salary.csv", header=True, inferSchema=True)


print("=== Original DataFrame ===")
df.show()

#Group by department 

print("=== Average Salary by Department ===")

df.groupBy("department").avg("salary").show()


print("=== Department Salary Statistics ===")


df.groupBy("department").agg(
        avg("salary").alias("avg_salary"),
        sum("salary").alias("total_salary"),
        count("salary").alias("employee_count"),
        max("salary").alias("max_salary"),
        min("salary").alias("min_salary")
).show()

spark.stop()


