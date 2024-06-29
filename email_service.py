import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
def send_email(user_details, bill_no, movie_title, showtime, num_tickets, total_amount):
    sender_email = "your_email@example.com"
    sender_password = "your_password_here"
    receiver_email = user_details['email']
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Booking Confirmation"
    body = f"""
    Booking Details
    Bill No: {bill_no}
    Movie: {movie_title}
    Showtime: {showtime}
    Number of Tickets: {num_tickets}
    Total Amount: ${total_amount:.2f}
    Booking Time: {datetime.now()}
    User Details:
    Name: {user_details['name']}
    Email: {user_details['email']}
    """
    message.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Booking details sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
