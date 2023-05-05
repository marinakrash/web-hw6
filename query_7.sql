SELECT g.course_name, g.grade, gr.group_number
FROM grades as g
INNER JOIN groups AS gr ON g.student_name = gr.student_name
where g.course_name = 'предмет'
and gr.group_number = '#'