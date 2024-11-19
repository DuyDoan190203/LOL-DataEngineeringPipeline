import pytest
from mage_pipe_lines.lol_data_exporter_partitition import export_data_to_google_cloud_storage
from mage_pipe_lines.lol_data_transformer import transform
from mage_pipe_lines.lol_data_loader import load_data_from_api
import pandas as pd
from pandas.testing import assert_frame_equal

@pytest.fixture(scope="module")
def sample_data():
    data = {
        'gameId': [1, 2],
        'creationTime': [1609459200000, 1609459200000],
        'gameDuration': [1800, 2100],
        'seasonId': [13, 13],
        'winner': [1, 2],
        'firstBlood': [1, 0],
        'firstTower': [1, 0],
        'firstInhibitor': [1, 0],
        'firstBaron': [1, 0],
        'firstDragon': [1, 0],
        'firstRiftHerald': [1, 0],
        't1_champ1id': [1, 2],
        't1_champ1_sum1': [4, 5],
        't1_champ1_sum2': [6, 7],
        't1_champ2id': [8, 9],
        't1_champ2_sum1': [10, 11],
        't1_champ2_sum2': [12, 13],
        't1_champ3id': [14, 15],
        't1_champ3_sum1': [16, 17],
        't1_champ3_sum2': [18, 19],
        't1_champ4id': [20, 21],
        't1_champ4_sum1': [22, 23],
        't1_champ4_sum2': [24, 25],
        't1_champ5id': [26, 27],
        't1_champ5_sum1': [28, 29],
        't1_champ5_sum2': [30, 31],
        't1_towerKills': [32, 33],
        't1_inhibitorKills': [34, 35],
        't1_baronKills': [36, 37],
        't1_dragonKills': [38, 39],
        't1_riftHeraldKills': [40, 41],
        't1_ban1': [42, 43],
        't1_ban2': [44, 45],
        't1_ban3': [46, 47],
        't1_ban4': [48, 49],
        't1_ban5': [50, 51],
        't2_champ1id': [52, 53],
        't2_champ1_sum1': [54, 55],
        't2_champ1_sum2': [56, 57],
        't2_champ2id': [58, 59],
        't2_champ2_sum1': [60, 61],
        't2_champ2_sum2': [62, 63],
        't2_champ3id': [64, 65],
        't2_champ3_sum1': [66, 67],
        't2_champ3_sum2': [68, 69],
        't2_champ4id': [70, 71],
        't2_champ4_sum1': [72, 73],
        't2_champ4_sum2': [74, 75],
        't2_champ5id': [76, 77],
        't2_champ5_sum1': [78, 79],
        't2_champ5_sum2': [80, 81],
        't2_towerKills': [82, 83],
        't2_inhibitorKills': [84, 85],
        't2_baronKills': [86, 87],
        't2_dragonKills': [88, 89],
        't2_riftHeraldKills': [90, 91],
        't2_ban1': [92, 93],
        't2_ban2': [94, 95],
        't2_ban3': [96, 97],
        't2_ban4': [98, 99],
        't2_ban5': [100, 101]
    }
    return pd.DataFrame(data)

def test_transform_data(sample_data):
    transformed_df = transform(sample_data)
    assert "game_length_category" in transformed_df.columns
    assert "t1_objective_control" in transformed_df.columns
    assert transformed_df['firstBaron'].isin([0]).sum() == 0

def test_load_data_from_api():
    df = load_data_from_api()
    assert df is not None
    assert not df.empty

def test_export_data_to_google_cloud_storage(sample_data, mocker):
    mocker.patch('mage_ai.io.google_cloud_storage.GoogleCloudStorage.export', return_value=None)
    export_data_to_google_cloud_storage(sample_data)
    mage_ai.io.google_cloud_storage.GoogleCloudStorage.export.assert_called_once()