import requests
import json
import datetime
import smtplib
import uuid
from faker import Faker
import time
import random
import os
import sys

sys.stdout.flush()


faker = Faker()

headers = {
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/90.0.4430.93 Safari/537.36"
         }
def crawl_cowin(pin_code_list,date):
    ip_addr = faker.ipv4()
    headers["X-Forwarded-For"] = ip_addr
    if date is None:
        date = datetime.datetime.now().strftime("%d-%m-%Y")
    for pin_code in pin_code_list:
        response = requests.get(
            "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pin_code
            +"&date="+date+"&random="+uuid.uuid4().__str__(),
            verify=False, headers=headers)
        try:
            resp_obj = json.loads(response.content)
            center_list = resp_obj["centers"]
            for center in center_list:
                session_list = center["sessions"]
                for session in session_list:
                    available_capacity = session['available_capacity']
                    min_age_limit = session["min_age_limit"]
                    if available_capacity > 0 and min_age_limit == 18:
                        print("Pincode:"+pin_code+" Available capacity :"+str(available_capacity),flush=True)
                        send_email(pincode=pin_code+",capacity = "+str(available_capacity))
        except Exception as exp:
            print("Exception is "+str(exp),flush=True)
            time.sleep(random.randint(1, 20))


gmail_user = "xxxxxxx@gmail.com"
gmail_password = "xxxxx"
to = "xxxxxx@gmail.com"
SEND_EMAIL = False
def send_email(pincode):
    if SEND_EMAIL:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user,to , pincode)
        server.close()
    os.system("open siren.wav")
    sys.exit(0)


i = 0
pin_codes = ["411044","411018","411027","411035","411033","411017","411026"]
while True:
    print("Iteration count :"+str(i), flush=True)
    crawl_cowin(pin_codes,date=None)
    time.sleep(random.randint(10,30))
    i+=1