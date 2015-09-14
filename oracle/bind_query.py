import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@localhost/orcl')

cur = con.cursor()
cur.prepare('select * from departments where department_id = :id')

cur.execute(None, {'id': 210})
res = cur.fetchall()
print res

cur.execute(None, {'id': 110})
res = cur.fetchall()
print res

cur.close()
con.close()
