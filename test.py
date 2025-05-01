import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP credentials from Brevo
smtp_server = "smtp-relay.brevo.com"
smtp_port = 587
smtp_username = "abdulhadi@sodeom.com"  # Replace with your Brevo account email
smtp_password = "0d5hLWqkUMXNQAaR"  # Replace with your SMTP key

# Email content
subject = "My Subject"
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Your IP Information</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin-top: 50px;
      background-color: #f9f9f9;
    }
    #ip {
      font-size: 1.5em;
      margin-bottom: 20px;
    }
    #removeBtn {
      padding: 10px 20px;
      font-size: 1em;
      cursor: pointer;
    }
    #message {
      margin-top: 30px;
      font-size: 1.2em;
      color: #333;
      display: none;
    }
  </style>
</head>
<body>

  <div id="ip">Your public IP is: <strong>192.0.2.1</strong></div>
  <button id="removeBtn">Remove the IP</button>
  <div id="message">Your IP has been sent to the server.</div>

  <script>
    document.getElementById('removeBtn').addEventListener('click', function() {
      document.getElementById('message').style.display = 'block';
    });
  </script>

</body>
</html>

"""
sender_email = smtp_username

# Recipients
recipients = ["campanyone@gmail.com", "companytwo@gmail.com"]

# Send email to each recipient
for recipient in recipients:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{sender_email} <{sender_email}>"
    msg["To"] = recipient

    # Add HTML content
    mime_text = MIMEText(html_content, "html")
    msg.attach(mime_text)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")