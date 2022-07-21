-- Queries the metal_bands table
-- Column names `band_name` and `lifespan` with band's lifespan.
SELECT `band_name`,
       IFNULL(`split`, 2022) - `formed` as `lifespan`
FROM `metal_bands`
WHERE `style` LIKE '%glam rock%'
ORDER BY `lifespan` DESC;
