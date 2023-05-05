SELECT c.teacher_name, c.course, g.student_name
FROM courses as c
INNER JOIN grade AS g ON c.course = g.course_name
where g.student_name = 'студент'
and c.teacher_name = 'преподаватель'