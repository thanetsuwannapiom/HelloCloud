import psycopg2
connection = psycopg2.connect(user='webadmin',
                                    password='VCNtps41396',
                                    host='node37019-thanet.proen.app.ruk-com.cloud',
                                    port='11235',
                                    database='project')
cursor = connection.cursor()

select_data = "SELECT * FROM copper"

cursor.execute(select_data)
Data = cursor.fetchall()
x=[]
print(Data)
for i in Data:
    x.append(i[0])

print(x)    
