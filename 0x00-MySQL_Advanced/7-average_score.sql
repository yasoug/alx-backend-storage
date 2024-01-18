-- This script creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN u_id INT
)
BEGIN
    SET @av = (SELECT AVG(score) AS av FROM corrections WHERE user_id = u_id);
    UPDATE users SET average_score = @av WHERE id = u_id;
END $$
DELIMITER ;
