import mysql.connector
from movie import Movie 
from theater import Theater 
from booking import book_ticket
def fetch_movies(cursor):
    cursor.execute("SELECT title, genre, rating, showtimes FROM movies")
    result = cursor.fetchall()
    return [Movie(title, genre, rating, showtimes.split(',')) for title, genre, rating, showtimes in result]
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="movie_booking"
)
cursor = db.cursor()
theater = Theater("AYYA THEATER", "123 Main St")
movies = fetch_movies(cursor)
for movie in movies:
    theater.add_movie(movie)
while True:
    theater.show_movies()
    movie_choice = int(input("Enter the number of the movie you want to see: ")) 
    if 0 <= movie_choice < len(theater.movies):
        selected_movie = theater.movies[movie_choice]
        print(f"Showtimes for {selected_movie.title}:")
        for idx, showtime in enumerate(selected_movie.showtimes, start=1):
            print(f"{idx}. {showtime}")
        showtime_choice = int(input("Enter the number of the showtime you want: ")) 
        if 0 <= showtime_choice < len(selected_movie.showtimes):
            selected_showtime = selected_movie.showtimes[showtime_choice]
            num_tickets = int(input("Enter the number of tickets: "))
            user_details = {
                'name': input("Enter your name: "),
                'email': input("Enter your email: ")
            }
            book_ticket(cursor, db, selected_movie, selected_showtime, num_tickets, user_details=user_details)
        else:
            print("Invalid showtime selection.")
    else:
        print("Invalid movie selection.")
    more_booking = input("Do you want to book another ticket? (yes/no): ").strip().lower()
    if more_booking != 'yes':
        break

print("Thank you for using the ticket booking system!")
