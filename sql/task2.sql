SELECT date as day
FROM assessments 
WHERE date >= '2011-01-01 00:00:00' AND date <= '2011-06-30 00:00:00'
AND scores >= 0
GROUP BY date;