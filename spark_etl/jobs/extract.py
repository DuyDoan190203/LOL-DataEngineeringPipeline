import requests
import gzip
import shutil
from pyspark.sql import SparkSession, DataFrame

def download_file(url: str, local_path: str) -> None:
    response = requests.get(url, stream=True)
    with open(local_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def extract_data(spark: SparkSession, url: str, local_path: str) -> DataFrame:
    download_file(url, local_path)
    with gzip.open(local_path, 'rb') as f_in:
        with open(local_path.replace('.gz', ''), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return spark.read.csv(local_path.replace('.gz', ''), header=True, inferSchema=True)