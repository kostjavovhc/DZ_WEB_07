from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Subject, Student, Teacher, Group
from conf.db import session

from pprint import pprint



def select_01():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
            .select_from(Student).join(Grade).group_by(Student.fullname).order_by(desc('average_grade')).limit(5).all()
    return result

def select_02(subject_id, limit):
#Знайти студента із найвищим середнім балом з певного предмета.
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
            .select_from(Grade).join(Student).filter(Grade.subjects_id == subject_id).group_by(Student.fullname).order_by(desc('average_grade')).limit(limit).all()
    return result


def select_03(subject_id):
#Знайти середній бал у групах з певного предмета.
    result = session.query(Group.name, Subject.name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
            .select_from(Student).join(Grade, Student.id == Grade.student_id).join(Subject, Subject.id == Grade.subjects_id).join(Group, Group.id == Student.group_id) \
                .filter(Subject.id == subject_id).group_by(Group.name, Subject.name).order_by(desc('average_grade')).all()
    return result


def select_04():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')).select_from(Grade).all()
    return result


def select_05(teacher_id):
    # Знайти які курси читає певний викладач.
    result = session.query(Subject.name).select_from(Subject).join(Teacher, Teacher.id == Subject.teacher_id).filter(Teacher.id == teacher_id).group_by(Subject.name).all()
    return result


def select_06(group_id):
# Знайти список студентів у певній групі.
    result = session.query(Group.name, Student.fullname).select_from(Group).join(Student, Group.id == Student.group_id).\
        filter(Group.id == group_id).order_by(Student.fullname).all()
    return result


def select_07(group_id, subject_id):
# Знайти оцінки студентів у окремій групі з певного предмета.
    result = session.query(Student.fullname, Group.name, Subject.name, Grade.grade, Grade.grade_date)\
            .select_from(Grade).join(Student, Student.id == Grade.student_id).join(Group, Group.id == Student.group_id)\
            .join(Subject, Subject.id == Grade.subjects_id).filter(Group.id == group_id).filter(Subject.id == subject_id)\
            .order_by(desc(Grade.grade)).all()
    return result


def select_08(teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.

    result = session.query(Subject.name, Teacher.fullname, func.round(func.avg(Grade.grade), 2).label('ave_grade'))\
        .select_from(Grade).join(Subject, Subject.id == Grade.subjects_id).join(Teacher, Teacher.id == Subject.teacher_id)\
        .filter(Teacher.id==teacher_id).group_by(Subject.name, Teacher.fullname).order_by(desc('ave_grade')).all()
    return result


def select_09(student_id):
# Знайти список курсів, які відвідує студент.
    result = session.query(Subject.name).select_from(Grade).join(Student, Student.id == Grade.student_id)\
            .join(Subject, Subject.id == Grade.subjects_id).filter(Student.id == student_id).group_by(Subject.name).all()
    return result

def select_10(student_id, teacher_id):
# Список курсів, які певному студенту читає певний викладач.
    result = session.query(Subject.name).select_from(Grade).join(Student, Student.id == Grade.student_id)\
            .join(Subject, Subject.id == Grade.subjects_id).join(Teacher, Teacher.id == Subject.teacher_id)\
            .filter(Student.id == student_id).filter(Teacher.id == teacher_id).group_by(Subject.name).all()
    return result

def select_11(student_id, teacher_id):
# Середній бал, який певний викладач ставить певному студентові.
    result = session.query(func.round(func.avg(Grade.grade), 2).label('ave_rate')).select_from(Grade)\
            .join(Subject, Subject.id==Grade.subjects_id).join(Student, Student.id == Grade.student_id)\
            .join(Teacher, Teacher.id == Subject.teacher_id).filter(Student.id==student_id).filter(teacher_id ==teacher_id)\
            .all()
    return result

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

if __name__ == '__main__':
    pprint(select_11(11,2))