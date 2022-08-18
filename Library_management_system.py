import mysql.connector
from mysql.connector import Error
import datetime
import re
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

#library management system application which works with MySql server. It contains functions connected with books and user of library.

#main window of application
root = tk.Tk()

#dimensions of screens
X_main = 400
Y_main = 800
X_main_center = root.winfo_screenwidth()
Y_main_center = root.winfo_screenheight()

X_main_center = int(X_main_center/2 - X_main/2)
Y_main_center = int(Y_main_center/2 - Y_main/2)

X_window = 400
Y_window = 600

#define title and buttons for main screen
root.title('Library Management System')
root.geometry(f'{X_main}x{Y_main}+{X_main_center}+{Y_main_center}')
root.resizable(False, False)

ttk.Label(root, text = 'Library Management System', font = ('Times New Roman', 22)).pack()

Button_font = font.Font(family='Times New Roman', size=16, weight='bold')
Text_1_font = font.Font(family='Times New Roman', size=14, weight='bold')

Button_borrow = tk.Button(root, text="Borrow", command= lambda: (print("Borrow"), Informations([1,1,0,0,0], 1).open_new_window()))
Button_borrow.pack()
Button_borrow.place(height=40, width=150, x = 20, y = 100)
Button_borrow['font'] = Button_font

Button_return = tk.Button(root, text="Return", command= lambda: (print("Return"), Informations([1,0,0,0,0], 2).open_new_window()))
Button_return.pack()
Button_return.place(height=40, width=150, x = 20, y = 150)
Button_return['font'] = Button_font

Button_reservation = tk.Button(root, text="Reservation", command= lambda: (print("Reservation"), Informations([1,1,0,0,0], 3).open_new_window()))
Button_reservation.pack()
Button_reservation.place(height=40, width=150, x = 20, y = 200)
Button_reservation['font'] = Button_font

Button_reservation_done = tk.Button(root, text="Reserv. done", command= lambda: (print("Reservation done"), Informations([1,0,0,0,0], 4).open_new_window()))
Button_reservation_done.pack()
Button_reservation_done.place(height=40, width=150, x = 20, y = 250)
Button_reservation_done['font'] = Button_font

Button_payment_done = tk.Button(root, text="Payment done", command= lambda: (print("Payment done"), Informations([0,1,0,0,0], 5).open_new_window()))
Button_payment_done.pack()
Button_payment_done.place(height=40, width=150, x = 20, y = 300)
Button_payment_done['font'] = Button_font

Button_add_book = tk.Button(root, text="Add book", command= lambda: (print("Add book"), Informations([0,0,1,1,1], 6).open_new_window()))
Button_add_book.pack()
Button_add_book.place(height=40, width=150, x = 20, y = 350)
Button_add_book['font'] = Button_font

Button_find_by_book = tk.Button(root, text="Find by book", command= lambda: (print("Find by title"), Informations([0,0,1,0,0], 7).open_new_window()))
Button_find_by_book.pack()
Button_find_by_book.place(height=40, width=150, x = 20, y = 400)
Button_find_by_book['font'] = Button_font

Button_find_by_author = tk.Button(root, text="Find by author", command= lambda: (print("Find by author"), Informations([0,0,0,1,0], 8).open_new_window()))
Button_find_by_author.pack()
Button_find_by_author.place(height=40, width=150, x = 20, y = 450)
Button_find_by_author['font'] = Button_font

Button_add_user = tk.Button(root, text="Add user", command= lambda: (print("Add user"), Informations([0,1,1,0,0], 9).open_new_window_2()))
Button_add_user.pack()
Button_add_user.place(height=40, width=150, x = 230, y = 100)
Button_add_user['font'] = Button_font

Button_delete_user = tk.Button(root, text="Delete user", command= lambda: (print("Delete user"), Informations([1,1,1,0,0], 10).open_new_window_2()))
Button_delete_user.pack()
Button_delete_user.place(height=40, width=150, x = 230, y = 150)
Button_delete_user['font'] = Button_font

Button_find_user = tk.Button(root, text="Find user", command= lambda: (print("Find user"), Informations([0,1,1,0,0], 11).open_new_window_2()))
Button_find_user.pack()
Button_find_user.place(height=40, width=150, x = 230, y = 200)
Button_find_user['font'] = Button_font

Button_exit = tk.Button(root, text="Exit", command= lambda: root.destroy())
Button_exit.pack()
Button_exit.place(height=40, width=120, x = 260, y = 750)
Button_exit['font'] = Button_font  

#class for additionals windows, buttons, and functions called in this windows
class Informations:
    
    def __init__(self, Field, Task):
        self.Write_informations = None
        self.Task_done_window = None
        self.Book_id = None
        self.User_id = None
        self.Title = None
        self.Author = None
        self.Year = None
        self.User_id2 = None
        self.First_name = None
        self.Last_name = None
        self.Field = Field
        self.Task = Task
    
    def open_new_window(self):
        self.Write_informations = tk.Toplevel(root)
        self.Write_informations.title("Write informations")
        self.Write_informations.geometry("400x400")
        
        #every task call one function from class books or users 
        if (self.Task == 1):
            def Task_(self):
                Informations.get_input_book_id(self)
                Informations.get_input_user_id(self)
                books(self.Book_id, self.User_id, '', '', '').borrow()
        
        if (self.Task == 2):
            def Task_(self):
                Informations.get_input_book_id(self)
                books(self.Book_id, '', '', '', '').returned()

        if (self.Task == 3):
            def Task_(self):
                Informations.get_input_book_id(self)
                Informations.get_input_user_id(self)
                books(self.Book_id, self.User_id, '', '', '').add_reservation()

        if (self.Task == 4):
            def Task_(self):
                Informations.get_input_book_id(self)
                books(self.Book_id, '', '', '', '').reservation_done()
                
        if (self.Task == 5):
            def Task_(self):
                Informations.get_input_user_id(self)
                books('', self.User_id, '', '', '').payment_done()
        
        if (self.Task == 6):
            def Task_(self):
                Informations.get_input_title(self)
                Informations.get_input_author(self)
                Informations.get_input_year(self)
                books('','', self.Title, self.Author, self.Year).add_book()
                
        if (self.Task == 7):
            def Task_(self):
                Informations.get_input_title(self)
                books('','', self.Title, '', '').find_by_title()
                
            def print_(self):
                Records_ = tk.Text(self.Write_informations)
                Records_.pack(expand=True)
                Records_.place(height=100, width=300, x = 50, y = 220)
                Records_.insert('end', books('', '', self.Title, '', '').find_by_title())
                Records_.config(state='disabled')
                Records_['font'] = Text_1_font
        
        if (self.Task == 8):
            def Task_(self):
                Informations.get_input_author(self)
                books('','', '', self.Author, '').find_by_author()
            
            def print_(self):
                Records_ = tk.Text(self.Write_informations)
                Records_.pack(expand=True)
                Records_.place(height=100, width=300, x = 50, y = 220)
                Records_.insert('end', books('', '', '', self.Author, '').find_by_author())
                Records_.config(state='disabled')
                Records_['font'] = Text_1_font
        
        #define text fields and buttons
        Book_id_ = tk.Text(self.Write_informations)
        Book_id_.pack(expand=True)
        Book_id_.place(height=30, width=100, x = 10, y = 10)
        Book_id_.insert('end', 'Book_id:')
        Book_id_.config(state='disabled')
        Book_id_['font'] = Text_1_font
        
        User_id_ = tk.Text(self.Write_informations)
        User_id_.pack(expand=True)
        User_id_.place(height=30, width=100, x = 10, y = 50)
        User_id_.insert('end', 'User_id:')
        User_id_.config(state='disabled')
        User_id_['font'] = Text_1_font
        
        Title_ = tk.Text(self.Write_informations)
        Title_.pack(expand=True)
        Title_.place(height=30, width=100, x = 10, y = 90)
        Title_.insert('end', 'Title:')
        Title_.config(state='disabled')
        Title_['font'] = Text_1_font
        
        Author_ = tk.Text(self.Write_informations)
        Author_.pack(expand=True)
        Author_.place(height=30, width=100, x = 10, y = 130)
        Author_.insert('end', 'Author:')
        Author_.config(state='disabled')
        Author_['font'] = Text_1_font
        
        Year_ = tk.Text(self.Write_informations)
        Year_.pack(expand=True)
        Year_.place(height=30, width=100, x = 10, y = 170)
        Year_.insert('end', 'Year:')
        Year_.config(state='disabled')
        Year_['font'] = Text_1_font
        
        Button_exit = tk.Button(self.Write_informations, text="Exit", command= lambda: self.Write_informations.destroy())
        Button_exit.pack()
        Button_exit.place(height=40, width=120, x = 260, y = 350)
        Button_exit['font'] = Button_font  
     
        Button_insert_data = tk.Button(self.Write_informations, text="Insert data", command= lambda: (Task_(self), Informations.clear_inputs(self), Informations.task_done(self), print_(self)))
        Button_insert_data.pack()
        Button_insert_data.place(height=40, width=120, x = 20, y = 350)
        Button_insert_data['font'] = Button_font   
        
        if (self.Field[0] == 1):
            self.Book_id_text = tk.Text(self.Write_informations)
            self.Book_id_text.pack(expand=True)
            self.Book_id_text.place(height=30, width=200, x = 190, y = 10)
            self.Book_id_text.config(state='normal')
            self.Book_id_text['font'] = Text_1_font 
        
        if (self.Field[1] == 1):
            self.User_id_text = tk.Text(self.Write_informations)
            self.User_id_text.pack(expand=True)
            self.User_id_text.place(height=30, width=200, x = 190, y = 50)
            self.User_id_text.config(state='normal')
            self.User_id_text['font'] = Text_1_font
    
        if (self.Field[2] == 1):
            self.Title_text = tk.Text(self.Write_informations)
            self.Title_text.pack(expand=True)
            self.Title_text.place(height=30, width=200, x = 190, y = 90)
            self.Title_text.config(state='normal')
            self.Title_text['font'] = Text_1_font
            
        if (self.Field[3] == 1):
            self.Author_text = tk.Text(self.Write_informations)
            self.Author_text.pack(expand=True)
            self.Author_text.place(height=30, width=200, x = 190, y = 130)
            self.Author_text.config(state='normal')
            self.Author_text['font'] = Text_1_font
            
        if (self.Field[4] == 1):
            self.Year_text = tk.Text(self.Write_informations)
            self.Year_text.pack(expand=True)
            self.Year_text.place(height=30, width=200, x = 190, y = 170)
            self.Year_text.config(state='normal')
            self.Year_text['font'] = Text_1_font
            
    def clear_inputs(self):
        if (self.Field[0] == 1):
            self.Book_id_text.delete("1.0","end")
        if (self.Field[1] == 1):
            self.User_id_text.delete("1.0","end")
        if (self.Field[2] == 1):
            self.Title_text.delete("1.0","end")
        if (self.Field[3] == 1):
            self.Author_text.delete("1.0","end")
        if (self.Field[4] == 1):
            self.Year_text.delete("1.0","end")
        
    def get_input_book_id(self):
        self.Book_id = self.Book_id_text.get("1.0","end-1c")
            
    def get_input_user_id(self):
        self.User_id = self.User_id_text.get("1.0","end-1c")
        
    def get_input_title(self):
        self.Title = self.Title_text.get("1.0","end-1c")
            
    def get_input_author(self):
        self.Author = self.Author_text.get("1.0","end-1c")
        
    def get_input_year(self):
        self.Year = self.Year_text.get("1.0","end-1c")

    def task_done(self):
        self.Task_done_window = tk.Toplevel(self.Write_informations)
        self.Task_done_window.title("Task done!")
        self.Task_done_window.geometry("150x200")
        
        self.Task_done_ = tk.Text(self.Task_done_window)
        self.Task_done_.pack(expand=True)
        self.Task_done_.place(height=30, width=100, x = 10, y = 10)
        self.Task_done_.insert('end', 'Task done!')
        self.Task_done_.config(state='disabled')
        self.Task_done_['font'] = Text_1_font

    def open_new_window_2(self):
        self.Write_informations_2 = tk.Toplevel(root)
        self.Write_informations_2.title("Write informations")
        self.Write_informations_2.geometry("400x400")
        
        if (self.Task == 9):
            def Task__(self):
                Informations.get_input_first_name(self)
                Informations.get_input_last_name(self)
                user('', self.First_name, self.Last_name, '', '').add_user()
        
        if (self.Task == 10):
            def Task__(self):
                Informations.get_input_user_id2(self)
                Informations.get_input_first_name(self)
                Informations.get_input_last_name(self)
                user(self.User_id2, self.First_name, self.Last_name, '', '').delete_user()
                
        if (self.Task == 11):
            def Task__(self):
                Informations.get_input_first_name(self)
                Informations.get_input_last_name(self)
                user(self.User_id2, self.First_name, self.Last_name, '', '').find_user()
        
            def print_(self):
                Records_ = tk.Text(self.Write_informations_2)
                Records_.pack(expand=True)
                Records_.place(height=150, width=300, x = 50, y = 150)
                Records_.insert('end', user('', self.First_name, self.Last_name, '', '').find_user())
                Records_.config(state='disabled')
                Records_['font'] = Text_1_font
        
        User_id2_ = tk.Text(self.Write_informations_2)
        User_id2_.pack(expand=True)
        User_id2_.place(height=30, width=100, x = 10, y = 10)
        User_id2_.insert('end', 'User_id:')
        User_id2_.config(state='disabled')
        User_id2_['font'] = Text_1_font

        First_name_ = tk.Text(self.Write_informations_2)
        First_name_.pack(expand=True)
        First_name_.place(height=30, width=100, x = 10, y = 50)
        First_name_.insert('end', 'First name:')
        First_name_.config(state='disabled')
        First_name_['font'] = Text_1_font

        Last_name_ = tk.Text(self.Write_informations_2)
        Last_name_.pack(expand=True)
        Last_name_.place(height=30, width=100, x = 10, y = 90)
        Last_name_.insert('end', 'Last name:')
        Last_name_.config(state='disabled')
        Last_name_['font'] = Text_1_font
        
        Button_exit = tk.Button(self.Write_informations_2, text="Exit", command= lambda: self.Write_informations_2.destroy())
        Button_exit.pack()
        Button_exit.place(height=40, width=120, x = 260, y = 350)
        Button_exit['font'] = Button_font  
     
        Button_insert_data = tk.Button(self.Write_informations_2, text="Insert data", command= lambda: (Task__(self), Informations.clear_inputs_2(self), Informations.task_done_2(self), print_(self)))
        Button_insert_data.pack()
        Button_insert_data.place(height=40, width=120, x = 20, y = 350)
        Button_insert_data['font'] = Button_font   
        
        if (self.Field[0] == 1):
            self.User_id2_text = tk.Text(self.Write_informations_2)
            self.User_id2_text.pack(expand=True)
            self.User_id2_text.place(height=30, width=200, x = 190, y = 10)
            self.User_id2_text.config(state='normal')
            self.User_id2_text['font'] = Text_1_font
            
        if (self.Field[1] == 1):
            self.First_name_text = tk.Text(self.Write_informations_2)
            self.First_name_text.pack(expand=True)
            self.First_name_text.place(height=30, width=200, x = 190, y = 50)
            self.First_name_text.config(state='normal')
            self.First_name_text['font'] = Text_1_font 
    
        if (self.Field[2] == 1):
            self.Last_name_text = tk.Text(self.Write_informations_2)
            self.Last_name_text.pack(expand=True)
            self.Last_name_text.place(height=30, width=200, x = 190, y = 90)
            self.Last_name_text.config(state='normal')
            self.Last_name_text['font'] = Text_1_font
            
    def get_input_user_id2(self):
        self.User_id2 = self.User_id2_text.get("1.0","end-1c")
        
    def get_input_first_name(self):
        self.First_name = self.First_name_text.get("1.0","end-1c")
    
    def get_input_last_name(self):
        self.Last_name = self.Last_name_text.get("1.0","end-1c")
            
    def clear_inputs_2(self):
        if (self.Field[0] == 1):
            self.User_id2_text.delete("1.0","end")
        if (self.Field[1] == 1):
            self.First_name_text.delete("1.0","end")
        if (self.Field[2] == 1):
            self.Last_name_text.delete("1.0","end")
        
    def task_done_2(self):
        self.Task_done_window = tk.Toplevel(self.Write_informations_2)
        self.Task_done_window.title("Task done!")
        self.Task_done_window.geometry("150x200")
        
        self.Task_done_ = tk.Text(self.Task_done_window)
        self.Task_done_.pack(expand=True)
        self.Task_done_.place(height=30, width=100, x = 10, y = 10)
        self.Task_done_.insert('end', 'Task done!')
        self.Task_done_.config(state='disabled')
        self.Task_done_['font'] = Text_1_font
        
#connecting with MySql server
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            passwd = 'xyz',
            database = 'library_management_system',
            auth_plugin='mysql_native_password'
        )
        print("Connected")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "")
mycursor = connection.cursor(buffered=True)

#class for tasks on books, like borrow, add new books, return or add new reservation
class books:
    
    def __init__(self, book_id, user_id, title, author, year):
        self.book_id = book_id
        self.user_id = user_id
        self.title = title
        self.author = author
        self.year = year
        self.result_1 = 0
        self.result_2 = 0
        self.result_3 = 0
        self.result_4 = 0
        
    def check_conditions(self):
        # check if book is already borrowed
        check_1 = 'SELECT sum(StatusOfBorrow) FROM library_management_system.borrows WHERE id_books = %s;' %(self.book_id)
        mycursor.execute(check_1)
        self.result_1 = str(mycursor.fetchone())
        if not(self.result_1 == '(None,)'):         
            self.result_1 = int(re.sub('[^0-9]', '', self.result_1))
        else:
            self.result_1 = 0
        connection.commit()
        
        #check how many books user already has
        check_2 = 'SELECT sum(StatusOfBorrow) FROM library_management_system.borrows WHERE id_users = %s;' %(self.user_id)
        mycursor.execute(check_2)
        self.result_2 = str(mycursor.fetchone())
        if not(self.result_2 == '(None,)'):         
            self.result_2 = int(re.sub('[^0-9]', '', self.result_2))
        else:
            self.result_2 = 0
        connection.commit()
        
        #check if user has any late payments
        check_3 = 'SELECT sum(StatusOfPayment) FROM library_management_system.payments WHERE id_users = %s;' %(self.user_id)
        mycursor.execute(check_3)
        self.result_3 = str(mycursor.fetchone())
        if not(self.result_3 == '(None,)'):         
            self.result_3 = int(re.sub('[^0-9]', '', self.result_3))
        else:
            self.result_3 = 0
        connection.commit()

        return self.result_1, self.result_2, self.result_3
    
    def check_reservation(self):
        # check if book is already reserved
        check_4 = 'SELECT sum(StatusOfReservation) FROM library_management_system.reservation WHERE id_books = %s;' %(self.book_id)
        mycursor.execute(check_4)

        self.result_4 = str(mycursor.fetchone())
        if not(self.result_4 == '(None,)'):         
            self.result_4 = int(re.sub('[^0-9]', '', self.result_4))
        else:
            self.result_4 = 0
        connection.commit()
        
        return self.result_4
    
    def borrow(self):
        
        self.check_conditions()
        self.check_reservation()
        
        x = datetime.date.today()
        y = datetime.timedelta(days = 30)
        borrow_= 'INSERT INTO borrows (ID_books, ID_users, DateOfBorrow, DateOfReturn, StatusOfBorrow) VALUES ( %s, %s, %s, %s, %s);'
        val = (self.book_id, self.user_id, x, x+y, 1)
        
        if (self.result_1 == 0 and self.result_2 < 5 and self.result_3 == 0 and self.result_4 == 0):
            mycursor.execute(borrow_, val)
            connection.commit()
        if (self.result_1 == 1):
            print('Book is already borrowed')
        if (self.result_2 >= 5):
            print('User has borrowed too many books')
        if (self.result_3 > 0):
            print('User has late payments')
        if (self.result_4 > 0):
            print('Book is already reserved')
        
    def returned(self):
        returned_ = '''UPDATE borrows SET StatusOfBorrow = 0
        WHERE ID_books = %s;''' %(self.book_id)
        mycursor.execute(returned_)
        connection.commit()
    
    def add_reservation(self):

        self.check_conditions()
        
        x = datetime.date.today()
        y = datetime.timedelta(days = 7)
        add_reservation_ = '''INSERT INTO reservation (ID_books, ID_users, DateOfReservation, EndOfReservation, StatusOfReservation) 
        VALUES ( %s, %s, %s, %s, %s);'''
        val = (self.book_id, self.user_id, x, x+y, 1)
        
        if (self.result_1 == 0 and self.result_2 < 5 and self.result_3 == 0):
            mycursor.execute(add_reservation_, val)
            connection.commit()
        if (self.result_1 == 1):
            print('Book is already borrowed')
        if (self.result_2 >= 5):
            print('User has borrowed too many books')
        if (self.result_3 > 0):
            print('User has late payments')  
        
    def reservation_done(self):
        reservation_done_ = '''UPDATE reservation SET StatusOfReservation = 0
        WHERE ID_books = %s;''' %(self.book_id)
        mycursor.execute(reservation_done_)
        connection.commit()
        
    def payment_done(self):
        payment_done_ = '''UPDATE library_management_system.payments
        SET StatusOfPayment = 0
        WHERE ID_users = %s;''' %(self.user_id)
        mycursor.execute(payment_done_)
        connection.commit()
    
    def add_book(self):
        add_book_ = 'INSERT INTO books (Title, Author, YearOfRelease) VALUES ( %s, %s, %s);'
        val = (self.title, self.author, self.year)
        mycursor.execute(add_book_, val)
        connection.commit()
    
    def find_by_title(self):
        find_by_title_ = 'SELECT * FROM library_management_system.BOOKS WHERE TITLE = "%s" ORDER BY AUTHOR ASC;' %(self.title)
        mycursor.execute(find_by_title_)
        result = mycursor.fetchall()
        print(result)
        connection.commit()
        return result
        
    def find_by_author(self):
        find_by_author_ = 'SELECT * FROM library_management_system.BOOKS WHERE AUTHOR = "%s" ORDER BY AUTHOR ASC;' %(self.author)
        mycursor.execute(find_by_author_)
        result = mycursor.fetchall()
        print(result)
        connection.commit()
        return result
   
#class for tasks on users, like add new user, delete user or find one  
class user:
    
    def __init__(self, user_id, first_name, last_name, date_of_registration, payments):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_registration = date_of_registration
        self.payments = payments
    
    def add_user(self):
        add_user_ = 'INSERT INTO users (FirstName, LastName, DateOfRegistration, AmountOfActualPayments) VALUES ( %s, %s, %s, %s);'
        val = (self.first_name, self.last_name, datetime.date.today(), 0.0)
        mycursor.execute(add_user_, val)
        connection.commit()
        
    def delete_user(self):
        print(self.user_id, self.first_name, self.last_name)
        delete_user_ = 'DELETE FROM library_management_system.users WHERE id = %s and FirstName = "%s" and LastName = "%s";' %(self.user_id, self.first_name, self.last_name)
        mycursor.execute(delete_user_)
        connection.commit()
        
    def find_user(self):
        print(self.first_name, self.last_name)
        find_user_ = 'SELECT * FROM library_management_system.users WHERE FirstName = "%s" and LastName = "%s" ORDER BY users.ID ASC;' %(self.first_name, self.last_name)
        mycursor.execute(find_user_)
        result = mycursor.fetchall()
        print(result)
        connection.commit()
        return result

root.mainloop()

