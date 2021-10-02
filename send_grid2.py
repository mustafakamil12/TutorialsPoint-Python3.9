import os
import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)


message = Mail(
    from_email='godric.phoenix@gmail.com',
    to_emails='godric.phoenix@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>'
)

with open('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/Estancia.pdf', 'rb') as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('Estancia.pdf'),
    FileType('application/pdf'),
    Disposition('attachment')
)
message.attachment = attachedFile

sg = SendGridAPIClient('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')
response = sg.send(message)
print(response.status_code, response.body, response.headers)
