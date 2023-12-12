# import socket
# import view import index, blog

# URLS = {

#     '/': index,
#     '/blog': blog

# }

# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url

# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200

# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found!</h3>'
#     elif code == 405:
#         return '<h1>404</h1><h3>Method Not Allowed!</h3>'
#     return URLS[url]()


# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()

# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()

#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()



# if __name__ == "__main":
#     run()
# con = sqlite3.connect("profile.db")
# cur = con.cursor()

# cur.execute("""
# """)

# con.close()

# cur.execute(CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         summa REAL,
#         date TEXT
#     ))

import sqlite3

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # date TEXT
#     # )""")
#     cur.execute("DROP TABLE users")
    
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     DROP TABLE person_table           
#     """)
    
    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN address            
    # """)
    
    
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;            
    # """)
    
    
    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT  "+79004005060",
    # age INTEGER CHECK (age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")
    
# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM T1
#         LIMIT 5 OFFSET 2
#     """)
    
#     res = cur.fetchall()
#     print(res)
#     res2 = cur.fetchmany()
#     print(res2)
    
    # for i in cur:
    #     print(i)
    
# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS student(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT NOT NULL,
#         name TEXT NOT NULL,
#         patronymic TEXT NOT NULL,
#         age INTEGER NOT NULL CHECK (age >= 16 AND age <= 45),
#         [group] TEXT NOT NULL,
#         FOREIGN KEY ([group]) REFERENCES groups (id) ON DELETE RESTRICT
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS groups(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         group_name TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS lessons(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         lesson_title TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS association(
#         lesson_id INTEGER NOT NULL,
#         group_id INTEGER NOT NULL,
#         FOREIGN KEY (group_id) REFERENCES groups (id)
#         FOREIGN KEY (lesson_id) REFERENCES lessons (id)
#     )""")

with sqlite3.connect("study.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT NOT NULL,
        name TEXT NOT NULL,
        age INTEGER NOT NULL CHECK (age >= 16 AND age <= 45),
        [course] TEXT NOT NULL,
        FOREIGN KEY ([course]) REFERENCES courses (id) ON DELETE RESTRICT
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS registration(
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (id)
        FOREIGN KEY (course_id) REFERENCES courses (id)
    )""")