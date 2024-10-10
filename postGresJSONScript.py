import psycopg2

db = psycopg2.connect(database="office_supplies",
                      host = "LocalHost",
                      user = "Postgres",
                      password="GAmeP88raMD####",
                      port="5432")


cursorCon = conn.cursor()

cursorCon.execute("SELECT * FROM supplies")

#Gather Everything from the Database
print(cursorCon.fetchall())

