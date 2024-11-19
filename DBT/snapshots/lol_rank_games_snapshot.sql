{% snapshot lol_rank_games_snapshot %}
    {{
        config(
            target_schema='snapshots',
            unique_key='gameId',
            strategy='timestamp',
            updated_at='updated_at'
        )
    }}

    SELECT * FROM {{ ref('lol_rank_games') }}

{% endsnapshot %}