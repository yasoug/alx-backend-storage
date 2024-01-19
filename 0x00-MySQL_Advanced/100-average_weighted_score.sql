-- This script creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN u_id INT)
BEGIN
    SET @av = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
    AS av from projects JOIN corrections ON corrections.project_id = projects.id
    WHERE user_id = u_id);
    UPDATE users SET average_score = @av WHERE id = u_id;
END $$
DELIMITER ;
