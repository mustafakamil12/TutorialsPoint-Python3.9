import sendgrid
import base64
from base64 import decodebytes
import os,sys
import ftplib
from ftplib import FTP
import pysftp
import paramiko
import xml.etree.ElementTree as ET
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content, Attachment, FileContent, FileName, FileType, Disposition

class My_Connection(pysftp.Connection):
    def __init__(self, *args, **kwargs):
        try:
            if kwargs.get('cnopts') is None:
                kwargs['cnopts'] = pysftp.CnOpts()
        except pysftp.HostKeysException as e:
            self._init_error = True
            raise paramiko.ssh_exception.SSHException(str(e))
        else:
            self._init_error = False

        self._sftp_live = False
        self._transport = None
        super().__init__(*args, **kwargs)

    def __del__(self):
        if not self._init_error:
            self.close()

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
    with FTP('134.209.65.211', 'ftpuser', 'Pit5cxcy') as ftp:
            # For text or binary file, always use `rb`
            #ftp.cwd('/ftp/upload')
            with open('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/mustafa.txt', 'rb') as text_file:
                ftp.storlines('STOR mustafa.txt', text_file)
                print("file had been uploaded")
            with open('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/kitten.jpg', 'rb') as image_file:
                ftp.storbinary('STOR kitten.jpg', image_file)
                print("file had been uploaded")

def sftpUploader():
    filePath = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/mustafa.txt'    #hard-coded
    path = '/var/sftp/files/'

    hostN = "134.209.65.211"             #hard-coded
    #portN = 4444
    username = "sftpuser"                #hard-coded
    password = "Pit5cxcy"                #hard-coded

    #keydata = b"""AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBB2m3Ux60uf1ENhdujLVoCv93TNHXryz8TPTpLGEvzL0oKSITZgSdLHgFe5WXvtlUhk4siIMBCKcuIQXBaMpdfA="""

    # LOAD THE ECDSA KEY
    #key = paramiko.AgentKey('ecdsa-sha2-nistp256', decodebytes(keydata))

    # SET OPTS
    #cnopts = pysftp.CnOpts()
    # ADD OUR KEY TO OPTS
    #cnopts.hostkeys.add(hostN, 'ecdsa-sha2-nistp256', key)
    # CONNECT

    with pysftp.Connection(host=hostN,username=username,password=password) as sftp:
        print("Connected!")
        #sftp.put(filePath, path)
        with sftp.cd('/files'):           # temporarily chdir to allcode
            sftp.put('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/mustafa.txt')  	# upload file to allcode/pycode on remote
            #sftp.get('remote_file')         # get a remote file

            print("Upload done.")
#--------------------- Main -------------------
apiKey_value_arr = parseXML("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/server_config.xml")

url = 'https://api.sendgrid.com/v3/mail/send'
default_header = ""
attach = 1
#sendEmail(apiKey_value_arr[0], "godric.phonex@gmail.com", "godric.phoenix@gmail.com",url, default_header, "Testing Email Using Sendgrid", "Hello Mustafa This is Testing Email Using sendgrid technique", attach)
#sftpUploader()

ftpUploader()
