#Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
query1 = '''SELECT s.fullname, ROUND(AVG(r.rate),2) as ave_rate
FROM rates r
JOIN students s ON r.student_id = s.id
GROUP BY s.fullname 
ORDER BY ave_rate DESC 
LIMIT 5;'''

#Знайти студента із найвищим середнім балом з певного предмета.
query2 = '''SELECT sb.name, s.fullname, ROUND(AVG(r.rate),2) as ave_rate
FROM rates r
JOIN students s ON r.student_id = s.id
JOIN subjects sb ON r.subject_id = sb.id 
WHERE sb.id = (?)
GROUP BY s.fullname 
ORDER BY ave_rate DESC 
LIMIT 1;'''

#Знайти середній бал у групах з певного предмета.
query3 = '''
SELECT sb.name, g.name , ROUND(AVG(r.rate),2) as ave_rate
FROM rates r
JOIN students s ON r.student_id = s.id
JOIN [groups] g ON s.group_id = g.id 
JOIN subjects sb ON r.subject_id = sb.id 
WHERE sb.id = (?)
GROUP BY sb.name, g.name 
ORDER BY ave_rate DESC
;'''

# Знайти середній бал на потоці (по всій таблиці оцінок).
query4 = '''
SELECT Round(AVG(rate), 2) as ave_rate
FROM rates
'''

# Знайти які курси читає певний викладач.
query5 = ''' 
SELECT s.name 
FROM subjects s 
JOIN teachers t ON s.teacher_id = t.id 
WHERE t.id = (?)
GROUP BY s.name ;
'''

# Знайти список студентів у певній групі.
query6 = ''' 
SELECT s.fullname, g.name 
FROM students s 
JOIN [groups] g ON g.id  = s.group_id  
WHERE g.id = (?)
GROUP BY s.fullname ;
'''

# Знайти оцінки студентів у окремій групі з певного предмета.
query7 = ''' 
SELECT s.fullname , g.name , sb.name, r.rate, r.date_of 
FROM rates r
JOIN students s ON r.student_id = s.id
JOIN [groups] g ON s.group_id = g.id 
JOIN subjects sb ON sb.id = r.subject_id
WHERE g.id = (?) AND sb.id = (?)
ORDER BY r.rate DESC, r.date_of DESC;
'''

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
query8 = ''' 
SELECT sb.name, ROUND(AVG(r.rate), 2) as ave_rate
FROM rates r
JOIN subjects sb ON sb.id = r.subject_id 
JOIN teachers t ON t.id = sb.teacher_id 
WHERE t.id = (?)
Group BY sb.name
ORDER BY ave_rate DESC;
'''

# Знайти список курсів, які відвідує студент.
query9 = ''' 
SELECT sb.name 
FROM rates r 
JOIN subjects sb ON r.subject_id = sb.id 
JOIN students s ON s.id = r.student_id 
WHERE s.id = (?)
GROUP BY sb.name ;
'''

# Список курсів, які певному студенту читає певний викладач.
query10 = ''' 
SELECT sb.name
FROM rates r 
JOIN subjects sb ON r.subject_id = sb.id 
JOIN students s ON s.id = r.student_id
JOIN teachers t ON t.id = sb.teacher_id
WHERE s.id = (?) and t.id = (?)
GROUP BY sb.name ;
'''

# Середній бал, який певний викладач ставить певному студентові.
query11 = ''' 
SELECT ROUND(AVG(r.rate), 2) 
FROM rates r 
JOIN subjects sb ON r.subject_id = sb.id 
JOIN students s ON s.id = r.student_id
JOIN teachers t ON t.id = sb.teacher_id
WHERE s.id = (?) and t.id = (?)
GROUP BY  t.id ;
'''
# Оцінки студентів у певній групі з певного предмета на останньому занятті.
query12 = ''' 
SELECT s.fullname, r.rate, sb.name, g.name, MAX(r.date_of) as last_date 
FROM students s JOIN rates r ON s.id = r.student_id
JOIN subjects sb ON r.subject_id = sb.id 
JOIN [groups] g ON g.id = s.group_id 
WHERE g.id  = (?) and sb.id  = (?)
GROUP BY s.fullname, sb.name, r.rate, g.name 
ORDER BY last_date DESC
LIMIT 2;
'''
