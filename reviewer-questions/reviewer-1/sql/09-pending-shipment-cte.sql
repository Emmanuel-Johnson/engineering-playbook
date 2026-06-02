WITH PendingShipments AS (
    SELECT 
        c.first_name || ' ' || c.last_name AS full_name,
        s.status
    FROM Customers AS c
    INNER JOIN Shippings AS s
    ON c.customer_id = s.customer
)

SELECT *
FROM PendingShipments
WHERE status = 'Pending';