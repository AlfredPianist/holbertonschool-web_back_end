-- Creates a trigger on the `orders` table
-- Before insertion, updates the `items` table with the new stock
DROP TRIGGER IF EXISTS `store`;
CREATE TRIGGER `store`
BEFORE INSERT ON `orders`
FOR EACH ROW
    UPDATE `items`
    SET `quantity` = `quantity` - NEW.`number`
    WHERE `items`.name = NEW.`item_name`;
