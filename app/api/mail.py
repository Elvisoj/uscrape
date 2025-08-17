import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
# Gmail setup
EMAIL = "eojtestingm@gmail.com"
APP_PASSWORD = "qraw aysx ylpv rvzz"
TO_EMAIL = "ighoelvis8@gmail.com"


def send_email(content):
    """Function to send an email with the scraped content."""

    try:
        # Create the email content
        subject = f"Today's Scraped Post - {datetime.now().strftime('%Y-%m-%d')}"
        body = content

        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = TO_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, APP_PASSWORD)
            server.sendmail(EMAIL, TO_EMAIL, msg.as_string())

        print("✅ Email sent successfully!")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")