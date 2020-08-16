import psycopg2


connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
               CREATE TABLE table2(
                   id INTEGER PRIMARY KEY,
                   completed BOOLEAN NOT NULL DEFAULT False
               );
               '''
               )

cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, True);')

cursor.execute(
    'INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, False))

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);', {
    'id': 3,
    'completed': True
})

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {'id': 4, 'completed': False}
cursor.execute(SQL, data)

# FETCHING DATA

cursor.execute('SELECT * FROM table2;')
print(cursor.fetchmany(3))
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchall())

cursor.execute('SELECT * FROM table2;')
print(cursor.fetchall())

connection.commit()

connection.close()
cursor.close()
