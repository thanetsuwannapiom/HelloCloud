import psycopg2
connection = psycopg2.connect(user='webadmin',
                                    password='MDDnfo15110',
                                    host='node38352-bunnapon.proen.app.ruk-com.cloud',
                                    port='11234',
                                    database='work')
cursor = connection.cursor()

select_data = "SELECT * FROM euro"

cursor.execute(select_data)
Data = cursor.fetchall()
x=[]
print(Data)
for i in Data:
    x.append(i[1])

print(x)    