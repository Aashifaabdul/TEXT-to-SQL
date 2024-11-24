import  sqlite3

#connect to sqlite
connection=sqlite3.connect("student.db")

#create cursor to insert record ,create table 
cursor=connection.cursor()

#create a table 
table_info="""Create table Student(name varchar(50),Class varchar(25),section varchar(15), marks int);

"""

cursor.execute(table_info)

cursor.execute("Insert into Student values('Aashifa','Data science','A',90);")
cursor.execute(" Insert into Student values('Aash','ML','B',70);")
cursor.execute(" Insert into Student values('Janani','Data science','A',30);")
cursor.execute(" Insert into Student values('Sabari','AI','C',80);")
cursor.execute(" Insert into Student values('Ambika','Data science','A',50);")
cursor.execute("Insert into Student values('Karthik','ML','B',80);")



#display all records 

print("The inserted records are" )
data=cursor.execute('''Select * from Student''')

for row in data:
    print(row)
    
#close the connection 
connection.commit()
connection.close()