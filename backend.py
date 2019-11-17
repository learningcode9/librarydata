import psycopg2

#created tables
def create_table():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS entry(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,entrytime DATE,exittime DATE)")
    cur.execute("CREATE TABLE IF NOT EXISTS entry1(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,entrytime TEXT)")
    conn.commit()
    conn.close()

def create_table1():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS entry(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,entrytime DATE,exittime DATE)")
    cur.execute("CREATE TABLE IF NOT EXISTS entry2(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,exittime TEXT)")
    conn.commit()
    conn.close()

def create_table2():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
   # cur.execute("CREATE TABLE IF NOT EXISTS entry(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,entrytime DATE,exittime DATE)")
    cur.execute("SELECT * INTO entry6 FROM(select e1.firstname,e1.lastname,e1.entrytime,e2.exittime from entry1 e1 INNER JOIN entry2 e2 ON e1.firstname=e2.firstname AND e1.lastname=e2.lastname)a")
    conn.commit()
    conn.close()

def insert1(firstname,lastname,entrytime):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("INSERT INTO entry1 VALUES(%s,%s,%s)",(firstname,lastname,entrytime))
    conn.commit()
    conn.close()

def insert2(firstname,lastname,exittime):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("INSERT INTO entry2 VALUES(%s,%s,%s)",(firstname,lastname,exittime))
    conn.commit()
    conn.close()


def view1():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("SELECT firstname,lastname,entrytime FROM entry1 order by entrytime DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

def view2():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("SELECT firstname,lastname,exittime FROM entry2 order by exittime DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(firstname="",lastname=""):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    #cur.execute("SELECT FROM entry3 WHERE firstname=? OR lastname=?",(firstname,lastname))
    cur.execute("SELECT * FROM entry6 WHERE firstname=%s AND lastname=%s",(firstname,lastname))
    rows=cur.fetchall()
    conn.close()
    return rows

 
create_table()
create_table1()
#
# create_table2()
#insert('srasds','belem','2019-11-12','2019-11-10')
#print(view())
#print(search('sravani','bellam'))




