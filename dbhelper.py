#install mysql.connector

import mysql.connector
#satrt Apache and Mysql
#browser->localhost/phpmyadmin
#->Database server
#->>A computer with all the databases
#create a db

#C->create
#R->retrieve
#U->update
#D->delete


#logic related to database

#connect to database-
import sys
class DB_helper:
	def __init__(self):

		try:
			self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="db-1") #->RHS retuurns a connector object with all the login details
			self.mycursor=self.conn.cursor()
		except:
			print("Some ERROR occured. Could not connect to database.")
			sys.exit(0)
		else:
			print("Connected to Database.")

	def register(self,name,email,password):
		#code for actual registration in the database
		    """
		    here, we need to check that the email being entered does not currently exists in the database, 
		    if it does, we simply need to return -1 saying that 'email already exists, registration failed'
		    If the email eneterd at this step does not exist already, then only we will insert a new user.
		    """
			
		try:
			self.mycursor.execute("""
				INSERT INTO `users`(`id`, `name`, `email`, `password`) VALUES (NULL,'{}','{}','{}');
				""".format(name,email,password))
			self.conn.commit() #two-way process to register a user in your database
		except:
			return -1
		else:
			return 1

	def search(self,email,password):
		self.mycursor.execute("""
			SELECT * FROM users WHERE email LIKE '{}'AND password LIKE '{}'
			""".format(email,password))

		data=self.mycursor.fetchall()

		return (data)
