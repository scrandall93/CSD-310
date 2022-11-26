#Sam Crandall; Module7.2Assignment; November 26th, 2022

#code is written to find information from a MySQL database with 
#a Python script. 

#importing mysqlconnector to connect to Movies db.
	#importing error code to handle errors.
import mysql.connector
from mysql.connector import errorcode

#logging into database Movies (I always feel strange about
	#including password here so please let me know if I 
	#need to be including that instead of using placeholders.) 
config = {
	"user": "root",
	"password": "*********", #change to user PW
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}
#database connection success message + SQL queries to be ran on Movies. 
try:
	
	db = mysql.connector.connect(**config) #calling connect function from mysql.connector to connect to movies DB
	
	print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"])) #print confirmation of connection to db

	print("") #printing blank line to clean up results
	
	cursor = db.cursor() #calling the cursor object

	cursor.execute("SELECT studio_id, studio_name FROM studio;") #using cursor.execute() function to execute query

	studio = cursor.fetchall() #using the cursor.fetchall() function to pull all records existing in studio db for query to pull from
	
	print("-- DISPLAYING Studio RECORDS --") #printing header for results

	for studio in studio: #using for loop to print results from query above
		
		print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))
		
	print("") #printing blank line to clean up results
	
	cursor = db.cursor() #calling the cursor object

	cursor.execute("SELECT genre_id, genre_name FROM genre;") #using cursor.execute() function to execute query

	genre = cursor.fetchall() #using the cursor.fetchall() function to pull all records existing in genre db for query to pull from
	
	print("-- DISPLAYING Genre RECORDS --") #printing header for results

	for genre in genre: #using for loop to print results from query above
		
		print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))
		
	print("") #printing blank line to clean up results
	
	cursor = db.cursor() #calling the cursor object

	cursor.execute("SELECT film_name, film_runtime FROM film where film_runtime < 120;") #using cursor.execute() function to execute query

	film = cursor.fetchall() #using the cursor.fetchall() function to pull all records existing in film db for query to pull from
	
	print("-- DISPLAYING Short Film RECORDS --") #printing header for results

	for film in film: #using for loop to print results from query above
		
		print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))
		
	print("") #printing blank line to clean up results
	
	cursor = db.cursor() #calling the cursor object

	cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;") #using cursor.execute() function to execute query

	film = cursor.fetchall() #using the cursor.fetchall() function to pull all records existing in film db for query to pull from
	
	print("-- DISPLAYING Director RECORDS in Order --") #printing header for results

	for film in film: #using for loop to print results from query above
		
		print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))
	

#except to handle any errors in logging in		
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print(" The supplied username or password are invalid.")
		
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print(" The specified database does not exist.")
		
	else:
		print(err)

#closing out the DB once results are given. 		
finally:
	db.close()
