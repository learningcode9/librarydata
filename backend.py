import psycopg2


#created tables
def entry_time():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS entryTime(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,EmployeeId text,entrytime text,day text)")
    conn.commit()
    conn.close()
def exit_time():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS exitTime(Firstname TEXT NOT NULL,Lastname TEXT NOT NULL,EmployeeId text ,exittime text,day text)")
    conn.commit()
    conn.close()

#Inserting data into the tables when you click timeIn and timeOut buttons
def insert_entrytime(firstname,lastname,employeeid,entrytime,day):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO entryTime VALUES(%s,%s,%s,%s,%s)",(firstname,lastname,employeeid,entrytime,day))
    conn.commit()
    conn.close()
def insert_exittime(firstname,lastname,employeeid,exittime,day):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO exitTime VALUES(%s,%s,%s,%s,%s)",(firstname,lastname,employeeid,exittime,day))
    conn.commit()
    conn.close()

#Counting how many times the employee is entering and exiting
def entry_count():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("select employeeid,count(entrytime) from  entryTime group by employeeid")  
    rows=cur.fetchall()
    conn.close()
    return rows
def exit_count():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("select employeeid,count(exittime) from exitTime group by employeeid")
    rows=cur.fetchall()
    conn.close()
    return rows


#displaying allemployees entrytimings and exittimings
def all_employee_entry_details():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT firstname,lastname,employeeid,entrytime FROM entryTime order by entrytime DESC")
    rows=cur.fetchall()
    conn.close()
    return rows
def all_employee_exit_details():
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT firstname,lastname,employeeid,exittime FROM  exitTime order by exittime DESC ")
    rows=cur.fetchall()
    conn.close()
    return rows

#Searching the employees based on the firstname,lastname or employeeid

def search(firstname="",lastname="",employeeid=""):
    conn=psycopg2.connect("dbname='library_data' user='postgres' password='postgres1984' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM (select e1.firstname,e1.lastname,e1.employeeid,e1.entrytime,e2.exittime from entryTime e1 INNER JOIN  exitTime e2 ON e1.firstname=e2.firstname AND e1.lastname=e2.lastname AND e1.employeeid=e2.employeeid) AS new_table WHERE firstname=%s OR  lastname=%s OR employeeid=%s",(firstname,lastname,employeeid))
    #cur.exexute("select e1.firstname,e1.lastname,e1.employeeid,e1.entrytime,e2.exittime from entryTime e1 INNER JOIN exitTime e2 on e1.firstname=e2.firstname and e1.lastname=e2.lastname,e1.employeeid=e2.employeeid")
    rows=cur.fetchall()
    conn.close()
    return rows

entry_time()
exit_time()







