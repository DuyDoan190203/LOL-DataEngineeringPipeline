WITH team_objectives AS (
    SELECT
        gameId,
        winner,
        -- Identifying if team 1 secured the first Baron and first Dragon
        CASE 
            WHEN firstBaron = 1 THEN 1
            ELSE 0
        END AS t1_first_baron,
        CASE
            WHEN firstDragon = 1 THEN 1
            ELSE 0
        END AS t1_first_dragon,
        
        -- Identifying if team 2 secured the first Baron and first Dragon
        CASE 
            WHEN firstBaron = 2 THEN 1
            ELSE 0
        END AS t2_first_baron,
        CASE
            WHEN firstDragon = 2 THEN 1
            ELSE 0
        END AS t2_first_dragon
    FROM
        "de-zoomcamp-preparer-438218.lol_rank_games.baron-games"
)

-- Calculating win rates based on securing Baron and Dragon
SELECT
    -- For Team 1
    'Team 1' AS team,
    t1_first_baron,
    t1_first_dragon,
    COUNT(*) AS total_games,
    SUM(CASE WHEN winner = 1 THEN 1 ELSE 0 END) AS wins,
    ROUND(SUM(CASE WHEN winner = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS win_rate
FROM
    team_objectives
GROUP BY
    t1_first_baron, t1_first_dragon

UNION ALL

SELECT
    -- For Team 2
    'Team 2' AS team,
    t2_first_baron,
    t2_first_dragon,
    COUNT(*) AS total_games,
    SUM(CASE WHEN winner = 2 THEN 1 ELSE 0 END) AS wins,
    ROUND(SUM(CASE WHEN winner = 2 THEN 1 ELSE 0 END) / COUNT(*), 2) AS win_rate
FROM
    team_objectives
GROUP BY
    t2_first_baron, t2_first_dragon


-- This query allows me to be able to see how often teams win when they secure both the first Baron and Dragon, 
-- compared to scenarios when they secure neither or only one of them.