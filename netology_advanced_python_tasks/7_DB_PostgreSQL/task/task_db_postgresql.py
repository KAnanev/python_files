import psycopg2 as pg


class ManagerDB:
    def __init__(self):
        self.conn = pg.connect(dbname='netology_task', user='netology_user', password='0301')

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def create_db(self):
        try:
            self.cur.execute("""
                                create table if not exists student(
                                    id serial primary key not null,
                                    name varchar(100) not null,
                                    gpa numeric(4,2),
                                    birth timestamp
                                )
                                create table if not exists course (
                                    id serial primary key,
                                    name varchar(100)
                                )
                                create table if not exists student_course (
                                    id serial primary key,
                                    student_id integer references student(id),
                                    course_id integer references course(id)
                                );
            """)
            self.conn.commit()

        except Exception as er:
            self.conn.rollback()
            print(er)

    def add_student(self, student):
        try:
            self.cur.execute("""
                        insert into student(name, gpa, birth) 
                        values(%(name)s, %(gpa)s, %(birth)s);
                    """, student)
            self.conn.commit()

        except Exception as er:
            self.conn.rollback()
            print(f' Ошибка - {er}')

    def get_student(self, student_id):
        try:
            self.cur.execute("""
                        select * from student
                        where id = %s;
                    """, (student_id, ))
            student = self.cur.fetchall()
            print(student)
        except Exception as er:
            print(f' Ошибка - {er}')

    def add_students(self, course_id, students):
        try:
            for item in students:
                self.cur.execute("""
                            insert into student(name, gpa, birth) 
                            values(%(name)s, %(gpa)s, %(birth)s) returning id;            
                            """, item)
                id_student = self.cur.fetchall()

                self.cur.execute("""
                                    insert into student_course (student_id, course_id)
                                    values (%s, %s)
                                """, (id_student[0], course_id, ))
                self.conn.commit()

        except Exception as er:
            self.conn.rollback()
            print(f' Ошибка - {er}')

    def get_students(self, course_id):
        self.cur.execute("""
                            select s.name from student_course sc
                            join student s on s.id = sc.student_id
                            join course c on c.id = sc.course_id
                            where c.id = %s
                        """, (course_id,))
        students_course_id = self.cur.fetchall()
        print(students_course_id)





if __name__ == '__main__':
    with ManagerDB() as conn:
        # conn.create_db()
        # conn.add_student({'name': 'Иван', 'gpa': 4.2, 'birth': '1999-01-08'})
        # conn.get_student(6)
        # conn.add_students(3, [{'name': 'Виктор', 'gpa': 3.0, 'birth': '1986-05-06'}, {'name': 'Utyyflbq', 'gpa': 4.0, 'birth': '1985-07-07'}])
        conn.get_students(3)

