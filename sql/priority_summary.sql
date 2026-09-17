SELECT
    priority,
    COUNT(*) AS number_of_tickets

FROM tickets

GROUP BY
    priority

ORDER BY
    CASE priority
        WHEN 'Urgent' THEN 1
        WHEN 'High' THEN 2
        WHEN 'Medium' THEN 3
        WHEN 'Low' THEN 4
        ELSE 5
    END;