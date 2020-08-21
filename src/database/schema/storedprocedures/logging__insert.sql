DELIMITER //

DROP PROCEDURE IF EXISTS logging__insert;

CREATE PROCEDURE logging__insert (
 IN p_message VARCHAR(200),
 IN p_details TEXT,
 IN p_category VARCHAR(50),
 IN p_subcategory VARCHAR(50)
)
BEGIN
    DECLARE created_date DATETIME DEFAULT now();

    INSERT INTO sow_logging
    (
        message, 
        details, 
        category, 
        subcategory, 
        created
    )
    VALUES 
    (
        p_message,
        p_details,
        p_category,
        p_subcategory,
        created_date
    );

    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;