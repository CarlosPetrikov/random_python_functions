from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

# Function to send emails via a Gmail SMTP server 
def send_mail(credentials, to_address, title, message, img_path=None):
    control = False
    while control == False:
        try:
            msg = MIMEMultipart()
            msg['From'] = credentials[0]
            msg['To'] = to_address
            msg['Subject'] = title
            text = MIMEText(message)
            msg.attach(text)
            
            if  img_path != None:
                img_data = open(img_path, 'rb').read()
                
                if '/' in img_path:
                    img_name = img_path.replace(" ", '').split('/')
                else:
                    img_name = img_path.replace(" ", '').split("\\")
                img_name = img_name[-1]
                
                image = MIMEImage(img_data, filename=img_name)
                msg.attach(image)
                
            server = smtplib.SMTP_SSL('smtp.gmail.com: 465')
            server.login(msg['From'], credentials[1])
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            control = True
                   
        except ConnectionError:
            continue
        
#Example:

credentials = ('mail@mail.com', 'SuperPassword@123')

to_address = 'somebody_once_told_me@outlook.com'
title = "Hey now, you're an all-star!"
message = '''
Hey now, you're an all-star, get your game on, go play
Hey now, you're a rock star, get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
'''
img_path = r'C:\Users\user\TOP_SONGS\all_star.png'

send_mail(credentials, to_address, title, message, img_path)