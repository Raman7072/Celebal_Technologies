SELECT W.id, WP.age, W.coins_needed, W.power 
  FROM Wands W INNER JOIN Wands_Property WP ON W.code=WP.code 
  WHERE ((W.coins_needed, W.power, WP.age) IN (SELECT MIN(W.coins_needed) AS coins_needed, W.power, WP.age 
    FROM Wands W INNER JOIN Wands_Property WP ON W.code=WP.code 
    GROUP BY W.power, WP.age)) 
  AND (is_evil=0) 
  ORDER BY W.power DESC, WP.age DESC;
