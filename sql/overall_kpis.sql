SELECT
    teams.team_name,
    COUNT(tickets.ticket_id) AS total_tickets,

    ROUND(
        AVG(tickets.response_hours),
        2
    ) AS average_response_hours,

    ROUND(
        100.0 * AVG(
            CASE
                WHEN tickets.response_hours
                    <= teams.target_response_hours
                THEN 1
                ELSE 0
            END
        ),
        1
    ) AS response_sla_percentage,

    ROUND(
        AVG(tickets.satisfaction_score),
        2
    )  AS average_satisfaction

FROM tickets

JOIN teams
    ON tickets.team_id = teams.team_id;


