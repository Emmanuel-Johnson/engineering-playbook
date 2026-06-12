DELIMITER $$

CREATE PROCEDURE get_orders_by_customer(IN cust_id INT)
BEGIN
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS full_name,
        o.order_id,
        o.item,
        o.amount
    FROM Customers c
    INNER JOIN Orders o
        ON c.customer_id = o.customer_id
    WHERE c.customer_id = cust_id;
END $$

DELIMITER ;

CALL get_orders_by_customer(1);