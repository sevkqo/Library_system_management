import mysql.connector
from mysql.connector import Error
import datetime
import re
import schedule
import time

#this code is used for tasks performed once a day in connect with MySql server. It checks if user didn't return book or didn't take book which was booked. In first case,
#code add payments for this users and change date of return for this books, or make book available fot other users.

#connecting with MySql server
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            passwd = 'Samsung123',
            database = 'library_management_system',
            auth_plugin='mysql_native_password'
        )
        print("Connected")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "")
mycursor = connection.cursor(buffered=True)

class books:
    
    def __init__(self, book_id, user_id, title, author, year):
        self.book_id = book_id
        self.user_id = user_id
        self.title = title
        self.author = author
        self.year = year
        self.result_1 = 0
        self.result_2 = 0

#function for checking books return   
    def add_payment(self):
        x = datetime.date.today()
        y = datetime.timedelta(days = 30)
        
        #first, code checks which users didn't return books
        select_users_ = '''SELECT DISTINCT BORROWS.ID_USERS FROM library_management_system.BORROWS
        WHERE CURDATE() > BORROWS.DATEOFRETURN
        AND BORROWS.STATUSOFBORROW = 1;'''
        mycursor.execute(select_users_)
        result_1 = mycursor.fetchall()
        for i in range(len(result_1)):
            result_1[i] = str(result_1[i])
            if not(result_1[i] == '(None,)'):         
                result_1[i] = int(re.sub('[^0-9]', '', result_1[i]))
            else:
                result_1[i] = 0
        print(result_1)
        connection.commit()
        
        #next, it checks how many books they didn't return and add payments on their library account
        for i in range(len(result_1)):
            late_payments_ = '''SELECT SUM(BORROWS.STATUSOFBORROW) FROM library_management_system.BORROWS
            WHERE ID_USERS = %s
            AND CURDATE() > DATEOFRETURN;''' %(result_1[i])
            mycursor.execute(late_payments_)
            result_2 = str(mycursor.fetchone())
            if not(result_2 == '(None,)'):         
                result_2 = int(re.sub('[^0-9]', '', result_2))
            else:
                result_2 = 0
            print(result_2)
            
            add_payment_ = '''INSERT INTO payments (ID_users, AmountOfPayment, DateOfPayment, StatusOfPayment) VALUES ( %s, %s, %s, %s);'''
            val = (result_1[i], result_2*10.0, x+y, 1)
            mycursor.execute(add_payment_, val)
            connection.commit()
        
        #at the end, it assings new date of return books
        next_date_of_return_ = '''UPDATE library_management_system.borrows 
        SET DateOfReturn = "%s"
        WHERE CURDATE() > DateOfReturn AND StatusOfBorrow = 1;''' %(x+y)
        mycursor.execute(next_date_of_return_)
        connection.commit()

#function for checking if reservations are expired       
    def reservation_valid(self):
        
        #code change status of reservations which are expired
        reservation_valid_ = '''UPDATE library_management_system.reservation SET reservation.StatusOfReservation = 0
        WHERE CURDATE() > reservation.EndOfReservation
        AND reservation.StatusOfReservation = 1;'''
        mycursor.execute(reservation_valid_)
        connection.commit()

schedule.every().day.at("00:00").do(books.add_payment,r'C:\Users\sevkq\.spyder-py3\Test_mysql.py')
schedule.every().day.at("00:00").do(books.reservation_valid,r'C:\Users\sevkq\.spyder-py3\Test_mysql.py')

#loop for scheduled tasks
while True:
   
    schedule.run_pending()
    time.sleep(1)