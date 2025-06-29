import smtplib

# Start TLS encryption
s = smtplib.SMTP("smtp.gmail.com", 587)

# Enable TLS encryption
s.starttls()

# Login to the email account
s.login("tempaminf3@gmail.com", "password_here")

# Send email
s.sendmail(
    "tempaminf3@gmail.com",
    "helloamin.com@gmail.com",
    "Subject: Test Email\n\nThis is a test email.",
)

# Close the connection
s.quit()

print("Email sent successfully.")
