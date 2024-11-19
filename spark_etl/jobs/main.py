from pyspark.sql import SparkSession
from src.jobs.extract import extract_data
from src.jobs.transform import transform_data
from src.jobs.load import load_data

def main(input_url: str, local_path: str, output_path: str):
    spark = SparkSession.builder.appName("LOLDataPipeline").getOrCreate()
    df = extract_data(spark, input_url, local_path)
    transformed_df = transform_data(df)
    load_data(transformed_df, output_path)
    spark.stop()

if __name__ == "__main__":
    input_url = 'https://github.com/DuyDoan190203/Datasets-for-DE-and-ML/releases/download/games/lol_rank_games.csv.gz'
    local_path = '/tmp/lol_rank_games.csv.gz'
    output_path = 'path/to/output'
    main(input_url, local_path, output_path)