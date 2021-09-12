# ArmStrong numbers
# def arm():
#     for i in range(100,1000):
#         n = i
#         s = 0
#         while n > 0:
#             s += (n % 10) ** 3
#             n = n// 10
#         if i==s:
#             print(i)
#
# Prime numbers
# def prime():
#     for i in range(100,1000):
#         flag=False
#         for a in range(2,int(i**0.5)+1):
#             if i%a==0:
#                 flag=True
#                 break
#         if not flag:
#             print(i)
#
# Arrange all names in ascending order in a list
# def bub_sort(l):
#     for i in range(len(l) - 1, -1, -1):
#         for j in range(i):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     return l
#
# Create a dictionary with the details of products(PID, pname, manufacturing date, qty, price)
# then define a function to find out details of all products whose qty>100 and price<450
# def select(pdts):
#     for pdt in pdts:
#         if pdt['qty']>100 and pdt['price']<450:
#             print(pdt)
#
# l=[]
# for i in range(1):
#     d= {"pid": input("PID: "), "name": input("Name: "), "mfd": input("MFD Date: "), "qty": int(input("QTY: ")),"price": int(input("Price: "))}
#     l.append(d)
# select(l)
#
# Selection Sort
# def selectionSort(l, size):
#     for j in range(size):
#         m = j
#         for i in range(j + 1, size):
#             if l[i] < l[m]:
#                 min_idx = i
#         (l[j], l[min_idx]) = (l[min_idx], l[j])
#     return l
#
# data = [-2, 45, 0, 11, -9]
# size = len(data)
# data=selectionSort(data, size)
# print('Ascending Order:')
# print(data)
#
# sum of all numbers in the text file
# file=open("test1.txt","r")
# s=0
# for line in file:
#     for ch in line.split():
#         if ch.isdigit():
#             s+=int(ch)
# print(s)
#
# delete "is" word from text file
# file=open("test1.txt","r")
# temp=""
# for line in file:
#     for word in line.split():
#         if word.lower()!="is":
#             temp+=word+" "
#     temp+="\n"
# file.close()
# file=open("test1.txt","w")
# file.write("")
# file.write(temp)
#
# Replace all "he" words by "she" in text file
# file=open("test1.txt","r")
# temp=""
# for line in file:
#     for word in line.split():
#         if word.lower()=="he":
#             temp+="she"+" "
#         else:
#             temp += word + " "
#     temp+="\n"
# file.close()
# file=open("test1.txt","w")
# file.write("")
# file.write(temp)
# file.close()
#
#
#
# Take input for roll,name and percentage of students and further write them in a binary file.
# import pickle
# def write_details():
#     lst=[]
#     for _ in range(10):
#         r=int(input("Enter roll "))
#         n=input("Enter name ")
#         p=float(input("Enter percentage "))
#         d=str(r)+' '+n+' '+str(p)
#         lst.append(d)
#     fp=open("student","wb")
#     pickle.dump(lst,fp)
#     fp.close()
# write_details()
#
# To read the roll,name and per stored in  binary file.
# import pickle
# f=open("student","rb")
# temp=pickle.load(f)
# f.close()
# for i in temp:
#     print(i)
#
# A binary file “STUDENT.DAT” has structure [admission_number, Name, Percentage].
# Write a function countrec() in Python that would read contents of the file “STUDENT.DAT”
# and display the details of those students whose percentage is above 75.
# Also display number of students scoring above 75%.
# import pickle
# fobj = open("student.dat", "rb")
# num = 0
# try:
#     while True:
#         rec = pickle.load(fobj)
#         if rec[2] > 75:
#             num = num + 1
#             print(rec[0], rec[1], rec[2])
# except:
#     fobj.close()
# print(num)
#
#
#
# csv open(roll, eng, hindi, science, sst, maths), get marks of students; display roll,
# total,percentage of 90% above students
# import csv
# file=open("files/students.csv","r")
# marks={}
# r=csv.reader(file)
# for s in r:
#     total=0
#     for i in range(1,6):
#         total+=float(s[i])
#     per=total/5
#     if per>=90:
#         print(s[0],total,per)
# file.close()
#
# phone.csv read name,address,area code,ph no
# display all with area code=125435
# import csv
# file=open("files/phone.csv","r")
# r=csv.reader(file)
# for s in r:
#     if s[2]==125435:
#         print(s[0])
# file.close()
#
# products.csv read name,code,price,qty
# display all with price>700
# import csv
# file=open("files/products.csv","r")
# r=csv.reader(file)
# for s in r:
#     if s[2]>700:
#         print(s[0])
# file.close()
#
#
#
# stack implementation by list
# stack=[]
# depth=5
# def push():
#     if len(stack)==depth:
#         print("stack overflow")
#     else:
#         n=int(input("Enter element:"))
#         stack.append(n)
#
# def pop():
#     if not stack:
#         print("stack underflow")
#     else:
#         print(stack[-1],end=" ")
#         stack.pop(-1)
#
# def traversing():
#     if not stack:
#         print("empty stack")
#     else:
#         for i in range(len(stack)-1,-1,-1):
#             print(stack[i])
#
#
# Binary Search:
# l=[10,13,16,34,56,78,90]
# n=int(input("enter ele: "))
# beg=0
# end=len(l)-1
# mid=(beg+end)//2
# while beg<=end:
#     mid = (beg + end) // 2
#     if l[mid]==n:
#         print(f"found at {mid}")
#         exit()
#     elif l[mid]<n:
#         beg=mid+1
#     else:
#         end=mid-1
# print("not found")
#
#
# Replace all prime numbers with its next prime number in a list
# def isPrime(n):
#     for i in range(2,int(n**0.5)):
#         if n%i==0:
#             return False
#     return True
# def nextPrime(n):
#     p=n+1
#     while True:
#         if isPrime(p):
#             break
#         p+=1
#     return p
# l=[11,12,45,7,19]
# for a in range(len(l)):
#     if isPrime(l[a]):
#         l[a]=nextPrime(l[a])
# print(l)
#
#
# Exchange odd position elements of a list with even ones(for odd last one stays unchanged)
# l=[1,2,3,4,5]
# for i in range(0,len(l),2):
#     if i+1<len(l):
#         l[i],l[i+1]=l[i+1],l[i]
# print(l)
#
#
# Exchange first half elements with last half in a list(for even no of elements)
# l=[1,2,3,4,5,6]
# l1=l[0:len(l)//2]
# l2=l[len(l)//2:]
# l_new=l2+l1
# print(l_new)
#
# create a dict with the opposite mapping
# x={"k1":"v1","k2":"v2","k3":"v3"}
# y={}
# for line in x:
#     y[x[line]]=line
# print(y)

# SQL::
'''
"Table1" Table:
ID | Name
......
......
......

"Names" Table:
ID | Salary
......
......
......

CREATE TABLE Table1 (
    ID int,
    Name varchar(255)
);

CREATE TABLE Names (
    ID int,
    Salary int
);

Insert Values into Table1:
INSERT INTO Table1 VALUES (1,'Ram');
INSERT INTO Table1 VALUES (101,'Bam');
INSERT INTO Table1 VALUES (1001,'Sam');
INSERT INTO Table1 VALUES (10001,'Lam');
INSERT INTO Table1 VALUES (100001,'Gam');

Insert Values into Names:
INSERT INTO Names VALUES (1,1000)
INSERT INTO Names VALUES (101,10000)
INSERT INTO Names VALUES (1001,100000000)
INSERT INTO Names VALUES (10001,100000000)
INSERT INTO Names VALUES (100001,100000)

Join the tables:
SELECT Table1.Name,Names.Salary
FROM Table1
FULL JOIN Names
ON Table1.ID = Names.ID

Find Duplicate:
SELECT ID, COUNT(ID)
FROM Names
GROUP BY ID
HAVING COUNT(ID)>1;

Add Row:
INSERT INTO Names (ID, Name)
VALUES (101,'abc');

Add Column:
ALTER TABLE Names
ADD email varchar(255);

Delete Row:
DELETE FROM Names WHERE ID=101;

Delete Column:
ALTER TABLE Name
DROP COLUMN email;

Sort According to Salary:
SELECT * FROM Names
ORDER BY Salary;

Minimum:
SELECT MIN(ID)
FROM Names;

Maximum:
SELECT MAX(ID)
FROM Names;

Count the number of people:
SELECT COUNT(ID)
FROM Names;

Find Average ID:
SELECT AVG(ID)
FROM Names;

Find Sum of All Salaries:
SELECT SUM(Salary)
FROM Names;

Find People whose name starts with "a":
SELECT * FROM Names
WHERE Name LIKE 'a%';

Find People whose name has "abc":
SELECT * FROM Customers
WHERE CustomerName LIKE '%abc%';

Find people with names "abc","cde","fgh":
SELECT * FROM Names
WHERE Name IN ('abc','cde','fgh');

Find people whose Salaries are in between 100000 and 200000
SELECT * FROM Names
WHERE Salary BETWEEN 10 AND 20;
'''

# Connect to database
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="yourpassword"
# )
# print(mydb)
#
# Create Table
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="yourpassword",
#   database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE Names (Name VARCHAR(255), Address VARCHAR(255))")
#
# Insert in database
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="yourpassword",
#   database="mydatabase"
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO Names (Name, Address) VALUES (%s, %s)"
# val = ("Putin", "Durgapur")
# mycursor.execute(sql, val)
# mydb.commit()
#
#
# Display Table
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="yourpassword",
#   database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM Names")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)