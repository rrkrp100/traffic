#!Python3



def send_mail(reciever, plate, place, owner):
    """
    Uses SMTP_SSL() for encryption instead of
     normal smtplib to send mails via gmail
    """
    import smtplib, ssl, datetime

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "rahulpndy7@gmail.com"  # Enter your address
    receiver_email = reciever  # Enter receiver address
    password = "Rahul1pandey"
    date=datetime.datetime.now().strftime("%y-%m-%d at %H-%M")

    message = """\
    Traffic Police India


    Subject: Traffic Light violation bill


    Greetings.
    You have been charged for running a red light on %s around %s
    Plate number : %s, owner of the vehicle %s, is required to come to the police station to pay the fine.

    Thank You
    Signed
    Rahul"""%(date,place,plate,owner)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        print("Hmm... Seems your internet connection is down -_-")



# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)



def send_sms(plate,place,phone):

    import requests
    import json, datetime

    URL='http://www.way2sms.com/api/v1/sendCampaign'

    date=datetime.datetime.now().strftime("%y-%m-%d at %H-%M")

    body="You have been charged for running a red light on %s around %s\nPlate number : %s"%(date,place,plate)

    response = sendPostRequest(URL, '16AXRL1ZLVO2TE84KMZFL3ABBFVIO3QA', 'GL3EK8371Q398L3T', 'stage', phone, 'Rahul', body )
    # print response if you want
    print (response.text)


if __name__ == "__main__":

    import requests
    import json, datetime
    send_mail("rrkrp100@gmail.com", "JH-09-6669", "Chandrapura", "B.Pandey")
    #send_sms("JH-09-6669", "Chandrapura",'9631507694')
