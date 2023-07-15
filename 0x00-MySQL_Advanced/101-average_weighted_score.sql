-- This script creates a stored procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.

-- The procedure ComputeAverageWeightedScoreForUsers takes no argument

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE average_weighted_score FLOAT;

    -- Get the first user_id
    SELECT `id` INTO user_id
    FROM `users`
    ORDER BY `id`
    LIMIT 1;

    -- Loop through all users
    WHILE user_id IS NOT NULL DO
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

        -- Get the next user_id
        SELECT `id` INTO user_id
        FROM `users`
        WHERE `id` > user_id
        ORDER BY `id`
        LIMIT 1;
    END WHILE;
END $$
DELIMITER ;
