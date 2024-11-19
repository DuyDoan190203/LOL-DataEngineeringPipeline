WITH raw_data AS (
    SELECT * FROM {{ ref('stg_lol_rank_games') }}
),

game_length_category AS (
    SELECT
        *,
        CASE
            WHEN gameDuration < 1500 THEN 'short'
            WHEN gameDuration < 2000 THEN 'medium'
            ELSE 'long'
        END AS game_length_category
    FROM raw_data
),

objective_control AS (
    SELECT
        *,
        {{ calculate_objective_control('firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron', 'firstDragon') }} AS t1_objective_control
    FROM game_length_category
),

filtered_data AS (
    SELECT * FROM objective_control
    WHERE firstBaron > 0
)

SELECT * FROM filtered_data