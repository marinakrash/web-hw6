SELECT c.teacher_name, c.course, AVG(g.grade) as avg_grade
FROM courses as c
INNER JOIN grade AS g ON c.course = g.course_name