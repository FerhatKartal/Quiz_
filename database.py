import sqlite3

def connect_database_cevaplar():
    cevaplar=[]
    con=sqlite3.connect("database.db") 
    cursor=con.cursor()   
    cursor.execute("SELECT *FROM cevaplar")
    datadb=cursor.fetchall()
    for i in datadb:
        cevaplar.append(i[0])
    con.close() 
    return cevaplar

def connect_database_sonuclar():
    sonuclar=[]
    con=sqlite3.connect("database.db") 
    cursor=con.cursor()   
    cursor.execute("SELECT *FROM sonuclar")
    datadb=cursor.fetchall()
    for i in datadb:
        sonuclar.append(i[0])
    con.close() 
    return sonuclar

def connect_database_kayit(puan):
    database=sqlite3.connect("database.db")
    cursor=database.cursor()
    cursor.execute("INSERT INTO sonuclar (puan) VALUES(?)",(puan,))
    database.commit()     
    database.close()