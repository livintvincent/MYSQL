import mysql.connector as m


def getconnection():
    connection = m.connect(host="localhost", user="root", database="studentdb", password="Livin123@")
    return connection


def insert(rollno, name, age, dob):
    con = getconnection()
    cursor = con.cursor()
    cursor.execute("insert into student values(%s, %s, %s,%s)", (rollno, name, age, dob))
    con.commit()
    cursor.close()
    con.close()
insert(10, "ammu", 15, "2010-03-15")


con = getconnection()
cursor = con.cursor()
cursor.execute("select * from student")
table = cursor.fetchall()
print(table)
con.commit()
con.close()

con = getconnection()
cursor = con.cursor()
cursor.execute("delete from student where rollno=6")
con.commit()
con.close()


def update(name, rollno):
    con = getconnection()
    cursor = con.cursor()
    cursor.execute("update student set name= %s where rollno = %s", (name, rollno))
    con.commit()
    con.close()
update("livin",5)







