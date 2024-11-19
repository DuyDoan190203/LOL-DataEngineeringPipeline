from pyspark.sql import DataFrame

def load_data(df: DataFrame, output_path: str) -> None:
    df.write.mode("overwrite").parquet(output_path)