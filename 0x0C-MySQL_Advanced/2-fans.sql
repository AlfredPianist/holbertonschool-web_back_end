-- Queries the metal_bands table
-- Column names `origin` and `nb_fans` with the sum of total fans.
SELECT `origin`,
       SUM(`fans`) AS `nb_fans`
FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
