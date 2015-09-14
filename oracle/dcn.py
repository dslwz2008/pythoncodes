import cx_Oracle 

def DCNCallback(message): 
    print "Notification:" 
    for tab in message.tables: 
        print "Table:", tab.name
        for row in tab.rows: 
            if row.operation & cx_Oracle.OPCODE_INSERT: 
                print "INSERT of rowid:", row.rowid
            if row.operation & cx_Oracle.OPCODE_DELETE: 
                print "DELETE of rowid:", row.rowid

con = cx_Oracle.Connection("pythonhol/welcome@localhost/orcl",
                           events = True) 
subscriptionInsDel = con.subscribe(callback = DCNCallback, 
       operations = cx_Oracle.OPCODE_INSERT | cx_Oracle.OPCODE_DELETE, 
       rowids = True) 
subscriptionInsDel.registerquery('select * from mytab') 

raw_input("Hit Enter to conclude this demo\n") 
