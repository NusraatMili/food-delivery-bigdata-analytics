from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, concat, regexp_extract
from pyspark.sql.functions import hour, to_timestamp

import os

# 1. Start Spark
spark = SparkSession.builder \
    .appName("Food Delivery Big Data Analysis") \
    .getOrCreate()


# 2. File Paths
input_path = "C:/Users/User/OneDrive/Documents/big-data-projects/food-delivery-bigdata/data/food_delivery.csv"
output_folder = "C:/Users/User/OneDrive/Documents/big-data-projects/food-delivery-bigdata/output"

os.makedirs(output_folder, exist_ok=True)


# 3. Load Dataset
df = spark.read.option("header", True).csv(input_path)

print("Dataset Schema:")
df.printSchema()


# 4. Data Cleaning

# Rename problematic column
df = df.withColumnRenamed("Time_taken(min)", "delivery_time_raw")

# Extract numeric value from text like "30 (min)"
df = df.withColumn(
    "delivery_time",
    regexp_extract(col("delivery_time_raw"), r'\d+', 0).cast("int")
)

# Remove invalid/null rows
df = df.filter(col("delivery_time").isNotNull())

# 5. Analysis

# Average delivery time by city
avg_time_by_city = df.groupBy("City").agg(
    avg(col("delivery_time")).alias("avg_delivery_time")
)

# Total orders by city
orders_by_city = df.groupBy("City").count() \
    .withColumnRenamed("count", "total_orders")


# Top Restaurants
top_restaurants = df.groupBy(
    concat(
        col("Restaurant_latitude"),
        col("Restaurant_longitude")
    ).alias("restaurant_id")
).count().withColumnRenamed("count", "total_orders") \
 .orderBy(col("total_orders").desc()) \
 .limit(10)

# FIXED FORMAT
df = df.withColumn(
    "order_time",
    to_timestamp(col("Time_Orderd"), "HH:mm:ss")   
)

orders_by_time = df.filter(col("order_time").isNotNull()) \
    .groupBy(hour(col("order_time")).alias("order_hour")) \
    .count() \
    .withColumnRenamed("count", "total_orders") \
    .orderBy("order_hour")


# 6. Show Results (CMD)
print("\n Average Delivery Time by City:")
avg_time_by_city.show()

print("\n Total Orders by City:")
orders_by_city.show()

print("\n Top Restaurants:")
top_restaurants.show()

print("\n Orders by Hour:")
orders_by_time.show()

# 7. Save Results (CSV)
avg_time_by_city.toPandas().to_csv(
    os.path.join(output_folder, "avg_time_by_city.csv"),
    index=False
)

orders_by_city.toPandas().to_csv(
    os.path.join(output_folder, "orders_by_city.csv"),
    index=False
)

top_restaurants.toPandas().to_csv(
    os.path.join(output_folder, "top_restaurants.csv"),
    index=False
)

orders_by_time.toPandas().to_csv(
    os.path.join(output_folder, "orders_by_time.csv"),
    index=False
)

print("top_restaurants.csv saved")
print("orders_by_time.csv saved")
print("\n✅ Files saved successfully in output folder!")

# 8. Stop Spark
spark.stop()
