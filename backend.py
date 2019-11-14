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
    cur.execute("SELECT firstname,lastname,entrytime FROM entry1")
    rows=cur.fetchall()
    conn.close()
    return rows

def view2():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("SELECT firstname,lastname,exittime FROM entry2")
    rows=cur.fetchall()
    conn.close()
    return rows

#def timein(firstname,lastname,entrytime):
 #   conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
  #  cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
   # cur.execute("SELECT entrytime FROM entry1")
   # cur.execute("INSERT INTO entry1 ((firstname,lastname,entrytime)VALUES(?,?,?))")
    #rows=cur.fetchall()
    #conn.close()
    #return rows
    




create_table()
create_table1()
#insert('srasds','belem','2019-11-12','2019-11-10')
#print(view())



