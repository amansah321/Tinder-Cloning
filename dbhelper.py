import mysql.connector

class DBHelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="tinder")
            self.mycursor = self.conn.cursor()
        except:
            print("Database error!")
        else:
            print("Connected to Database!!!")

    def search(self,email,password):
        self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))
        data = self.mycursor.fetchall()

        return data


    def register (self,name,email,password):
        try:
            self.mycursor.execute("INSERT INTO users VALUES(NULL,'{}','{}','{}')".format(name,email,password))
            self.conn.commit()  #whenever we want any permanent changes in our database then we write this statement
        except:
            return -1  # it means registration is not done
        else:
            return 1   # it means registration is not done

    def fetch_user(self,row_no):
        self.mycursor.execute("SELECT * FROM users LIMIT {},1".format(row_no-1))
        data = self.mycursor.fetchall()
        return data
    def count_users(self):
        self.mycursor.execute("SELECT COUNT(*) FROM users") # this will count no. of rows
        data = self .mycursor.fetchall()
        return data

    def add_proposal(self,romeo_id,juliet_id):
        # check whether tihs romeo has already proposed this juliet
        self.mycursor.execute("SELECT * FROM proposals WHERE romeo_id = {} AND juliet_id = {}".format(romeo_id,juliet_id))
        data = self.mycursor.fetchall()

        if len(data) > 0:
            return 0 #this means this romeo has already proposed this juliet
        try:
            self.mycursor.execute("INSERT INTO proposals VALUES (NULL,{},{})".format(romeo_id,juliet_id))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
    def fetch_one_proposal(self,romeo_id,row_no):
        self.mycursor.execute("SELECT * FROM proposals JOIN users ON proposals.juliet_id = users.id WHERE proposals.romeo_id = {} LIMIT {},1".format(romeo_id,row_no - 1))
        data = self.mycursor.fetchall()
        return data

    def fetch_one_request(self,juliet_id,row_no):
        self.mycursor.execute("SELECT * FROM proposals JOIN users ON proposals.romeo_id = users.id WHERE proposals.juliet_id = {} LIMIT {},1".format(juliet_id,row_no - 1))
        data = self.mycursor.fetchall()
        return data

    def fetch_one_match(self,user_id,row_no):
        self.mycursor.execute( "SELECT * FROM proposals p JOIN users u ON p.juliet_id = u.id WHERE p.juliet_id IN (SELECT p.romeo_id FROM proposals p WHERE p.juliet_id = {}) AND p.romeo_id = {} LIMIT {},1".format(user_id,user_id, row_no - 1))
        data = self.mycursor.fetchall()
        return data

    def edit_user_profile(self,user_id,password,city,about):
        try:
            self.mycursor.execute("UPDATE users SET password = '{}', city = '{}', bio = '{}' WHERE id = {}".format(password,city,about,user_id))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

