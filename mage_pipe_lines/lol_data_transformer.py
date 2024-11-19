import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data['creationTime'] = pd.to_datetime(data['creationTime'], unit='ms')

    def categorize_game_duration(duration):
        if duration < 1500:
            return 'short'
        elif duration < 2000:
            return 'medium'
        else:
            return 'long'
    
    data['game_length_category'] = data['gameDuration'].apply(categorize_game_duration)
    data['t1_objective_control'] = data[['firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron', 'firstDragon']].sum(axis=1)
    filtered_data = data[data['firstBaron'] > 0]

     # Add More data validation
    assert filtered_data['gameId'].notnull().all(), "Null values found in 'gameId'"
    assert filtered_data['creationTime'].notnull().all(), "Null values found in 'creationTime'"
    assert filtered_data['firstBaron'].notnull().all(), "Null values found in 'firstBaron'"

    return filtered_data


@test
def test_output(output, *args):
    # Ensure there are no games with zero Barons
    assert output['firstBaron'].isin([0]).sum() == 0, 'There are games with zero Baron farming.'
    # Ensure no missing values in critical columns
    assert output[['gameId', 'creationTime', 'firstBaron']].isnull().sum().sum() == 0, 'Null values found in critical columns'
    # Ensure 'creationTime' is converted to datetime
    assert pd.api.types.is_datetime64_any_dtype(output['creationTime']), 'creationTime is not a datetime type'