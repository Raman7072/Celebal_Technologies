SELECT ROUND(lat_n, 4) 
    FROM (SELECT LAT_N, RANK() OVER(ORDER BY lat_n ASC) AS ranked FROM station) AS station_temp 
        WHERE ranked = (SELECT ROUND(COUNT(*) / 2) FROM station)
