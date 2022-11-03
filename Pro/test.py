import psycopg2
connection = psycopg2.connect(user='webadmin',
                                    password='VCNtps41396',
                                    host='node37019-thanet.proen.app.ruk-com.cloud',
                                    port='11235',
                                    database='project')
cursor = connection.cursor()

select_copper = 'select * from copper'

cursor.execute(select_copper)
Data = cursor.fetchall()
s = []
for i in Data: # แปลง list ซ้อน list
    for z in i:
        s.append(z)

print(s)