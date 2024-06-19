import sqlite3
import tkinter.messagebox
from tkinter import *
from PIL import Image,ImageTk
import datetime
class sqlite:
    def create_table_student(self):
        conn = sqlite3.connect('datastore.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE Data_Stored (
                Student_id text,
               Name text,
               membership text,
               bookname text,
              book_id text,
               issuedate text,
               duedate text)""")
        conn.commit()
        conn.close()
    def create_table_book(self):
        conn = sqlite3.connect('Booksdetail.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE Books_details(
                book_no text,
                title text,
                author text,
                avail text)""")
        conn.commit()
        conn.close()
class gui(sqlite):
    def __init__(self):
        self.root=Tk()
        self.root2 = Toplevel()
        self.root3 = Toplevel()
        self.root4 = Toplevel()
    def image_create(self):
        self.bg1 = Image.open("pic3.png")
        self.photo3 = ImageTk.PhotoImage(self.bg1)
        self.bg2 = Image.open("download.png")
        self.photo = ImageTk.PhotoImage(self.bg2)
        self.bg3 = Image.open("ok2.png")
        self.photo2 = ImageTk.PhotoImage(self.bg3)
    def login(self):
        self.root2.withdraw()
        self.root3.withdraw()
        self.root4.withdraw()
        self.image_create()
        self.root.geometry("1920x1000")
        my_canvas = Canvas(self.root, width=800, height=800, bg="#F0F0F0")
        my_canvas.pack(fill="both", expand=TRUE)
        my_canvas.create_rectangle(450, 30, 1200, 620, fill="#D3F0FE")
        my_canvas.create_rectangle(70, 30, 450, 620, fill="white")
        my_canvas.create_image(155,60, image=self.photo, anchor="nw")
        my_canvas.create_image(500,200, image=self.photo2, anchor="nw")
        my_canvas.create_text(250,320, text="UIT Library", font=("Helvetica", 40, "bold"), fill="black")
        my_canvas.create_text(255,370, text="Login", font=("Helvetica", 30, "bold"), fill="Black")
        my_canvas.create_text(250, 420, text="Student ID:", font=("Helvetica", 18), fill="Black")
        my_canvas.create_text(250, 470, text="Name:", font=("Helvetica", 18), fill="Black")
        button = Button(self.root, text="Submit", command=self.dashboard, relief=GROOVE, padx=20)
        my_canvas.create_window(210, 570, anchor="nw", window=button)
        self.root.title("Library Management System")
        studentid = StringVar()
        name = StringVar()
        self.member=BooleanVar()
        membership=Checkbutton(self.root,text="Click here to apply for membership",variable=self.member,bg="white")
        my_canvas.create_window(270,545,window=membership)
        self.studententry = Entry(self.root, textvariable=studentid, font=10,bd=2)
        self.nameentry = Entry(self.root, textvariable=name, font=10,bd=2)
        my_canvas.create_window(250, 445, window=self.studententry)
        my_canvas.create_window(250, 500, window=self.nameentry)
        self.root.mainloop()
    def dashboard(self):
        if self.studententry.get()!="" and self.nameentry.get()!="":
            self.root.withdraw()
            self.root3.withdraw()
            self.root4.withdraw()
            self.root2.deiconify()
            self.root2.title("Library Management System")
            self.root2.geometry("1920x1000")
            my_canvas2 = Canvas(self.root2, width=800, height=800, bg="#F0F0F0")
            my_canvas2.pack(fill="both", expand=TRUE)
            my_canvas2.create_rectangle(450, 30, 1200, 620, fill="#9ED4F1")
            my_canvas2.create_rectangle(70, 30, 450, 620, fill="white")
            my_canvas2.create_image(155, 60, image=self.photo, anchor="nw")
            my_canvas2.create_image(500, 80, image=self.photo3, anchor="nw")
            my_canvas2.create_text(250, 320, text="UIT Library", font=("Helvetica", 30, "bold"), fill="black")
            my_canvas2.create_text(260, 370, text="Type of book",anchor="center",font=("Helvetica", 20, "bold"), fill="black")
            button1 = Button(self.root2, text="Add Book", command=self.addbook,font=20)
            button2 = Button(self.root2, text="Remove Book", command=self.removebook,font=20)
            button3 = Button(self.root2, text="Issue Book", command=self.issuebook,font=20)
            button4 = Button(self.root2, text="Return Book", command=self.returnbook,font=20)
            my_canvas2.create_window(260,420,anchor="center",window=button1)
            my_canvas2.create_window(260, 470, anchor="center",window=button2)
            my_canvas2.create_window(260, 520, anchor="center",window=button3)
            my_canvas2.create_window(260, 570, anchor="center", window=button4)
            self.root2.mainloop()


    def addbook(self):
        self.root2.withdraw()
        self.root3.deiconify()
        self.root3.geometry("1920x1080")
        my_canvas3 = Canvas(self.root3, width=800, height=800, bg="#F0F0F0")
        my_canvas3.pack(fill="both", expand=TRUE)
        my_canvas3.create_rectangle(450, 30, 1200, 620, fill="#9ED4F1")
        my_canvas3.create_rectangle(70, 30, 450, 620, fill="white")
        my_canvas3.create_image(155, 60, image=self.photo, anchor="nw")
        my_canvas3.create_image(500, 80, image=self.photo3, anchor="nw")
        my_canvas3.create_text(250, 330, text="UIT Library", font=("Helvetica", 30, "bold"), fill="black")
        my_canvas3.create_text(225, 370, text="Enter Book ID:", anchor="center", font=("Helvetica", 15),
                               fill="black")
        my_canvas3.create_text(240, 430, text="Enter Book Name:", anchor="center", font=("Helvetica", 15),
                               fill="black")
        my_canvas3.create_text(245, 495, text="Enter Author Name:", anchor="center", font=("Helvetica", 15),
                               fill="black")
        book_no=StringVar()
        book_author = StringVar()
        book_title = StringVar()
        self.book_id = Entry(self.root3, textvariable=book_no, font=10, bd=2)
        self.bookname = Entry(self.root3, textvariable=book_title, font=10, bd=2)
        self.book_author = Entry(self.root3, textvariable=book_author, font=10, bd=2)
        my_canvas3.create_window(250, 460, window=self.bookname)
        my_canvas3.create_window(250, 400, window=self.book_id)
        my_canvas3.create_window(250, 520, window=self.book_author)
        button = Button(self.root3, text="Submit", command=self.add, relief=GROOVE, padx=20)
        my_canvas3.create_window(220, 550, anchor="nw", window=button)
        self.root3.mainloop()


    def report(self):
        if self.book_no_issue.get()!="" and self.bookname_issue.get()!="":
            self.get_records_book()
            self.get_records_students()
            for i in self.records_book:
                if i[0]==self.book_no_issue.get():
                    if i[3]=="available":
                        self.root3.withdraw()
                        self.root4 = Toplevel()
                        self.root4.geometry("1920x1080")
                        my_canvas4 = Canvas(self.root4, width=800, height=800, bg="#F0F0F0")
                        my_canvas4.pack(fill="both", expand=TRUE)
                        my_canvas4.create_rectangle(450, 30, 1200, 620, fill="#9ED4F1")
                        my_canvas4.create_rectangle(70, 30, 450, 620, fill="white")
                        my_canvas4.create_image(155, 60, image=self.photo, anchor="nw")
                        my_canvas4.create_image(500, 80, image=self.photo3, anchor="nw")
                        my_canvas4.create_text(250, 330, text="UIT Library:", font=("Helvetica", 30, "bold"), fill="black")
                        my_canvas4.create_text(150, 380, text="Roll no:", font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(150, 410, text="Name:", font=("Helvetica", 15,), fill="black")
                        my_canvas4.create_text(150, 440, text="Membership:", font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(150, 470, text="Issue Date:", font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(150, 500, text="Due Date:", font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(150, 530, text="Book id:", font=("Helvetica", 15), fill="black")
                        self.submit()
                        self.get_records_students()
                        for i in self.records_student:
                            if i[0] == self.studententry.get():
                                self.record = i
                        my_canvas4.create_text(300, 380, text=self.studententry.get(), font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(300, 410, text=self.nameentry.get(), font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(300, 440, text=self.membership, font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(300, 470, text=self.record[5], font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(300, 500, text=self.record[6], font=("Helvetica", 15), fill="black")
                        my_canvas4.create_text(300, 530, text=self.record[3], font=("Helvetica", 15), fill="black")
                        button = Button(self.root4, text="Dashboard", command=self.pressed, relief=GROOVE, padx=20)
                        my_canvas4.create_window(220, 560, anchor="nw", window=button)
                        self.root4.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Search Error', "Book not available")
    def pressed(self):
        self.update_avail(0)
    def issuebook(self):
        self.root2.withdraw()
        self.root3 = Toplevel()
        self.root3.geometry("1920x1080")
        my_canvas3 = Canvas(self.root3, width=800, height=800, bg="#F0F0F0")
        my_canvas3.pack(fill="both", expand=TRUE)
        my_canvas3.create_rectangle(450, 30, 1200, 620, fill="#9ED4F1")
        my_canvas3.create_rectangle(70, 30, 450, 620, fill="white")
        my_canvas3.create_image(155, 60, image=self.photo, anchor="nw")
        my_canvas3.create_image(500, 80, image=self.photo3, anchor="nw")
        my_canvas3.create_text(250, 330, text="UIT Library", font=("Helvetica", 30, "bold"), fill="black")
        my_canvas3.create_text(240, 380, text="Enter Book ID:", anchor="center", font=("Helvetica", 18),
                               fill="black")
        my_canvas3.create_text(255, 450, text="Enter Book Name:", anchor="center",font=("Helvetica", 18), fill="black")
        id=StringVar()
        book=StringVar()
        self.book_no_issue = Entry(self.root3, textvariable=id, font=10, bd=2)
        self.bookname_issue = Entry(self.root3, textvariable=book, font=10,bd=2)
        my_canvas3.create_window(250, 410, window=self.book_no_issue)
        my_canvas3.create_window(250, 480, window= self.bookname_issue)
        button = Button(self.root3, text="Submit",command=self.report,relief=GROOVE, padx=20)
        my_canvas3.create_window(220, 510, anchor="nw", window=button)
        self.root3.mainloop()

    def returnbook(self):
        self.root2.withdraw()
        self.root3 = Toplevel()
        self.root3.geometry("1920x1080")
        my_canvas3 = Canvas(self.root3, width=800, height=800, bg="#F0F0F0")
        my_canvas3.pack(fill="both", expand=TRUE)
        my_canvas3.create_rectangle(450, 30, 1200, 620, fill="#9ED4F1")
        my_canvas3.create_rectangle(70, 30, 450, 620, fill="white")
        my_canvas3.create_image(155, 60, image=self.photo, anchor="nw")
        my_canvas3.create_image(500, 80, image=self.photo3, anchor="nw")
        my_canvas3.create_text(250, 330, text="UIT Library", font=("Helvetica", 30, "bold"), fill="black")
        my_canvas3.create_text(250, 400, text="Enter book id:", anchor="center", font=("Helvetica",18),
                               fill="black")
        book_id= StringVar()
        self.book_no_return = Entry(self.root3, textvariable=book_id, font=10,bd=2)
        my_canvas3.create_window(250, 450, window=self.book_no_return)
        button = Button(self.root3, text="Submit", command=self.return_book, relief=GROOVE, padx=20)
        my_canvas3.create_window(220, 490, anchor="nw", window=button)
        self.root3.mainloop()
    def return_book(self):
        self.get_records_book()
        self.get_records_students()
        self.select(self.studententry.get())
        try:
            for ok in self.records_book:
                if self.record[4] == self.book_no_return.get():
                    if self.record[0]==self.studententry.get():
                        if ok[3] == "notavailable":
                            for ok in self.records_student:
                                due_date=datetime.datetime.strptime(ok[6],'%Y-%m-%d').date()
                                if ok[0]==self.studententry.get() and self.book_no_return.get()==ok[4]:
                                    check=due_date>=datetime.date.today()
                                    if check==True:
                                        tkinter.messagebox.showinfo('Return', "Thank you for returning!")
                                    else:
                                        tkinter.messagebox.showinfo('Return late', "Please pay the fine for returning late.")

                            conn = sqlite3.connect('datastore.db')
                            c = conn.cursor()
                            c.execute(("DELETE FROM Data_Stored WHERE book_id=?"),(self.book_no_return.get(),))
                            conn.commit()
                            c.close()
                            self.update_avail(1)
                    else:
                        tkinter.messagebox.showinfo('Wrong account', "U cant return book of someone else.")
                        self.dashboard()
                else:
                    tkinter.messagebox.showinfo('Wrong Book ID', "Please re-check Book ID.")
        except:
            tkinter.messagebox.showinfo('Search Error', "No user found with book")
            self.dashboard()

    def removebook(self):
            self.root2.withdraw()
            self.root3 = Toplevel()
            self.root3.geometry("1920x1080")
            my_canvas3 = Canvas(self.root3, width=800, height=800, bg="#F0F0F0")
            my_canvas3.pack(fill="both", expand=TRUE)
            my_canvas3.create_rectangle(450, 30, 1200, 620, fill="#9ED4F1")
            my_canvas3.create_rectangle(70, 30, 450, 620, fill="white")
            my_canvas3.create_image(155, 60, image=self.photo, anchor="nw")
            my_canvas3.create_image(500, 80, image=self.photo3, anchor="nw")
            my_canvas3.create_text(260, 330, text="UIT Library", font=("Helvetica", 30, "bold"), fill="black")
            my_canvas3.create_text(260, 390, text="Enter Book ID:", anchor="center", font=("Helvetica", 18),
                                   fill="black")
            book = StringVar()
            self.bookid_remove = Entry(self.root3, textvariable=book, font=10,bd=2)
            my_canvas3.create_window(260, 430, window=self.bookid_remove)
            button = Button(self.root3, text="Remove", command=self.remove, relief=GROOVE, padx=20)
            my_canvas3.create_window(230, 460, anchor="nw", window=button)
            self.root3.mainloop()
    def update_avail(self,no):
        conn = sqlite3.connect('Booksdetail.db')
        c = conn.cursor()
        # c.execute("SELECT *, oid FROM Data_stored")
        # records = c.fetchall()
        if no==1:
            entry=(self.book_no_return.get(),)
        else:
            entry = (self.book_no_issue.get(),)
        try:
            if no==1:
                c.execute(('''UPDATE Books_details SET avail='available' WHERE book_no=?'''),entry)
            else:
                c.execute(('''UPDATE Books_details SET avail='notavailable' WHERE book_no=?'''), entry)
        except:
            tkinter.messagebox.showinfo('Search Error', "Please re-enter Book ID!")
        conn.commit()
        c.close()
        self.dashboard()


    def remove(self):
        conn = sqlite3.connect('Booksdetail.db')
        c=conn.cursor()
        #c.execute("SELECT *, oid FROM Data_stored")
        #records = c.fetchall()
        entry=(self.bookid_remove.get(),)
        try:
            c.execute(("DELETE FROM Books_details WHERE book_no=?;"),entry)
        except:
            tkinter.messagebox.showinfo('Search Error',"Please re-enter Book ID")
        conn.commit()
        c.close()
        self.dashboard()
    def add(self):
        if self.book_id.get()!='' and self.bookname.get()!='' and self.book_author.get()!='':
            conn = sqlite3.connect('Booksdetail.db')
            c = conn.cursor()
            c.execute("INSERT INTO Books_details VALUES(:book_no, :title, :author,:avail)",
                      {
                          'book_no': self.book_id.get(),
                          'title': self.bookname.get(),
                          'author': self.book_author.get(),
                          'avail': "available"

                      })
            conn.commit()
            conn.close()
            self.dashboard()
    def get_records_students(self):
        conn = sqlite3.connect('datastore.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM Data_stored")
        self.records_student = c.fetchall()
        conn.commit()
        conn.close()
    def get_records_book(self):
        conn = sqlite3.connect('Booksdetail.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM Books_details")
        self.records_book = c.fetchall()

        conn.commit()
        conn.close()

    def submit(self):
        conn = sqlite3.connect('datastore.db')
        c = conn.cursor()
        today = datetime.date.today()
        if self.member.get() == 1:
            self.membership = "Yes"
        else:
            self.membership = "No"
        c.execute(
            "INSERT INTO Data_stored VALUES(:student_id, :name, :membership, :bookname,  :book_id,  :issuedate,  :duedate)",
            {
                'student_id': self.studententry.get(),
                'name': self.nameentry.get(),
                'membership': self.membership,
                'bookname': self.bookname_issue.get(),
                'book_id': self.book_no_issue.get(),
                'issuedate': str(today),
                'duedate': str(today + datetime.timedelta(days=7))

            })
        conn.commit()
        conn.close()
    def select(self,id):
        conn = sqlite3.connect('datastore.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Data_Stored where Student_id=?",(id,))

        fetch=c.fetchall()
        self.record=[]
        for i in list(fetch):
            for j in i:
                self.record.append(j)
        conn.commit()
        conn.close()

#driver code
a=gui()
a.login()