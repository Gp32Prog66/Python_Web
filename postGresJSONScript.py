import psycopg2

db = psycopg2.connect(database="office_supplies",
                      host = "localHost",
                      user = "postgres",
                      password="GAmeP88raMD####",
                      port="5432")


cursorCon = db.cursor()

cursorCon.execute("SELECT * FROM supplies")

#Gather Everything from the Database

for row in cursorCon.fetchall():
    print(row)


#Use Fetchall Statement
print('Using Fetchall Statement')
print(cursorCon.fetchall())

db.commit()


#Close Connection and Database
db.close()
cursorCon.close()
