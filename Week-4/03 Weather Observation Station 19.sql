select round(sqrt(power((a-b),2) + power((c-d),2)),4) from ( select max(lat_n) as a , min(lat_n) as b , max(long_w) as c , min(long_w) as d from station ) station
