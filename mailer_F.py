import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "ddb4tt@gmail.com"
email_list = ["debabratar421@gmail.com"]
password = "cebilytdqunogsee"

message = "Unknown person detected"
subject = "Unknown person image"

# imagesimple_email_context = ssl.create_default_context()
#
# try:
#     print("connecting to server")
#     TIE_server = smtplib.SMTP(smtp_server, smtp_port)
#     TIE_server.starttls(context=simple_email_context)
#     TIE_server.login(email_from, password)
#     print("connected to server")
#
#     TIE_server.sendmail(email_from, email_to, message)
#
# except Exception as e:
#     print(e)
#
# finally:
#     TIE_server.quit()

def send_email():
    for person in email_list:

        body = f"""
        Unkown person detected
    """
        msg = MIMEMultipart()
        msg["From"] = email_from
        msg["To"] = person
        msg["Subject"] = subject

        msg.attach(MIMEText(body, 'plain'))
        filename = "unknown.jpg"

        attachment = open(filename, 'rb')

        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', 'attachment; filename= '+ filename)
        msg.attach(attachment_package)

        text = msg.as_string()

        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, password)
        print("connected to server")

        print("sending email")
        TIE_server.sendmail(email_from, person, text)
        print("email sent to", person)

    TIE_server.quit()


