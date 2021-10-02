import sendgrid
import base64
import os,sys
import ftplib
import xml.etree.ElementTree as ET
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment, FileContent, FileName, FileType, Disposition


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    #print("tree = ", tree)

    # get root element
    root = tree.getroot()
    #print("root = ", root)

    # create empty list for news items
    apikeys = []

    # iterate news items
    for item in root.findall('./email/apikey'):
        #print(f"item = {item}")
        #print(f"item.text = {item.text}")
        # empty news dictionary
        apikeys.append(item.text)

    return apikeys

def sendEmail(apiKyeValue, from_address, to_address,url, default_header, subjectTxt, contentTxt, attach):
    print(f"apiKyeValue: {apiKyeValue}")
    print(f"from_address: {from_address}")
    print(f"to_address: {to_address}")
    print(f"url: {url}")
    print(f"default_header: {default_header}")
    print(f"subject: {subjectTxt}")
    print(f"content: {contentTxt}")

    filePath = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/testfile.txt'
    payLoad = ''

    if attach == 0:
        try:
            FILE1 = open(filePath,'r')
            for line in FILE1:
                payLoad += line
            FILE1.close()
        except OSError:
            sys.exit("Unable to find the target file...")

    elif attach == 1:
        try:
            FILE1 = open(filePath,'rb')
            payLoad = FILE1.read()
            FILE1.close()
        except OSError:
            sys.exit("Unable to find the target file...")



    if attach == 0:
        sg = sendgrid.SendGridAPIClient(api_key=apiKyeValue)
        from_email = Email(from_address)
        to_email = To(to_address)
        subject = subjectTxt
        content = Content("text/plain", contentTxt)
        mail = Mail(from_email, to_email, subject, payLoad)
        # Get a JSON-ready representation of the Mail object
        mail_json = mail.get()

        # Send an HTTP POST request to /mail/send
        response = sg.client.mail.send.post(request_body=mail_json)
        print(response.status_code)
        print(response.headers)

    elif attach == 1:
        sg = sendgrid.SendGridAPIClient(api_key=apiKyeValue)
        from_email = Email(from_address)
        to_email = To(to_address)
        subject = subjectTxt
        #content = Content("text/plain", contentTxt)
        html_content = '<strong>and easy to do anywhere, even with Python</strong>'
        mail = Mail(from_email, to_email, subject, html_content)
        # Get a JSON-ready representation of the Mail object
        encoded_file = base64.b64encode(payLoad).decode()
        print(f"encoded_file = {encoded_file}")
        attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('testfile.txt'),
        FileType('application/txt'),
        Disposition('attachment')
        )
        mail.attachment = attachedFile

        response = sg.send(mail)
        print(response.status_code, response.body, response.headers)

def ftpUploader():
    session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
    file = open('kitten.jpg','rb')                  # file to send
    session.storbinary('STOR kitten.jpg', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
#--------------------- Main -------------------
apiKey_value_arr = parseXML("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/server_config.xml")

url = 'https://api.sendgrid.com/v3/mail/send'
default_header = ""
attach = 1
sendEmail(apiKey_value_arr[0], "godric.phonex@gmail.com", "godric.phoenix@gmail.com",url, default_header, "Testing Email Using Sendgrid", "Hello Mustafa This is Testing Email Using sendgrid technique", attach)
