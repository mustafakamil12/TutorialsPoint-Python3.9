import sendgrid
import os
import xml.etree.ElementTree as ET
from sendgrid.helpers.mail import Mail, Email, To, Content


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


def sendEmail(apiKyeValue, from_address, to_address,url, default_header, subjectTxt, contentTxt):
    print(f"apiKyeValue: {apiKyeValue}")
    print(f"from_address: {from_address}")
    print(f"to_address: {to_address}")
    print(f"url: {url}")
    print(f"default_header: {default_header}")
    print(f"subject: {subjectTxt}")
    print(f"content: {contentTxt}")

    sg = sendgrid.SendGridAPIClient(api_key=apiKyeValue)
    from_email = Email(from_address)
    to_email = To(to_address)
    subject = subjectTxt
    content = Content("text/plain", contentTxt)
    mail = Mail(from_email, to_email, subject, content)
    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)

apiKey_value_arr = parseXML("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/server_config.xml")

url = 'https://api.sendgrid.com/v3/mail/send'
default_header = ""
sendEmail(apiKey_value_arr[0], "godric.phonex@gmail.com", "godric.phoenix@gmail.com",url, default_header, "Testing Email Using Sendgrid", "Hello Mustafa This is Testing Email Using sendgrid technique")
