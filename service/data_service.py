import psycopg2
import csv


conn = psycopg2.connect(database="fastapi",
                        host="localhost",
                        user="postgres",
                        password="0000",
                        port="5432")

cursor = conn.cursor()

cursor.execute("SELECT * FROM data_table")
for record in cursor:
    print(record)