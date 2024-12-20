from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    bucket_name = 'mage-lol-rank-games-derek-2'

    for season, season_df in df.groupby('seasonId'):
        for game_length, partition_df in season_df.groupby('game_length_category'):
            object_key = f'season={season}/game_length={game_length}/Lol_rank_data(partition).parquet'
            GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
                partition_df, bucket_name, object_key
            )

