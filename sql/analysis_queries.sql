SELECT
    status,
    COUNT(*) AS number_of_tickets
FROM tickets
GROUP BY status
ORDER BY number_of_tickets DESC;

SELECT
    priority,
    COUNT(*) AS number_of_tickets
FROM tickets
GROUP BY priority
ORDER BY number_of_tickets DESC;

SELECT
    ROUND(AVG(response_hours), 2) AS average_response_hours
FROM tickets;

SELECT
    tickets.ticket_id
    tickets.status
    tickets.priority
    teams.team_name
FROM tickets
JOIN teams
    ON tickets.team_id = teams.team_id
LIMIT 10;

SELECT
    teams.team_name
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
    ON tickets.team_id = teams.team_id

GROUP BY
    teams.team_id
    teams.team_name

ORDER BY
    response_sla_percentage ASC;