-- Creates the procedure ComputeAverageWeightedScoreForUsers
-- Computes and store the average weighted score for all students
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DROP VIEW IF EXISTS users_weighted_average_scores;
    CREATE VIEW users_weighted_average_scores AS
        SELECT
            corrections.user_id,
            (SUM(corrections.score * projects.weight) / SUM(projects.weight)) AS average_weighted_score
        FROM corrections
        JOIN projects ON projects.id = corrections.project_id
        GROUP BY corrections.user_id;
    UPDATE users
    SET average_score = (
        SELECT average_weighted_score
        FROM users_weighted_average_scores
        WHERE users.id = users_weighted_average_scores.user_id
    );
END$$