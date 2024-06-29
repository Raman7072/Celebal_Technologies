SELECT Joined.Hacker_ID, name 
  FROM ( SELECT S.hacker_id, Count(*) as countmaxscore 
    FROM Submissions S LEFT JOIN Challenges C ON S.challenge_id = C.Challenge_id LEFT JOIN Difficulty D ON C.Difficulty_level = D.Difficulty_level 
    Where S.score = D.score GROUP BY S.hacker_id ) AS Joined LEFT JOIN Hackers H ON Joined.hacker_id = H.hacker_ID 
  WHERE countmaxscore > 1 
  ORDER BY countmaxscore DESC, Joined.hacker_id ASC
