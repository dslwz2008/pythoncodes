import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@localhost/orcl')
print con.version

con.close()
