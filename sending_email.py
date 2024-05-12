import smtplib
import ssl

def send_email(email_address: str, message: str):
    user = "mahdimeyghani02@gmail.com"
    password = "exit sttz mqbo lfni"

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    email_sender = email_address
    email_receiver = "mahdimeyghani02@gmail.com"

    subject = "Portfolio Website"

    body = message

    email_message = f"subject: {subject}\n\nFrom: {email_sender}\n{body}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, email_receiver, email_message)


if __name__ == "__main__":
    send_email("boochip02@gmail.com", "Hello\nHows everything?\nIs everything ok?")
