-- Creates a trigger on the `orders` table
-- After insertion, updates the `items` table with the new stock
CREATE TRIGGER `store`
BEFORE INSERT ON `orders`
FOR EACH ROW
    UPDATE `items`
    SET `quantity` = `quantity` - NEW.`number`
    WHERE `items`.name = NEW.`item_name`;
