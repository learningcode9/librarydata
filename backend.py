import psycopg2

#created tables
def create_table():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS entry(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,entrytime DATE,exittime DATE)")
    cur.execute("CREATE TABLE IF NOT EXISTS entry1(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,EmployeeId TEXT NOT NULL,entrytime TEXT)")
    conn.commit()
    conn.close()

def create_table1():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS entry(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,entrytime DATE,exittime DATE)")
    cur.execute("CREATE TABLE IF NOT EXISTS entry2(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,EmployeeId TEXT NOT NULL,exittime TEXT)")
    conn.commit()
    conn.close()

def create_table2():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS new_table AS(select e1.firstname,e1.lastname,e1.employeeid,e1.entrytime,e2.exittime from entry1 e1 INNER JOIN entry2 e2 ON e1.firstname=e2.firstname AND e1.lastname=e2.lastname AND e1.employeeid=e2.employeeid)")
    #cur.execute("SELECT * INTO entry6 FROM(select e1.firstname,e1.lastname,e1.employeeid,e1.entrytime,e2.exittime from entry1 e1 INNER JOIN entry2 e2 ON e1.firstname=e2.firstname AND e1.lastname=e2.lastname AND e1.employeeid=e2.employeeid)a")
   # cur.execute("SELECT * INTO entry3 FROM(SELECT e1.firstname, e1.lastname,e1.employeeid,e1.entrytime,e2.exittime FROM entry1 e1 INNER JOIN entry2 e2 ON e1.firstname=e2.firstname and e1.lastname =e2.lastname and e1.employeeid=e2.employeeid)a")
    #cur.execute("SELECT * INTO entry3 FROM(SELECT e1.firstname, e1.lastname,e1.employeeid,e1.entrytime,e2.exittime FROM entry1 e1 INNER JOIN entry2 e2 ON e1.firstname=e2.firstname and e1.lastname =e2.lastname and e1.employeeid=e2.employeeid)a WHERE EXISTS (SELECT * FROM entry3 WHERE firstname=%s OR  lastname=%s OR employeeid=%s",(firstname,lastname,employeeid)"))
    conn.commit()
    conn.close()


def insert1(firstname,lastname,employeeid,entrytime):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("INSERT INTO entry1 VALUES(%s,%s,%s,%s)",(firstname,lastname,employeeid,entrytime))
    conn.commit()
    conn.close()

def insert2(firstname,lastname,employeeid,exittime):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("INSERT INTO entry2 VALUES(%s,%s,%s,%s)",(firstname,lastname,employeeid,exittime))
    conn.commit()
    conn.close()


def view1():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("SELECT firstname,lastname,employeeid,entrytime FROM entry1 order by entrytime DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

def view2():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    cur.execute("SELECT firstname,lastname,employeeid,exittime FROM entry2 order by exittime DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(firstname="",lastname="",employeeid=""):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO entry1 VALUES(%s,%s)",(firstname,lastname))
    #cur.execute("SELECT FROM entry3 WHERE firstname=? OR lastname=?",(firstname,lastname))
    cur.execute("SELECT * FROM new_table WHERE firstname=%s OR  lastname=%s OR employeeid=%s",(firstname,lastname,employeeid))
   # cur.execute("SELECT e1.firstname,e1.lastname,e1.employeeid,e1.entrytime,e2.exittime FROM entry1 e1 INNER JOIN entry2 e2 ON e1.firstname=e2.firstname AND e1.lastname=e2.lastname AND e1.employeeid=e2.employeeid WHERE e1.firstname =e2.firstname OR e1.lastname =e2.lastname OR e1.employeeid=e2.employeeid")
    rows=cur.fetchall()
    conn.close()
    return rows

 
create_table()
create_table1()
create_table2()
#search()
#
#create_table2()
#insert('srasds','belem','2019-11-12','2019-11-10')
#print(view())

#print(view1())



