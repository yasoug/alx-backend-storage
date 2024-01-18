-- This script creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT,
)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT AVG(score) AS av FROM corrections WHERE av.user_id=user_id);
    UPDATE users SET average_score = avg_score WHERE id=user_id;
END $$
DELIMITER ;
