import psycopg2 as pg

# # Создаем подключение
# conn = pg.connect(
#     dbname='netology_test',
#     user='netology_user',
#     password='test'
# )
#
# # conn = psycopg2.connect("dbname=netology_db user=netology_user")
#
# # Создаем курсор
# cur = conn.cursor()
#
# # cur.execute("""CREATE TABLE student (
# #     id serial PRIMARY KEY,
# #     name varchar(100),
# #     gpa numeric(10, 2),
# #     birth timestamp with time zone);
# # """)
#
# # Создаем таблицу
# cur.execute("""
#     create table if not exists Student(
#         id serial primary key,
#         name varchar(100) not null,
#         gpa numeric(4,2)
#     );
# """)
#
# # Отправляем запрос
# conn.commit()
#
# # Закрываем соединение
# conn.close()

with pg.connect(
    dbname='netology_test',
    user='netology_user',
    password='test'
) as conn:
    cur = conn.cursor()

    cur.execute("""
        create table if not exists Student(
            id serial primary key,
            name varchar(100) not null,
            gpa numeric(4,2)
        );
    """)

# Вставка в таблицу Student
cur.execute("""
            insert into Student(name, gpa) 
            values('Иван', 4.7),('Геннадий', NULL);
        """)

# Извлечение из таблицы
    cur.execute("""
        select * from Student;
    """)

    students = cur.fetchall()
    print(students)



