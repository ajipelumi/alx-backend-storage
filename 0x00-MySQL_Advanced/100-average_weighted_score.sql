-- This script creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.

-- The procedure ComputeAverageWeightedScoreForUser takes 1 argument:
-- - The user_id

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_weighted_score FLOAT;
    
    -- Get the average weighted score
    SELECT SUM(`score` * `projects`.`weight`) / SUM(`projects`.`weight`) INTO average_weighted_score
    FROM `corrections`
    JOIN `projects`
    ON `corrections`.`project_id` = `projects`.`id`
    GROUP BY `corrections`.`user_id`
    HAVING `corrections`.`user_id` = user_id;

    -- Update users table
    UPDATE `users`
    SET `average_score` = average_weighted_score
    WHERE `id` = user_id;
END $$
DELIMITER ;
