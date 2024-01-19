-- This script creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN u_id INT)
BEGIN
    SET @av = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
    AS av from projects JOIN corrections ON corrections.project_id = projects.id
    WHERE user_id = u_id);
    UPDATE users SET average_score = @av WHERE id = u_id;
END $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE all_rows INT;
    SET all_rows = (select COUNT(*) FROM users);
    WHILE all_rows > 0 DO
        CALL ComputeAverageWeightedScoreForUser(all_rows);
        SET all_rows = all_rows - 1;
    END WHILE;
END $$
DELIMITER ;
