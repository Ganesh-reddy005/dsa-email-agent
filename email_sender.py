import smtplib
from email.mime.text import MIMEText #plain text
from email.mime.multipart import MIMEMultipart #html
from typing import Optional #type hinting

import os
from dotenv import load_dotenv
load_dotenv()
mail_acc=os.getenv('SENDER_MAIL')
password=os.getenv('APP_PASSWORD')

def send_mail(subject:str, body:str, sender_acc:str, app_password:str,
              recp_acc:Optional[str] = None)->None:
    if recp_acc==None:
        recp_acc = sender_acc
    #creating Multipart message allows Plain text or HTML
    msg=MIMEMultipart()
    msg['From'] = sender_acc
    if isinstance(recp_acc, list):
        msg["To"] = ", ".join(recp_acc)
    else:
        msg["To"] = recp_acc
    msg['Subject'] = subject
    #attaching  - plain text body
    msg.attach(MIMEText(body,'plain'))

    #coonection
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo() #identifies itself
        #connection encryption
        server.starttls()
        server.ehlo()

        #logging in with our details
        if mail_acc and password:
            server.login(mail_acc,password)
            server.send_message(msg)
            print('Sent Successfully!')
        else:
            print('no details found!')
    except Exception as e:
        print("Failed to send email. Error:")
        print(e)

    finally:
        try:
            server.quit()
        except:
            pass


if __name__=='__main__':
    recpt_mail='b.ganesh.reddy.05@gmail.com'
    sender_acc=mail_acc
    app_password=password

    subject = 'DSA question of the day'
    body = (
        "Hello!\n\n"
        "This is a test email from your DSA agent. If you can read this, the SMTP "
        "sending works.\n\n"
        "— Your friendly Gmail agent"
     )
    send_mail(subject=subject,body=body,sender_acc=sender_acc,app_password=app_password,
              recp_acc=recpt_mail)
