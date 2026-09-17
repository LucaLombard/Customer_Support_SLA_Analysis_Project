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