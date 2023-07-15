-- This script creates a stored procedure ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.

-- The procedure ComputeAverageWeightedScoreForUsers takes no argument

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE average_weighted_score FLOAT;

    -- Declare a cursor to iterate over all users
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    -- Declare a handler to catch the end of the cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN cur;

    -- Iterate over all users
    read_loop: LOOP
        -- Fetch the user id
        FETCH cur INTO user_id;

        -- If the cursor is empty, leave the loop
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Compute the average weighted score for the user
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END $$
DELIMITER ;
