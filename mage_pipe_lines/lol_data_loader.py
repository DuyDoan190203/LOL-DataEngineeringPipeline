import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://github.com/DuyDoan190203/Datasets-for-DE-and-ML/releases/download/games/lol_rank_games.csv.gz'
    
    lol_rank_dtypes ={
        'gameId': 'int64',
        'creationTime': pd.Int64Dtype(),
        'gameDuration': 'int64',
        'seasonId': 'int64',
        'winner': 'int64',
        'firstBlood': pd.Int64Dtype(),
        'firstTower': 'int64',
        'firstInhibitor': 'int64',
        'firstBaron': 'int64',
        'firstDragon': 'int64',
        'firstRiftHerald': 'int64',
        't1_champ1id': 'int64',
        't1_champ1_sum1': 'int64',
        't1_champ1_sum2': 'int64',
        't1_champ2id': 'int64',
        't1_champ2_sum1': 'int64',
        't1_champ2_sum2': 'int64',
        't1_champ3id': 'int64',
        't1_champ3_sum1': 'int64',
        't1_champ3_sum2': 'int64',
        't1_champ4id': 'int64',
        't1_champ4_sum1': 'int64',
        't1_champ4_sum2': 'int64',
        't1_champ5id': 'int64',
        't1_champ5_sum1': 'int64',
        't1_champ5_sum2': 'int64',
        't1_towerKills': 'int64',
        't1_inhibitorKills': 'int64',
        't1_baronKills': 'int64',
        't1_dragonKills': 'int64',
        't1_riftHeraldKills': 'int64',
        't1_ban1': 'int64',
        't1_ban2': 'int64',
        't1_ban3': 'int64',
        't1_ban4': 'int64',
        't1_ban5': 'int64',
        't2_champ1id': 'int64',
        't2_champ1_sum1': 'int64',
        't2_champ1_sum2': 'int64',
        't2_champ2id': 'int64',
        't2_champ2_sum1': 'int64',
        't2_champ2_sum2': 'int64',
        't2_champ3id': 'int64',
        't2_champ3_sum1': 'int64',
        't2_champ3_sum2': 'int64',
        't2_champ4id': 'int64',
        't2_champ4_sum1': 'int64',
        't2_champ4_sum2': 'int64',
        't2_champ5id': 'int64',
        't2_champ5_sum1': 'int64',
        't2_champ5_sum2': 'int64',
        't2_towerKills': 'int64',
        't2_inhibitorKills': 'int64',
        't2_baronKills': 'int64',
        't2_dragonKills': 'int64',
        't2_riftHeraldKills': 'int64',
        't2_ban1': 'int64',
        't2_ban2': 'int64',
        't2_ban3': 'int64',
        't2_ban4': 'int64',
        't2_ban5': 'int64'
    }

    return pd.read_csv(url, sep=",", compression="gzip", dtype=lol_rank_dtypes)
