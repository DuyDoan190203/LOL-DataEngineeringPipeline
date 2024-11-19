import pytest
from pyspark.sql import SparkSession
from src.jobs.extract import extract_data
from src.jobs.transform import transform_data
from src.jobs.load import load_data

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.appName("test").getOrCreate()

def test_extract_data(spark):
    url = 'https://github.com/DuyDoan190203/Datasets-for-DE-and-ML/releases/download/games/lol_rank_games.csv.gz'
    local_path = '/tmp/lol_rank_games.csv.gz'
    df = extract_data(spark, url, local_path)
    assert df.count() > 0

def test_transform_data(spark):
    url = 'https://github.com/DuyDoan190203/Datasets-for-DE-and-ML/releases/download/games/lol_rank_games.csv.gz'
    local_path = '/tmp/lol_rank_games.csv.gz'
    df = extract_data(spark, url, local_path)
    transformed_df = transform_data(df)
    assert "game_length_category" in transformed_df.columns
    assert "t1_objective_control" in transformed_df.columns
    assert transformed_df.filter(transformed_df["firstBaron"] == 0).count() == 0

def test_load_data(spark):
    url = 'https://github.com/DuyDoan190203/Datasets-for-DE-and-ML/releases/download/games/lol_rank_games.csv.gz'
    local_path = '/tmp/lol_rank_games.csv.gz'
    df = extract_data(spark, url, local_path)
    transformed_df = transform_data(df)
    load_data(transformed_df, "path/to/output")
    loaded_df = spark.read.parquet("path/to/output")
    assert loaded_df.count() == transformed_df.count()