from pyspark.sql import SparkSession
import time

def create_spark_session():
    return (SparkSession.builder
            .appName("fraud-detection")
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            .getOrCreate())

def main():
    print("Starting Spark application...")
    
    # Create Spark session
    spark = create_spark_session()
    
    print(f"Created Spark session version: {spark.version}")
    
    # Keep the application running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        spark.stop()

if __name__ == "__main__":
    main() 