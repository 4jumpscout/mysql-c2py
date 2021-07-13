import mysql.connector
import pandas as pd
x=mysql.connector.connect(user="root",password="CemKaraca2112.",host="localhost",database="mytable")
mycursor= x.cursor()
mycursor.execute("select * from mytable ")
z=mycursor.fetchall()
m=pd.DataFrame(z)
print(m)