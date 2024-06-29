SELECT ROUND(SQRT(POWER((a-b),2) + POWER((c-d),2)),4)
  FROM ( SELECT MAX(lat_n) AS a ,MIN(lat_n) AS b , MAX(long_w) AS c , MIN(long_w) AS d FROM STATION ) STATION
