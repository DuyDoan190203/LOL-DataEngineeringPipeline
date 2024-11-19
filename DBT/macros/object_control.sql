{% macro calculate_objective_control(firstBlood, firstTower, firstInhibitor, firstBaron, firstDragon) %}
    {{ firstBlood }} + {{ firstTower }} + {{ firstInhibitor }} + {{ firstBaron }} + {{ firstDragon }}
{% endmacro %}