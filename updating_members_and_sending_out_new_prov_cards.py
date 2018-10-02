


###imports
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
import re
import yaml
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table
from reportlab.lib.colors import HexColor, PCMYKColor, PCMYKColorSep, Color, black, blue, red

import pickle



# In[46]:

exec(compile(open('Cleaning_xml.py').read(), 'Cleaning_xml_only.py', 'exec'))


def sending_prov_cards(members):



    ###loading the old members user_id

    with open('old_user_id.pkl', 'rb') as f:
        old_user_id = pickle.load(f)
    old_user_id = [str(x) for x in old_user_id]
    new_cards = [x for x in members['user_id'] if x not in old_user_id]

    if len(new_cards) == 0:
        print('No need to print out')
    else:

        members_cards = members[members['user_id'].isin(new_cards)]
        members_cards['full_name'] = members_cards['first_name'] + '_' + members_cards['last_name']



        for index, row in members_cards.iterrows():

            full_name = row['full_name']
            number = str(row['numbers'])
            email = row['user_email']



            canvas = Canvas('./cards/' + full_name + '.pdf')
            canvas.drawImage('image_to_use_as_background.png', 100,450, width=400, height=125)
            #user_in = input()

            canvas.drawString(225, 725, 'SOCCER FAN CLUB last_name',charSpace=1)
            canvas.setStrokeColor(black, alpha=1)
            canvas.drawString(240, 710, 'PROVISIONAL ID 2018-19')
            canvas.setFont('Helvetica', 8)
            canvas.setFillColor(black)
            canvas.drawString(350, 503, full_name.title())
            canvas.drawString(370, 493, number)
            canvas.drawString(370, 482, '1495')

            canvas.showPage()



            canvas.save()



            fromaddr = "no.reply.account@from_where_is_sent.com"
            toaddr = row['user_email']





            msg = MIMEMultipart()

            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Updated Provisional ID"

            body = """members_cards!

    Bla bla bla"""


            msg.attach(MIMEText(body, 'plain'))

            filename = './cards/' + full_name + '.pdf'
            attachment = open('./cards/' + full_name + '.pdf', "rb")

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587) #587
            server.ehlo()
            server.starttls()
            server.login(fromaddr, "divendres4")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

    with open('old_user_id.pkl', 'wb') as picklefile:
        pickle.dump(members['user_id'], picklefile)


    print('DONE')




sending_prov_cards(members)
