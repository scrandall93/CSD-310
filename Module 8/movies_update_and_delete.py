#Sam Crandall; Module 8.2 Assignment; November 26th, 2022
#code is written to show db pre and post data changes

#importing mysqlconnector to connect to Movies db.
	#importing error code to handle errors.
import mysql.connector

#logging into database Movies (I always feel strange about
	#including password here so please let me know if I 
	#need to be including that instead of using placeholders.) 
config = {
	"user": "root",
	"password": "*********", #change to user PW
	"host": "127.0.0.1",
	"database": "movies"
}

try:
	db = mysql.connector.connect(**config) #calling connect function from mysql.connector to connect to movies DB
	cursor = db.cursor()
	print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"])) #print confirmation of connection to db
	print("") #printing blank line to clean up results

#except to handle any errors in logging in		
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print(" The supplied username or password are invalid.")	
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print(" The specified database does not exist.")	
	else:
		print(err)

def show_films(cursor, title):
	#method to execute an inner join on all tables and 
	#iterate over the dataset and output the results to the
	#terminal window. 
	
	#inner join query
	cursor.execute("Select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film inner join genre on film.genre_id = genre.genre_id inner join studio on film.studio_id = studio.studio_id;")
		
	#get the results from the cursor object
	films = cursor.fetchall()
	
	print("\n -- {} --".format(title))
	
	#iterate over the film data set and display the results
	for film in films:
		print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")

def show_films2(cursor, title):
	#query to insert Halloween into film table
	sql = "INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	val = ("4", "Halloween", "2018", "106", "David Gordon Green", "2", "1")
	
	#executing query
	cursor.execute(sql, val)
	
	#commiting changes from query
	db.commit()
	
	#querying to find current values in tables with changes included
	cursor.execute("Select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film inner join genre on film.genre_id = genre.genre_id inner join studio on film.studio_id = studio.studio_id;")

	#get the results from the cursor object
	films = cursor.fetchall()
		
	print("\n -- {} --".format(title))
		
	#iterate over the film data set and display the results
	for film in films:
		print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))
		
show_films2(cursor, "DISPLAYING FILMS AFTER INSERT")

def show_films3(cursor, title):
	#query to update the genre of Aliens to horror
	sql = "UPDATE film SET genre_id = '1' where film_id = '2'"
	
	#executing query
	cursor.execute(sql)
	
	#commiting changes from query
	db.commit()
	
	#querying to find current values in tables with changes included
	cursor.execute("Select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film inner join genre on film.genre_id = genre.genre_id inner join studio on film.studio_id = studio.studio_id;")

	#get the results from the cursor object
	films = cursor.fetchall()
		
	print("\n -- {} --".format(title))
		
	#iterate over the film data set and display the results
	for film in films:
		print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))
		
show_films3(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Aliens to Horror")

def show_films4(cursor, title):
	#query to delete Gladiator for film table
	sql = "DELETE FROM film where film_name = 'Gladiator'"
	
	#executing query
	cursor.execute(sql)
	
	#commiting changes from query
	db.commit()
	
	#querying to find current values in tables with changes included
	cursor.execute("Select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film inner join genre on film.genre_id = genre.genre_id inner join studio on film.studio_id = studio.studio_id;")

	#get the results from the cursor object
	films = cursor.fetchall()
		
	print("\n -- {} --".format(title))
		
	#iterate over the film data set and display the results
	for film in films:
		print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))
		
show_films4(cursor, "DISPLAYING FILMS AFTER DELETE")
