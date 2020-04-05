#!Python3

def find_plate(img=None):

  import plate_segment, pandas as pd, shutil, os
  # "img" is the full path along with the image name can be supplied to the license plate extractor to find the llicense plate number from the new file, default is "carz.jpg"
  if img== None:
    plate=123456
  else:
    plate= plate_segment.license_plate_extractor()
    #plate=123456

    print("Plate we got was :  "+ plate)
    """
  A function call to find the plate number's
  owner and other details, returning a dictionary 
  of the details

  """
  #Make sure the plate number is numeric and not string
  df = pd.read_csv("/home/rahul/Project/rto.csv")
  row = df[df['Plate_Num']==plate]
  
  if len(row)==1:
    #if the plate was found in the rto 
    name = row['Name'].to_string()[1:].strip()
    email = row['Email'].to_string()[1:].strip()
    phone = row['Phone'].to_string()[1:].strip()
    print("Sending Fine Letter to: "+email)
    #send_mail(reciever=email,plate=plate,owner=name)

    #if default image was not used move it to the caught folder
    if img!=None:
      shutil.copy(img+".png", "/home/rahul/Project/caught")
      os.remove(img+".png")
      shutil.copy(img+"_orig.png", "/home/rahul/Project/caught")
      os.remove(img+"_orig.png")

  elif img !=None:
    #if the plate was not found in the rto csv
    shutil.copy(img+".png", "/home/rahul/Project/not_found")
    os.remove(img+".png") 
    shutil.copy(img+"_orig.png", "/home/rahul/Project/not_found")
    os.remove(img+"_orig.png")


    
def send_mail(reciever="rrkrp100@gmail.com",plate= "JH-09-6669",place= "Chandrapura",owner="B.Pandey"):

    """
    Uses SMTP_SSL() for encryption instead of
     normal smtplib to send mails via gmail
    """
    import smtplib, ssl, datetime

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "rahulpndy7@gmail.com"  # Enter your address
    receiver_email = reciever  # Enter receiver address
    password = "Roxa@&1234"
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
    except Exception as ex:
        print(ex)
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
