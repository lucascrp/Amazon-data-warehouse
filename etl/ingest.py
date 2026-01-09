"""
ETL Step 1: Ingest raw CSV files into Spark DataFrames and write as raw Parquet
"""
import os
from pyspark.sql import SparkSession

def create_spark(app_name="etl-ingest"):
    return SparkSession.builder.appName(app_name).getOrCreate()

def ingest_csv_to_parquet(spark, input_path, output_path, **read_opts):
    df = spark.read.option("header", True).csv(input_path, **read_opts)
    df.write.mode("overwrite").parquet(output_path)
    print(f"Ingested {input_path} → {output_path} ({df.count()} rows)")
    return df

def main():
    spark = create_spark()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_dir = os.path.join(base_dir, "Dimensions")
    out_dir = os.path.join(base_dir, "data", "raw")
    os.makedirs(out_dir, exist_ok=True)

    files = {
        "product": (os.path.join(src_dir, "Product-dimension.csv"), os.path.join(out_dir, "product")),
        "location": (os.path.join(src_dir, "Location-dimension.csv"), os.path.join(out_dir, "location")),
        "supplier": (os.path.join(src_dir, "Supplier-dimension.csv"), os.path.join(out_dir, "supplier")),
        "time": (os.path.join(src_dir, "Time-dimension.csv"), os.path.join(out_dir, "time")),
        "inventory": (os.path.join(src_dir, "Inventory-Fact.csv"), os.path.join(out_dir, "inventory")),
    }
    for name, (src, dest) in files.items():
        ingest_csv_to_parquet(spark, src, dest)
    spark.stop()

if __name__ == "__main__":
    main()
