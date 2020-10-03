SELECT date as day, SUM(CASE WHEN scores>=0 THEN scores ELSE 0 END) as num_pos_scores, SUM(CASE WHEN score<0 THEN score ELSE 0 END) as num_neg_scores
FROM assessments 
WHERE date >= '2011-03-01 00:00:00' AND date <= '2011-04-30 00:00:00'
GROUP BY date;