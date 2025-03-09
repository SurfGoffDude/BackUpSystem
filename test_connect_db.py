import psycopg2


conn = psycopg2.connect(
    dbname="testdb",
    user="testuser",
    password="testpassword",
    host="localhost",
    port="5432",
)

cur = conn.cursor()

cur.execute("SELECT * FROM testtable;")

data = (0, "BMW", 250, 0)
cur.execute(
    "INSERT INTO testtable (MotorcycleID, Name, Weight, Cubes) VALUES (%s, %s, %s, %s);",
    data,
)
conn.commit()

'''data = [(2, "Triumph", 300, 2500), (3, "Harley", 300, 1500)]
cur.executemany(
    "INSERT INTO testtable (MotorcycleID, Name, Weight, Cubes) VALUES (%s, %s, %s, %s);",
    data,
)
conn.commit()'''

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
