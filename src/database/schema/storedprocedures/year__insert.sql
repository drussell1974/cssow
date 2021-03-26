DELIMITER //

DROP PROCEDURE IF EXISTS year__insert;
	
CREATE PROCEDURE year__insert (
    IN p_study_duration INT,
    IN p_start_study_in_year INT,
    IN p_key_stage_id INT,
    IN p_created_by INT,
    IN p_published_state INT)
BEGIN
	SET @yr = p_start_study_in_year;
    SET @last_year = p_start_study_in_year + p_study_duration;
    
	WHILE @yr < @last_year DO
		SET @yr_name = CONCAT('Yr', @yr);
		SELECT @yr, @last_year, @yr_name;
		INSERT IGNORE INTO sow_year (
			name,
            year_num,
			key_stage_id,
			created_by,
			published
		)
		VALUES (
			@yr_name,
            @yr,
			p_key_stage_id,
			p_created_by,
			p_published_state
		);
        
        SET @yr = @yr + 1;
	END WHILE;
END;
//

DELIMITER ;

        