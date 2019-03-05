#!Python3

def send_mail(reciever, plate, place, owner):
    """Sends the charges to the offender"""

    import webbrowser, datetime
    """from  urllib import quote #used in Python2 : webbrowser.open("mailto:%s?subject=%s&body=%s"%(sender, quote(subject),quote(body)))"""

    sender = "rahulpndy7@gmail.com"
    date=datetime.datetime.now().strftime("%y-%m-%d at %H-%M")

    subject = "Traffic Light violation bill"
    body  = "Greetings.\n\nYou have been charged for running a red light on %s around %s\nPlate number : %s, owner of the vehicle %s,is required to come to the police station to pay the fine.\n\n Thank You \n Signed\n Rahul\n " %(date,place,plate,owner)

    webbrowser.open("mailto:%s?subject=%s&body=%s"%(sender, subject, body))





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
