from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone
import psycopg2
import csv
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
import json
from datetime import date
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File
from fastapi import FastAPI, File, UploadFile
import codecs


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class DateEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, date):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


conn = psycopg2.connect(database="fastapi",
                        host="localhost",
                        user="postgres",
                        password="0000",
                        port="5432")

cursor = conn.cursor()

def dbGetData():
    data = []
    cursor.execute("SELECT * FROM data_table")
    for record in cursor:
        tuple = {
            'datetime': record[0],
            'close': record[1],
            'high': record[2],
            'low': record[3],
            'open': record[4],
            'volume': record[5],
            'instrument': record[6],

        }
        data+= [tuple]
    return data

def dbInsertData(data):
    postgres_insert_query = """ INSERT INTO data_table (datetime, close, high, low, open, volume, instrument) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (data['datetime'], data['close'], data['high'], data['low'], data['open'], data['volume'], data['instrument'])
    print(record_to_insert)
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()

class Data(BaseModel):
    datetime: datetime
    close: int
    high: int
    low: int
    open: int
    volume: int
    instrument: str

@app.get("/api/data")
def getData():
    data = dbGetData()
    return data

@app.post("/api/data")
def uploadData(file: UploadFile = File(...))-> dict[str, str]:
    #add in databas
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    for rows in csvReader:
        dbInsertData(rows)            
    return {"added":"Data"}