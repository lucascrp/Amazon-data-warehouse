"""
ETL Step 3: Write star schema tables to Parquet/Delta, with partitioning
"""
import os
from pyspark.sql import SparkSession

def create_spark(app_name="etl-write"):
    return SparkSession.builder.appName(app_name).getOrCreate()

def main():
    spark = create_spark()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    proc_dir = os.path.join(base_dir, "data", "processed")
    out_dir = os.path.join(base_dir, "data", "star")
    os.makedirs(out_dir, exist_ok=True)

    # Read processed tables
    product = spark.read.parquet(os.path.join(proc_dir, "product"))
    location = spark.read.parquet(os.path.join(proc_dir, "location"))
    supplier = spark.read.parquet(os.path.join(proc_dir, "supplier"))
    time = spark.read.parquet(os.path.join(proc_dir, "time"))
    inventory = spark.read.parquet(os.path.join(proc_dir, "inventory"))

    # Example: join inventory with product and time for a fact table
    fact = inventory.join(product, inventory.ProductID == product.productID, "left") \
                    .join(time, inventory.DateID == time.date, "left")
    # Partition by year/month if available
    if "year" in fact.columns and "month" in fact.columns:
        fact.write.mode("overwrite").partitionBy("year", "month").parquet(os.path.join(out_dir, "fact_inventory"))
    else:
        fact.write.mode("overwrite").parquet(os.path.join(out_dir, "fact_inventory"))
    print("Fact table written to star schema directory.")
    spark.stop()

if __name__ == "__main__":
    main()
