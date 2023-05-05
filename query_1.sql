SELECT g.student_name, AVG(g.grade) as highest_avg_grade
FROM grades as g
GROUP BY g.student_name;
ORDER BY AVG(g.grade) DESC;
LIMIT 5;
