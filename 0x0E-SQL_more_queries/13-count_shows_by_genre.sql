-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT `geners`.`name`
COUNT (*) AS `number_of_shows` 
FROM `tv_geners` AS 
`geners` INNER JOIN `tv_show_genres` rel1 
ON `geners`.`id` = `rel1.`genere_id`
GROUP BY `genere`.`name` 
	ORDER BY `number_of_shows`;
