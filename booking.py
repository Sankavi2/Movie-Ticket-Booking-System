from datetime import datetime
from email_service import send_email
def book_ticket(cursor, db, movie, showtime, num_tickets, ticket_price=100, user_details=None):
    subtotal = num_tickets * ticket_price
    gst = subtotal * 0.05  # 5% GST
    total_amount = subtotal + gst
    user_details_str = f"Name: {user_details['name']}, Email: {user_details['email']}"
    cursor.execute(
        "INSERT INTO bookings (movie_title, showtime, num_tickets, total_amount, booking_time, user_details) VALUES (%s, %s, %s, %s, %s, %s)",
        (movie.title, showtime, num_tickets, total_amount, datetime.now(), user_details_str)
    )
    db.commit()
    bill_no = cursor.lastrowid 
    print(f"{num_tickets} tickets booked for {movie.title} at {showtime}. Total amount: ${total_amount:.2f}. Bill No: {bill_no}")
    with open(f"{user_details['email']}_booking_details.txt", "w") as file:
        file.write(f"Booking Details\n")
        file.write(f"Bill No: {bill_no}\n")
        file.write(f"Movie: {movie.title}\n")
        file.write(f"Showtime: {showtime}\n")
        file.write(f"Number of Tickets: {num_tickets}\n")
        file.write(f"Subtotal: ${subtotal:.2f}\n")
        file.write(f"GST (5%): ${gst:.2f}\n")
        file.write(f"Total Amount: ${total_amount:.2f}\n")
        file.write(f"Booking Time: {datetime.now()}\n")
        file.write(f"User Details\n")
        for key, value in user_details.items():
            file.write(f"{key}: {value}\n")
    send_email(user_details, bill_no, movie.title, showtime, num_tickets, total_amount)
