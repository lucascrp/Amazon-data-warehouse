"""
ETL Step 2: Transform and clean DataFrames, build star schema tables
"""
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, upper, trim, when

def create_spark(app_name="etl-transform"):
    return SparkSession.builder.appName(app_name).getOrCreate()

def clean_product(df):
    return df.withColumn("category", upper(trim(col("category")))) \
             .withColumn("product_name", trim(col("product_name")))

def clean_location(df):
    return df.withColumn("warehouse_name", trim(col("Warehouse")))

def clean_supplier(df):
    return df.withColumn("supplier_name", trim(col("SupplierName")))

def clean_time(df):
    return df.withColumn("date_key", to_date(col("date"), "M/d/yyyy"))

def clean_inventory(df):
    return df.withColumn("Quantity_on_hand", col("Quantity_on_hand").cast("int")) \
             .withColumn("Stock_Movement", col("Stock_Movement").cast("int"))

def main():
    spark = create_spark()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, "data", "raw")
    proc_dir = os.path.join(base_dir, "data", "processed")
    os.makedirs(proc_dir, exist_ok=True)

    # Read raw parquet
    product = spark.read.parquet(os.path.join(raw_dir, "product"))
    location = spark.read.parquet(os.path.join(raw_dir, "location"))
    supplier = spark.read.parquet(os.path.join(raw_dir, "supplier"))
    time = spark.read.parquet(os.path.join(raw_dir, "time"))
    inventory = spark.read.parquet(os.path.join(raw_dir, "inventory"))

    # Clean
    product = clean_product(product)
    location = clean_location(location)
    supplier = clean_supplier(supplier)
    time = clean_time(time)
    inventory = clean_inventory(inventory)

    # Write cleaned tables
    product.write.mode("overwrite").parquet(os.path.join(proc_dir, "product"))
    location.write.mode("overwrite").parquet(os.path.join(proc_dir, "location"))
    supplier.write.mode("overwrite").parquet(os.path.join(proc_dir, "supplier"))
    time.write.mode("overwrite").parquet(os.path.join(proc_dir, "time"))
    inventory.write.mode("overwrite").parquet(os.path.join(proc_dir, "inventory"))
    spark.stop()

if __name__ == "__main__":
    main()
