#Name:Ms.Ankita Rajshekhar Tambake
#Roll No:A-60(SE)
#Name OF Project: "HOTEL MANAGEMENT SYSTEM"

import sqlite3
from sqlite3 import Error

def connection(Hotel_db):
    conn = None
    try:
        conn = sqlite3.connect(Hotel_db)
    except Error as e:
        print(e)
    return conn

def Insert(conn):
    Borrow_no=int(input("Enter the Borrow number  :"))
    fname =       input("Enter First name         : ")
    mname=        input("Enter Middle name        : ")
    lname=        input("Enter Last name          : ")
    add=          input("Enter Address            : ")
    mobile=       input("Enter Mobile number      : ")
    d1=           input("Enter Cheak In date      : ")
    d2=           input("Enter Cheak Out date     : ")
    Gd=           input("Enter your Gender        : ")
    Mail=         input("Enter E-mail             : ")
    
    sql = '''insert into Hotel(Borrow_no,First_name,Middle_name,Last_name,Address,
    Mobile_no,Cheak_in_date,Cheak_out_date,Gender,Mail) values(?,?,?,?,?,?,?,?,?,?)'''
    cur= conn.cursor()
    data=(Borrow_no,fname,mname,lname,add,mobile,d1,d2,Gd,Mail)
    cur.execute(sql,data)
    conn.commit()
    print("Your Data Is Added Successfully---!!!")
    return cur.lastrowid

def Display_all(conn):
    cur = conn.cursor()
    sql='''select * from Hotel'''
    
    cur.execute(sql)
    rows=cur.fetchall()
    for row in rows:
        print("Borrow No:",row[0],"\nFirst name:",row[1],
              "\nMiddle name:",row[2],"\nLast name:",row[3],
              "\nAddress:",row[4],"\nMobile:",row[5],
              "\nCheak In Date:",row[6],"\nCheak Out Date:",row[7],
              "\nGender:",row[8],"\nMail:",row[9])
        print("\n===========================================================\n")
        
def Display_one(conn):
    cur = conn.cursor()
    Borrow_no=int(input("Enter Borrow number: "))
    print("---------------------")
    sql="select * from Hotel where Borrow_no=?"
    cur.execute(sql,(Borrow_no,))
    rows=cur.fetchall()
    for row in rows:
        print("\nBorrow no : ",row[0], "\nfirst name : ",row[1], "\nMiddle name : ",row[2],
              "\nLast name : ",row[3], "\nAddress : ",row[4],"\nMobile No : ",row[5],
              "\nCheak in date : ",row[6],"\nCheak out date :",row[7],"\nGender :",row[8],"\nMail :",row[9])

def Update(conn):
    cur=conn.cursor()

    Borrow_no=int(input("Enter the Borrow number :"))
    fname =       input("Enter First name        : ")
    mname=        input("Enter Middle name       : ")
    lname=        input("Enter Last name         : ")
    add=          input("Enter Address           : ")
    mobile=       input("Enter Mobile number     : ")
    d1=           input("Enter Cheak In date     : ")
    d2=           input("Enter Cheak Out date    : ")
    Gd=           input("Enter your Gender       : ")
    Mail =        input("Enter E-mail            : ")
    
    data=(Borrow_no,fname,mname,lname,add,mobile,d1,d2,Gd,Mail)
    sql='''update Hotel set Borrow_no=?,First_name=?,Middle_name=?,Last_name=?,Address=?,
    Mobile_no=?,Cheak_in_date=?,Cheak_out_date=?,Gender=?,Mail=?'''
    cur.execute(sql,data)
    conn.commit()
    print("Your Data Is Uploaded Successfully---!!!")
    cur.close()


def Delete(conn):
    Borrow_no= int(input("Enter Your Borrow number: "))
    print("---------------------------")
    sql = 'delete from Hotel where Borrow_no=?'
    cur = conn.cursor()
    cur.execute(sql,(Borrow_no,))
    conn.commit()
    print("Your Data Is deleted Successfully---!!!")

    
def main():
    try:
        database =r"A:\Program Files\Hotel.db"
        conn = connection(database)
        with conn:
            print("-----------------------------------------------------")
            print("***************HOTEL MANAGEMENT SYSTEM***************")
            print("-----------------------------------------------------")
            print("| W E L C O M E    T O    H O T E l    L O T U S |")
            print("-----------------------------------------------------")
            print("1.Enter Customer Data :")
            print("--------------------------------")
            print("2.Enter To Display All Data :")
            print("--------------------------------")
            print("3.Enter To Display One Data :")
            print("--------------------------------")
            print("4.Enter To Update Your Data :")
            print("--------------------------------")
            print("5.Enter To Delete Your Data :")
            print("--------------------------------")
            ch=int(input("Enter the number of your choice --->  "))
            print("--------------------------------")
            if(ch==1):
                id=Insert(conn)
            elif(ch==2):
                id=Display_all(conn)
            elif(ch==3):
                id=Display_one(conn)
            elif(ch==4):
                id=Update(conn)
            else:
                id=Delete(conn)
    except Error as e:
        print("Error in DB Connection",e)

if __name__=="__main__":
    main()
     

