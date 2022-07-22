-- Creates an index on the table names
-- The idx_name_first is used for the first letter of the name column
CREATE INDEX idx_name_first ON names (name(1));
