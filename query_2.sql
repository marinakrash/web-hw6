SELECT g.student_name, g.course_name, max(AVG(g.grade)) as highest_avg_grade
FROM grades as g
where g.course_name = 'предмет'