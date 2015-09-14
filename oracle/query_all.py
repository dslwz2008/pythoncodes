import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@localhost/orcl')

cur = con.cursor()
cur.execute('select * from departments order by department_id')
res = cur.fetchall()
print res

cur.close()
con.close()
