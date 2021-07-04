from dbhelper import DBHelper
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
import shutil


class Tinder():
    def __init__(self):
        #conncet with database
        self.db = DBHelper()
        self.user_data = None
        #load the gui of the login form
        self.load_gui_window(self.load_login_gui)
    def load_gui_window(self,gui_type,data = None,row_no = 1):
        self.root = Tk()
        self.root.title("Tinder")
        self.root.configure(background = "#FF5375")
        self.root.maxsize(400,600)
        self.root.minsize(400,600)

        if data is None:
            gui_type()
        else:
            gui_type(data,row_no)
        self.root.mainloop()

    def load_register_gui(self):
        self.label1 = Label(self.root, text="Tinder", bg="#FF5375", fg="#fff")
        self.label1.pack(pady=(20, 20))
        self.label1.configure(font=("Times", 32, "bold"))

        self.label2 = Label(self.root, text="Register to proceed", bg="#FF5375", fg="#fff")
        self.label2.pack(pady=(10, 20))
        self.label2.configure(font=("Times", 20, "italic"))

        self.label0 = Label(self.root, text="Enter Name", bg="#FF5375", fg="#fff")
        self.label0.pack(pady=(10, 5))
        self.label0.configure(font=("Times", 14))

        self.name_input = Entry(self.root)
        self.name_input.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.label3 = Label(self.root, text="Enter Email", bg="#FF5375", fg="#fff")
        self.label3.pack(pady=(10, 5))
        self.label3.configure(font=("Times", 14))

        self.email_input = Entry(self.root)
        self.email_input.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.label4 = Label(self.root, text="Enter Password", bg="#FF5375", fg="#fff")
        self.label4.pack(pady=(10, 5))
        self.label4.configure(font=("Times", 14))

        self.password_input = Entry(self.root, show="*")
        self.password_input.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.registration = Button(self.root, text="Register", font=30, bg="#fff", width=30, height=1,
                            command=lambda: self.reg_validation())
        self.registration.pack(pady=(10, 10))

        self.label5 = Label(self.root, text="Already a member?", bg="#FF5375", fg="#fff")
        self.label5.pack(pady=(10, 5))
        self.label5.configure(font=("Times", 12))

        self.login_btn = Button(self.root, text="Login", font=30, bg="#fff", width=15, height=1,command = lambda : self.load_new_gui(self.load_login_gui))
        self.login_btn.pack(pady=(10, 10))


    def load_login_gui(self):

        self.label1 = Label(self.root,text = "Tinder", bg = "#FF5375",fg = "#fff")
        self.label1.pack(pady=(20,20))
        self.label1.configure(font=("Times",32,"bold"))

        self.label2 = Label(self.root, text="Login to proceed", bg="#FF5375", fg="#fff")
        self.label2.pack(pady=(10, 20))
        self.label2.configure(font=("Times", 20, "italic"))

        self.label3 = Label(self.root, text="Enter Email", bg="#FF5375", fg="#fff")
        self.label3.pack(pady=(10, 5))
        self.label3.configure(font=("Times", 14))

        self.email_input = Entry(self.root)
        self.email_input.pack(pady=(2,10),ipady = 7,ipadx = 80)

        self.label4 = Label(self.root, text="Enter Password", bg="#FF5375", fg="#fff")
        self.label4.pack(pady=(10, 5))
        self.label4.configure(font=("Times", 14))

        self.password_input = Entry(self.root,show = "*")
        self.password_input.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.login = Button(self.root,text="Login",font=30, bg="#fff", width=30, height=1,command = lambda:self.login_validation())
        self.login.pack(pady=(10,10))

        self.label5 = Label(self.root, text="Not a member?", bg="#FF5375", fg="#fff")
        self.label5.pack(pady=(10, 5))
        self.label5.configure(font=("Times", 12))

        self.reg = Button(self.root, text="Register", font=30, bg="#fff", width=15, height=1,command = lambda : self.load_new_gui(self.load_register_gui))
        self.reg.pack(pady=(10, 10))

    def load_new_gui(self,new_gui,data = None,row_no = 1):
        self.root.destroy()
        if data is None:
            self.load_gui_window(new_gui)
        else:
            self.load_gui_window(new_gui,data,row_no)
    def load_home_menu(self):
        self.root.destroy()
        self.load_gui_window(self.load_user_profile_gui)


    def header_menu(self):
        menu = Menu(self.root)
        self.root.config(menu = menu)
        filemenu = Menu(menu)
        menu.add_cascade(label = "Home",menu = filemenu)
        filemenu.add_command(label = "My Profile",command = lambda : self.load_home_menu())
        filemenu.add_command(label = "Edit Profile",command = lambda : self.load_edit_profile())
        filemenu.add_command(label = "View Profile",command = lambda : self.view_profile(1))
        filemenu.add_command(label = "LogOut",command = lambda:self.logout())

        helpmenu = Menu(menu)
        menu.add_cascade(label = "Proposals",menu = helpmenu)
        helpmenu.add_command(label = "My Proposals",command = lambda : self.show_proposals(1))
        helpmenu.add_command(label = "My Requests",command = lambda : self.show_requests(1))
        helpmenu.add_command(label = "My Matches",command = lambda : self.show_matches(1))

    def load_edit_profile(self):
        # load the form
        self.load_new_gui(self.edit_profile_gui)
    def edit_profile_gui(self):

        self.header_menu()

        self.label1 = Label(self.root, text="Tinder", bg="#FF5375", fg="#fff")
        self.label1.pack(pady=(20, 20))
        self.label1.configure(font=("Times", 32, "bold"))

        self.label2 = Label(self.root, text="Edit Profile", bg="#FF5375", fg="#fff")
        self.label2.pack(pady=(10, 20))
        self.label2.configure(font=("Times", 20, "italic"))

        self.label0 = Label(self.root, text="Edit Password", bg="#FF5375", fg="#fff")
        self.label0.pack(pady=(10, 5))
        self.label0.configure(font=("Times", 14))

        v = StringVar(self.root, value = self.user_data[3])

        self.edit_password_input = Entry(self.root,textvariable = v,show="*")
        self.edit_password_input.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.label3 = Label(self.root, text="Edit City", bg="#FF5375", fg="#fff")
        self.label3.pack(pady=(10, 5))
        self.label3.configure(font=("Times", 14))

        v = StringVar(self.root, value=self.user_data[6])

        self.edit_city_input = Entry(self.root,textvariable = v)
        self.edit_city_input.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.label4 = Label(self.root, text="Enter About Me", bg="#FF5375", fg="#fff")
        self.label4.pack(pady=(10, 5))
        self.label4.configure(font=("Times", 14))

        v = StringVar(self.root, value=self.user_data[8])

        self.edit_about_input = Entry(self.root,textvariable = v)
        self.edit_about_input.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.edit_btn = Button(self.root, text="Edit Profile", font=30, bg="#fff", width=30, height=1,
                                   command=lambda: self.edit_profile())
        self.edit_btn.pack(pady=(10, 10))

    def edit_profile(self):
        password = self.edit_password_input.get()
        city = self.edit_city_input.get()
        about = self.edit_about_input.get()

        response = self.db.edit_user_profile(self.user_data[0],password,city,about)
        if response == 1:
            messagebox.showinfo("Messege","Profile Updated")
        else:
            messagebox.showerror("Error","Some error occured")




    def show_matches(self,row_no):

        data = self.db.fetch_one_match(self.user_data[0],row_no)
        print(data[0])
        self.load_new_gui(self.load_matches_gui,data[0],row_no)



    def show_requests(self, row_no):
        data = self.db.fetch_one_request(self.user_data[0], row_no)
        print (data[0])
        self.load_new_gui(self.load_requests_gui, data[0], row_no)


    def show_proposals(self,row_no):
        data = self.db.fetch_one_proposal(self.user_data[0],row_no)
        self.load_new_gui(self.load_proposals_gui, data[0], row_no)

    def view_profile(self,row_no,btn = None):

        # find total users(rows) in the table
        num_users = self.db.count_users()

        if num_users[0][0] < row_no:
            messagebox.showerror("Error","This is the last user")
        if row_no < 0:
            messagebox.showerror("Error", "This is the first user")
        else:
            data = self.db.fetch_user(row_no)
            if data[0][2] == self.user_data[2]:
                if btn == "Next" or btn is None:
                    row_no = row_no + 1
                else:
                    row_no = row_no - 1
                data = self.db.fetch_user(row_no)

            # load the gui of other users
            self.load_new_gui(self.load_other_user_profile_gui,data[0],row_no)

    def load_matches_gui(self,data,row_no):
        self.header_menu()

        # load dp
        imageUrl = "image/user.jpg"

        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        self.label5 = Label(self.root, text=data[4], bg="#FF5375", fg="#fff")
        self.label5.pack(pady=(10, 5))
        self.label5.configure(font=("Times", 12))

        # age
        if data[7] == 0:
            self.label6 = Label(self.root, text="Age:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label6 = Label(self.root, text="Age:  " + str(data[7]), bg="#FF5375", fg="#fff")
        self.label6.pack(pady=(10, 5))
        self.label6.configure(font=("Times", 12))

        # gender
        if data[8] == "":
            self.label7 = Label(self.root, text="Gender:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label7 = Label(self.root, text="Gender:  " + str(data[8]), bg="#FF5375", fg="#fff")
        self.label7.pack(pady=(10, 5))
        self.label7.configure(font=("Times", 12))

        # city
        if data[9] == "":
            self.label8 = Label(self.root, text="City:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label8 = Label(self.root, text="City:  " + str(data[9]), bg="#FF5375", fg="#fff")
        self.label8.pack(pady=(10, 5))
        self.label8.configure(font=("Times", 12))

        # bio
        if data[11] == "":
            self.label9 = Label(self.root, text="About me:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label9 = Label(self.root, text="About me:  " + str(data[11]), bg="#FF5375", fg="#fff")
        self.label9.pack(pady=(10, 5))
        self.label9.configure(font=("Times", 12))

        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.prev = Button(self.root, text="Previous", font=30, bg="#fff", width=15, height=1,
                           command=lambda: self.show_matches(row_no - 1))
        self.prev.pack(side=LEFT)

        self.next = Button(self.root, text="Next", font=30, bg="#fff", width=15, height=1,
                           command=lambda: self.show_matches(row_no + 1))
        self.next.pack(side=RIGHT)
    def load_requests_gui(self,data,row_no):
        self.header_menu()

        # load dp
        imageUrl = "image/user.jpg"

        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        self.label5 = Label(self.root, text=data[4], bg="#FF5375", fg="#fff")
        self.label5.pack(pady=(10, 5))
        self.label5.configure(font=("Times", 12))

        # age
        if data[7] == 0:
            self.label6 = Label(self.root, text="Age:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label6 = Label(self.root, text="Age:  " + str(data[7]), bg="#FF5375", fg="#fff")
        self.label6.pack(pady=(10, 5))
        self.label6.configure(font=("Times", 12))

        # gender
        if data[8] == "":
            self.label7 = Label(self.root, text="Gender:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label7 = Label(self.root, text="Gender:  " + str(data[8]), bg="#FF5375", fg="#fff")
        self.label7.pack(pady=(10, 5))
        self.label7.configure(font=("Times", 12))

        # city
        if data[9] == "":
            self.label8 = Label(self.root, text="City:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label8 = Label(self.root, text="City:  " + str(data[9]), bg="#FF5375", fg="#fff")
        self.label8.pack(pady=(10, 5))
        self.label8.configure(font=("Times", 12))

        # bio
        if data[11] == "":
            self.label9 = Label(self.root, text="About me:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label9 = Label(self.root, text="About me:  " + str(data[11]), bg="#FF5375", fg="#fff")
        self.label9.pack(pady=(10, 5))
        self.label9.configure(font=("Times", 12))

        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.prev = Button(self.root, text="Previous", font=30, bg="#fff", width=15, height=1,
                           command=lambda: self.show_requests(row_no - 1))
        self.prev.pack(side=LEFT)

        self.next = Button(self.root, text="Next", font=30, bg="#fff", width=15, height=1,
                           command=lambda: self.show_requests(row_no + 1))
        self.next.pack(side=RIGHT)

    def load_proposals_gui(self,data,row_no):
        self.header_menu()

        # load dp
        imageUrl = "image/user.jpg"

        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        self.label5 = Label(self.root, text=data[4], bg="#FF5375", fg="#fff")
        self.label5.pack(pady=(10, 5))
        self.label5.configure(font=("Times", 12))

        # age
        if data[7] == 0:
            self.label6 = Label(self.root, text="Age:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label6 = Label(self.root, text="Age:  " + str(data[7]), bg="#FF5375", fg="#fff")
        self.label6.pack(pady=(10, 5))
        self.label6.configure(font=("Times", 12))

        # gender
        if data[8] == "":
            self.label7 = Label(self.root, text="Gender:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label7 = Label(self.root, text="Gender:  " + str(data[8]), bg="#FF5375", fg="#fff")
        self.label7.pack(pady=(10, 5))
        self.label7.configure(font=("Times", 12))

        # city
        if data[9] == "":
            self.label8 = Label(self.root, text="City:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label8 = Label(self.root, text="City:  " + str(data[9]), bg="#FF5375", fg="#fff")
        self.label8.pack(pady=(10, 5))
        self.label8.configure(font=("Times", 12))

        # bio
        if data[11] == "":
            self.label9 = Label(self.root, text="About me:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label9 = Label(self.root, text="About me:  " + str(data[11]), bg="#FF5375", fg="#fff")
        self.label9.pack(pady=(10, 5))
        self.label9.configure(font=("Times", 12))

        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.prev = Button(self.root, text="Previous", font=30, bg="#fff", width=15, height=1,
                           command=lambda: self.show_proposals(row_no - 1))
        self.prev.pack(side=LEFT)

        self.next = Button(self.root, text="Next", font=30, bg="#fff", width=15, height=1,
                           command=lambda: self.show_proposals(row_no + 1))
        self.next.pack(side=RIGHT)




    def load_other_user_profile_gui(self,data,row_no):
        self.header_menu()

        # load dp
        imageUrl = "image/user.jpg"

        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        self.label5 = Label(self.root, text = data[1], bg="#FF5375", fg="#fff")
        self.label5.pack(pady=(10, 5))
        self.label5.configure(font=("Times", 12))

        # age
        if data[4] == 0:
            self.label6 = Label(self.root, text="Age:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label6 = Label(self.root, text="Age:  " + str(data[4]), bg="#FF5375", fg="#fff")
        self.label6.pack(pady=(10, 5))
        self.label6.configure(font=("Times", 12))

        # gender
        if data[5] == "":
            self.label7 = Label(self.root, text="Gender:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label7 = Label(self.root, text="Gender:  " + str(data[5]), bg="#FF5375", fg="#fff")
        self.label7.pack(pady=(10, 5))
        self.label7.configure(font=("Times", 12))

        # city
        if data[6] == "":
            self.label8 = Label(self.root, text="City:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label8 = Label(self.root, text="City:  " + str(data[6]), bg="#FF5375", fg="#fff")
        self.label8.pack(pady=(10, 5))
        self.label8.configure(font=("Times", 12))

        # bio
        if data[8] == "":
            self.label9 = Label(self.root, text="About me:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label9 = Label(self.root, text="About me:  " + str(data[8]), bg="#FF5375", fg="#fff")
        self.label9.pack(pady=(10, 5))
        self.label9.configure(font=("Times", 12))

        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.prev = Button(self.root, text="Previous", font=30, bg="#fff", width=15, height=1,command = lambda : self.view_profile(row_no - 1, "Prev"))
        self.prev.pack(side = LEFT)

        self.propose_btn = Button(self.root, text="Propose", font=30, bg="#fff", width=15, height=1,command = lambda :
self.propose(data[0]))
        self.propose_btn.pack(side=LEFT)

        self.next = Button(self.root, text="Next", font=30, bg="#fff", width=15, height=1, command = lambda : self.view_profile(row_no + 1,"Next"))
        self.next.pack(side=LEFT)
    def propose(self,juliet_id):
        romeo_id = self.user_data[0]
        response = self.db.add_proposal(romeo_id,juliet_id)

        if response == 1:
            messagebox.showinfo("Congrats!","Proposal sent successfully")
        elif response == 0:
            messagebox.showerror("Error!","Already proposed")
        else:
            messagebox.showerror("Error!","Some error occured")

    def change_dp(self):
        pathname = filedialog.askopenfilename(initialdir = "/images", title = "Something") # this code is used to open a dialog box from where we can select files

        #extract filename from path
        filename = pathname.split("/")[-1]
        destination = "D:\\Python\\Tinder\\image\\" + filename

        if filename.split(".")[-1] == 'jpg' or filename.split(".")[-1] == 'png':
            # update dp
            shutil.copyfile(pathname,destination)

        else:
            messagebox.showerror("Error!","Incorrect file format.Only jpg and png type is accepted")

    def load_user_profile_gui(self):

        self.header_menu()

        # load dp
        imageUrl = "image/user.jpg"

        load = Image.open(imageUrl)
        load = load.resize((200,200),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image = render)
        img.image = render
        img.pack()

        self.dp = Button(self.root, text="Change DP",command = lambda : self.change_dp())
        self.dp.pack(pady=(5, 5))

        self.label5 = Label(self.root, text="Hello " + self.user_data[1], bg="#FF5375", fg="#fff")
        self.label5.pack(pady=(10, 5))
        self.label5.configure(font=("Times", 12))

        # age
        if self.user_data[4] == 0:
            self.label6 = Label(self.root, text="Age:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label6 = Label(self.root, text="Age:  " + str(self.user_data[4]), bg="#FF5375", fg="#fff")
        self.label6.pack(pady=(10, 5))
        self.label6.configure(font=("Times", 12))

        # gender
        if self.user_data[5] == "":
            self.label7 = Label(self.root, text="Gender:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label7 = Label(self.root, text="Gender:  " + str(self.user_data[5]), bg="#FF5375", fg="#fff")
        self.label7.pack(pady=(10, 5))
        self.label7.configure(font=("Times", 12))

        # city
        if self.user_data[6] == "":
            self.label8 = Label(self.root, text="City:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label8 = Label(self.root, text="City:  " + str(self.user_data[6]), bg="#FF5375", fg="#fff")
        self.label8.pack(pady=(10, 5))
        self.label8.configure(font=("Times", 12))

        # bio
        if self.user_data[8] == "":
            self.label9 = Label(self.root, text="About me:  " + "Not Specified", bg="#FF5375", fg="#fff")

        else:
            self.label9 = Label(self.root, text="About me:  " + str(self.user_data[8]), bg="#FF5375", fg="#fff")
        self.label9.pack(pady=(10, 5))
        self.label9.configure(font=("Times", 12))

    def logout(self):
        # unset session data
        self.user_data = None
        # destroying user profile gui
        self.root.destroy()
        # loading the gui of login form
        self.load_gui_window(self.load_login_gui)
    def reg_validation(self):
        # fetch name,email and password provided by the user
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.db.register(name,email,password)

        if response:
            self.name_input.delete(0, 'end')
            self.email_input.delete(0, 'end')
            self.password_input.delete(0, 'end')
            messagebox.showinfo("Register Message","Registration Successful")
        else:
            messagebox.showerror("Register Message","Registration Failed")


    def login_validation(self):
        email = self.email_input.get()
        password = self.password_input.get()

        self.email_input.delete(0, 'end')
        self.password_input.delete(0, 'end')

        data = self.db.search(email,password)
        if len(data) == 1:
            messagebox.showinfo("Login Messsage","You have logged in successfully")
            # set session data
            print (data)
            self.user_data = data[0]
            # load the gui of user profile
            self.root.destroy()
            self.load_gui_window(self.load_user_profile_gui)
        else:
            messagebox.showerror("Login Message","Incorrect email/password ")






obj = Tinder()


