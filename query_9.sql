SELECT s.name, g.course
FROM students as s
INNER JOIN grade AS g ON s.name = g.student_name
where s.name = 'студент'