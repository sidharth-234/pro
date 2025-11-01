import sqlite3
import getpass
import datetime
conn=sqlite3.connect('PHARMACY.db')
cursor=conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(20) UNIQUE,
        password TEXT,
        role TEXT NOT NULL CHECK(role IN('admin','pharmacist'))
               
               
               )
''')
# conn.close()

cursor.execute('''
     CREATE TABLE IF NOT EXISTS Medicines(
        medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(30),
        Category VARCHAR(30),
        Quantity INT NOT NULL,
        Price FLOAT NOT NULL,
        date DATE,
        Expiry_date DATE,
        added_by INTEGER,
        FOREIGN KEY(added_by) REFERENCES User(user_id)
        
        )
''') 
# conn.close()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers(
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30),
        contact_no INT

        )
''')
# conn.close()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sales(
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        med_id INT,
        cust_id INT,
        quantity INT,
        total_price FLOAT,
        sale_date DATE,
        FOREIGN KEY(med_id) REFERENCES Medicines(medicine_id),
        FOREIGN KEY(cust_id) REFERENCES Customers(customer_id)
        
        )
''')
conn.close()

def register():
    try:
        print('Register:')
        username=input('enter user name:')
        password=getpass.getpass('enter your password:')
        if len(password)<6:
            print('password should be atleat six character')
            return
         
        role=input('enter role(admin/pharmacist):')
        if role not in ['admin','pharmacist']:
            print('invalid role')
            return
        
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()
        cursor.execute('''INSERT INTO user(user_name,password,role)
                    VALUES(?,?,?)''',(username,password,role))
        print('registered successfully✅')
    except Exception as e:
        print('error❌',e)

    conn.commit()
    conn.close()

def login():
    try:
        print('login:')
        username=input('enter username:')
        password=getpass.getpass('enter password:')
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()
        cursor.execute('''
        SELECT user_id,role FROM user WHERE user_name=? AND password=?
          ''',(username,password))
        user=cursor.fetchone()
        if user: 
           print('login successful✅')
           return user[0],user[1]
        else:
           print('invalid credentials❌')
    except Exception as e:
        print('error❌',e)
    
    conn.commit()
    conn.close()

def logout():
    print('logout😴')
    exit()


def add_medicine(user_id):
    try:
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()
        medicine_name=input('Enter medicine name:')
        category=input('Enter category:')
        quantity=int(input('Enter quantity:'))
        price=float(input('Enter price:'))
        date=input('Enter purchase date:yyyy-mm-dd ')
        exp=input('Expiry date:yyyy-mm-dd ')
        cursor.execute('''
            INSERT INTO Medicines(Name,Category,Quantity,Price,date,Expiry_date,added_by)
                VALUES(?,?,?,?,?,?,?)''',(medicine_name,category,quantity,price,date,exp,user_id))
    
        print('Medicine Added✅')
    except Exception as e:
        print('error❌',e)
    conn.commit()
    conn.close()


def view_medicine():
    try:
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()

        cursor.execute('''
            SELECT * FROM Medicines
        ''',)
        medicine=cursor.fetchall()
        if medicine:
            print('Medicine inventory💊: ')
            for med in medicine:
                print(med)
        else:
            print('No medicines found')
    except Exception as e:
        print('error❌',e)

    conn.commit()
    conn.close()

def search_medicine():
    try:
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()
        id=int(input('Enter medicine id:'))
        data=cursor.execute('''
            SELECT * FROM Medicines WHERE medicine_id=?
        ''',(id,))
        found=data.fetchone()
        if found:
            print('Medicine found💊',found)
        else:
            print('Medicine not found❌')
    except Exception as e:
        print('error❌',e)

    conn.commit()
    conn.close

def update_medicine(user_id):
    try:
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()
        med_id=int(input('Enter medicine id to update:'))
        cursor.execute('''
            SELECT added_by FROM Medicines WHERE medicine_id=?
        ''',(med_id,))
        add=cursor.fetchone()
        if not add or add[0]!=user_id:
            print('Not authorized❌')
            return
        
        new_qnty=int(input('Enter new quantity:'))
        new_price=float(input('Enter new price:'))
    
        
        cursor.execute('''
            UPDATE Medicines SET Quantity=?,Price=? WHERE medicine_id=?
        ''',(new_qnty,new_price,med_id))
        print('Medicine updated✅')
    except ValueError:
      print('invalid entry!!')
    except Exception as e:
      print('error❌',e) 
    conn.commit()
    conn.close()

def Delete_medicine(user_id):
    try:
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()
        med_id=int(input('Enter medicine id:'))
        cursor.execute('''
            SELECT added_by FROM Medicines WHERE medicine_id=?
        ''',(med_id,))
        add=cursor.fetchone()
        if not add or add[0]!=user_id:
            print('Not authorized❌')
            return

        ch=input('are you sure you want to delete y/n:')
        if ch=='y':
            cursor.execute('''
                DELETE FROM Medicines WHERE medicine_id=?
            ''',(med_id,))
            print('medicine deleted✅')
        else:
            print('not deleted!!!')
    except Exception as e:
        print('error❌',e)    
    conn.commit()
    conn.close()

def sell_medicine(user_id):
    try:
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()
        cust_id=int(input('enter customer id:'))
        cust_name=input('enter customer name:')
        contact_no=int(input('enter contact number:'))

        meds_id=int(input('enter medicine id:'))
        quantity=int(input('enter quantity to sell:'))
        cursor.execute('''
          SELECT Quantity,Price FROM Medicines WHERE medicine_id=?
        ''',(meds_id,))
        med=cursor.fetchone()
        if not med:
            print('medicine not found❌')
            return
        elif quantity>med[0]:
            print('Insufficiant Stock❌')
            return
       
        total_price=quantity*med[1]
        sale_date=input('Enter sale date:yyyy-mm-dd')

        cursor.execute('''
                INSERT INTO Customers(customer_id,name,contact_no)
                VALUES(?,?,?)
        ''',(cust_id,cust_name,contact_no))

        cursor.execute('''
                INSERT INTO Sales(med_id,cust_id,quantity,total_price,sale_date)
                VALUES(?,?,?,?,?)       
        ''',(meds_id,cust_id,quantity,total_price,sale_date))
        
        print('Sale Recorded✅')
    except Exception as e:
        print('error❌',e)
    conn.commit()
    conn.close()

def view_sale(user_id):
    try:
        conn=sqlite3.connect('PHARMACY.db')
        cursor=conn.cursor()
        cursor.execute('''
           SELECT * FROM Sales
        ''')
        sales=cursor.fetchall()
        for s in sales:
            print(s)
    except Exception as e:
        print('error❌',e)
    conn.commit()
    conn.close()

      

def medi_store(user_id,role):
    try:
        while True:
            print('-----💊MEDICINE INVENTORY SYSTEM💊---')
            print('--MENU:--')

            if role=='admin':
       
                print('1.Add medicine')
                print('2.View medicine')
                print('3.Search medicine')
                print('4.Update medicine')
                print('5.Delete medicine')
                print('6.sell medicine')
                print('7.View sale')
                print('8.exit')
        
            elif role=='pharmacist':
                print('1.Add medicine')
                print('2.View medicine')
                print('3.Search medicine')
                print('4.Update medicine')
                print('5.Delete medicine')
                print('6.exit')


            choice=int(input('enter choice:'))
            if role=='admin':
        
                if choice==1:
                    add_medicine(user_id)
                elif choice==2:
                    view_medicine()
                elif choice==3:
                    search_medicine()
                elif choice==4:
                    update_medicine(user_id)
                elif choice==5:
                    Delete_medicine(user_id)
                elif choice==6:
                    sell_medicine(user_id)
                elif choice==7:
                    view_sale(user_id)
                else:
                    break

            elif role=='pharmacist':
            
                if choice==1:
                    add_medicine(user_id)
                elif choice==2:
                    view_medicine()
                elif choice==3:
                    search_medicine()
                elif choice==4:
                    update_medicine(user_id)
                elif choice==5:
                    Delete_medicine(user_id)
                else:
                    break
    except Exception as e:
        print('error',e)
            

def main():
    while True:
        print('Menu:')
        print('1. Register🔒')
        print('2. login🔑')
        print('3. logout😴')

        ch=int(input('enter your choice:'))
        if ch==1:
            register()

        elif ch==2:
            user_id,role=login()
            medi_store(user_id,role)

        elif ch==3:
            logout()
main()