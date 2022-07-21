-- Creates a trigger on the `users` table
-- Before inserting a new email, resets `valid_email` to default (0).
DELIMITER $$
DROP TRIGGER IF EXISTS `reset_email_validation`;
CREATE TRIGGER `reset_email_validation`
BEFORE UPDATE ON `users`
FOR EACH ROW
BEGIN
    IF NEW.`email` <> OLD.`email` THEN
        SET NEW.`valid_email` = 0;
    END IF;
END$$
