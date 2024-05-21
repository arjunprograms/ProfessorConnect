import smtplib
import ssl
import schedule
import time
from datetime import datetime

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "arjun.subedischool@gmail.com"
sender_password = 

# Email content
subject = "Staying Connected: Fostering Student-Professor Relationships"
body = """Dear Professor,

Hope this email finds you well! As a dedicated student, I believe in nurturing strong connections with my professors, which can greatly benefit both academic and professional growth. I wanted to take a moment to express my gratitude for your guidance and mentorship throughout this journey. Your expertise and insights have been invaluable in shaping my educational path.

Additionally, I would like to explore opportunities for further collaboration or assistance you might need. Whether it's research projects, teaching assistantships, or any other academic endeavors, I am eager to contribute and learn from your experience.

Please feel free to reach out to me if you have any upcoming opportunities or if you would like to discuss potential areas of cooperation. I am always excited to expand my knowledge and skills under your guidance.

Thank you for your time and consideration. I look forward to hearing from you.

Best regards,
Arjun Subedi
"""

recipients = ["kniu@fullerton.edu", "zibragimov@fullerton.edu", "zharris@fullerton.edu", "mnargesi@fullerton.edu", "dpatel@fullerton.edu", "pvemula@fullerton.edu"]

# Function to send email
def send_email():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(sender_email, sender_password)
        for recipient in recipients:
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient, message)
        print(f"Emails sent successfully at {datetime.now()}")

# Schedule the task to run every 3 months
schedule.every(3).months.do(send_email)

# Run the scheduled task
while True:
    schedule.run_pending()
    time.sleep(1)