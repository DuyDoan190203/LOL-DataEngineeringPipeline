from pyspark.sql import DataFrame
from pyspark.sql.functions import col, when, sum as spark_sum

def transform_data(df: DataFrame) -> DataFrame:
    """
    Transform the data by adding new columns and filtering out invalid rows.
    """
    df = df.withColumn("creationTime", (col("creationTime") / 1000).cast("timestamp"))

    categorize_game_duration = when(col("gameDuration") < 1500, "short") \
        .when(col("gameDuration") < 2000, "medium") \
        .otherwise("long")

    df = df.withColumn("game_length_category", categorize_game_duration)
    df = df.withColumn("t1_objective_control", 
                       col("firstBlood") + col("firstTower") + col("firstInhibitor") + col("firstBaron") + col("firstDragon"))
    df = df.filter(col("firstBaron") > 0)

    # Cache the DataFrame to optimize performance for subsequent actions
    df.cache()
    
    return df