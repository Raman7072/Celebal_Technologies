SELECT h.hacker_id, h.name , sum(s.marks) AS total 
  FROM hackers h left join (SELECT hacker_id,challenge_id,max(score) as marks from submissions 
    group by hacker_id,challenge_id) s ON h.hacker_id=s.hacker_id 
  GROUP BY h.hacker_id,h.name having total > 0 
  ORDER BY total desc, h.hacker_id asc
