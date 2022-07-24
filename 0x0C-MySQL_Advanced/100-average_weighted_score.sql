-- Creates the procedure ComputeAverageWeightedScoreForUser
-- Computes and store the average weighted score for a student
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE weighted_average_score FLOAT;
    SET weighted_average_score = (
        SELECT SUM(score * weight) / SUM(weight)
        FROM users
        JOIN corrections ON users.id = corrections.user_id
        JOIN projects ON projects.id = corrections.project_id
        WHERE users.id = user_id
    );
    UPDATE users
    SET average_score = weighted_average_score
    WHERE id = user_id;
END$$