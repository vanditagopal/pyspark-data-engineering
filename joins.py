import os
from config import PYTHON_PATH

os.environ["PYSPARK_PYTHON"] = PYTHON_PATH
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON_PATH

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Joins") \
    .master("local[*]") \
    .getOrCreate()

employees_df = spark.read.csv("data/employees.csv", header=True, inferSchema=True)
departments_df = spark.read.csv("data/departments.csv", header=True, inferSchema=True)

print("=== Employees DataFrame ===")
employees_df.show()

print("=== Departments DataFrame ===")
departments_df.show()

#Inner Join
print("=== Inner Join ===")


employees_df.join(
    departments_df,
    on="dept_id",
    how="inner"
).show()

#Left Join
print("=== LEFT JOIN ===")

employees_df.join(
    departments_df,
    on="dept_id",
    how="left"
).show()

# RIGHT JOIN
print("=== RIGHT JOIN ===")

employees_df.join(
    departments_df,
    on="dept_id",
    how="right"
).show()

# FULL OUTER JOIN
print("=== FULL OUTER JOIN ===")

employees_df.join(
    departments_df,
    on="dept_id",
    how="outer"
).show()

spark.stop()    
