import psycopg2
import csv


conn = psycopg2.connect(database="fastapi",
                        host="localhost",
                        user="postgres",
                        password="0000",
                        port="5432")

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS data_table (datetime timestamp,close DOUBLE PRECISION ,high DOUBLE PRECISION ,low DOUBLE PRECISION ,open DOUBLE PRECISION , volume DOUBLE PRECISION ,instrument varchar(20))")
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            print('Inserting ...')
            line_count += 1
        else:
            datetime = row[0]
            close = row[1]
            high = row[2]
            low = row[3]
            open = row[4]
            volume = row[5]
            instrument = row[6]
            postgres_insert_query = """ INSERT INTO data_table (datetime, close, high, low, open, volume, instrument) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (datetime, close, high, low, open, volume, instrument)
            cursor.execute(postgres_insert_query, record_to_insert)

            conn.commit()
            count = cursor.rowcount
            #print(count, "Record inserted successfully into mobile table")
            line_count += 1
    print(f'Processed {line_count} lines.')