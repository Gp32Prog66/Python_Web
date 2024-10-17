import psycopg2

#Connect to PostGres
db = psycopg2.connect(database="office_supplies",
                      host = "localHost",
                      user = "postgres",
                      password="GAmeP88raMD####",
                      port="5432")

#Opening Cursor in a Database
cursorCon = db.cursor()

#Execute Simple Query
cursorCon.execute("SELECT * FROM supplies")

#Gather Everything from the Database

#Print out Office Supplies in Rows
for row in cursorCon.fetchall():
    print(row)


#Use Fetchall Statement
print('Using Fetchall Statement')
print(cursorCon.fetchall())

#Save Data
db.commit()


#Close Connection and Database
db.close()
cursorCon.close()
