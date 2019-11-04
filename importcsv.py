import csv
import sqlite3
from contextlib import closing

def importcsv():
    with open('csv/api_titlewords.csv', 'r', newline="", encoding='utf-8') as f:
        reader = csv.reader(f)
        dbname = 'db.sqlite3'
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()
            for row in reader:
                sql = 'insert into api_titlewords(id,word,type1,type2,type3) values(?,?,?,?,?)'
                id = row[0]
                type1 = row[1]
                type2 = row[2]
                type3 = row[3]
                word = row[4]
                r = c.execute(sql, (id,word,type1,type2,type3))
            conn.commit()

    with open('csv/api_titlechains.csv', 'r', newline="", encoding='utf-8') as f:
        reader = csv.reader(f)
        dbname = 'db.sqlite3'
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()
            for row in reader:
                sql = 'insert into api_titlechains(id1,id2,num) values(?,?,?)'
                id1 = row[0]
                id2 = row[1]
                num = row[2]
                r = c.execute(sql, (id1,id2,num))
            conn.commit()
    

if __name__ == '__main__':
    importcsv()