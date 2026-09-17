SELECT
    status,
    COUNT(*) AS number_of_tickets
FROM tickets
GROUP BY status
ORDER BY number_of_tickets DESC;