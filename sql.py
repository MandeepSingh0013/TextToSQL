import sqlite3

#connect to db
connection =sqlite3.connect("student.db")
# Create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

#create the table 
table_info="""
Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR (25), SECTION VARCHAR(25), MARKS INT);
    """

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Mandeep','Data Science','A',90) ''')
cursor.execute('''Insert Into STUDENT values('Gaurav','Data Science','B',100) ''')
cursor.execute('''Insert Into STUDENT values('Shambu','Data Science','A',86) ''')
cursor.execute('''Insert Into STUDENT values('Akshat','DEVOPS','A',50) ''')
cursor.execute('''Insert Into STUDENT values('Jay','DEVOPS','A',35) ''')

#Display all the records
print("The inserted records are...")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
#Close the Connection
connection.commit()
connection.close()