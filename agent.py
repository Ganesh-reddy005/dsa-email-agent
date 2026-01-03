from email_sender import send_mail
from llm_answer_genrator import generate_answer
from question_loader import get_random_questions
from dotenv import load_dotenv
from datetime import date
import os
load_dotenv()


JSON_PATH = "questions.json"

def run_agent():
    question = get_random_questions(JSON_PATH)

    llm_output = generate_answer(question)

    subject = f"DSA Question Of the DAY :({question['difficulty']} - {date.today().isoformat()})"
    body = "From GANESH REDDY's AI AGENT\n"+llm_output+"\nHOPE IT WAS USEFULL!!"

    send_mail(subject=subject,
              body=body,
              sender_acc=os.getenv('SENDER_MAIL'),
              app_password=os.getenv('APP_PASSWORD'),
              recp_acc=['b.ganesh.reddy.05@gmail.com',
                        'jeevaninn@gmail.com',
                        'gkmamarnath@gmail.com',
                        'karthikam3178@gmail.com']
    )
    

if __name__=='__main__':
    run_agent()