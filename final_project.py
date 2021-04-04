import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv


csvdata = []
with open('receiver_list.txt', 'r') as file:  #membuka file receiver_list.txt file ini bisa ganti namanya sesuai kebutuan juga bisa diganti dengan file extention csv
    reader = csv.reader(file)  #ini untuk membaca file text
    for row in reader:  #iterasi melalui semua baris di file text
        csvdata.append(
            row #Menambahkan email ke array . tambahnkan seluruh baris ke array
        )  #Tambahkan elemen kedua dari setiap baris kolom email ke daftar email
    csvdata.pop(0)


def sender(
        recipient, name_to_display, from_email, password, body, subj
):  #membuat fungsi untuk mengirim email. 
    msg = MIMEMultipart()

    msg['Subject'] = subj
    msg['From'] = f'{name_to_display} <{from_email}>'
    msg['To'] = recipient

    msg.attach(MIMEText(body, 'plain'))
    
    # Lampiran, sesuaikan nama filename dengan nama di attachment
    filename = "Final.pdf"
    attachment = open("/Users/nurfitrianahamsyi/Desktop/Final.pdf", "rb")
 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

your_email = "kitatesprogram@gmail.com" #sesuaikan dengan email gmail
your_password =  "coba_tes123" #ganti password emailnya,sesuaikan dengan email gmail
name_to_display = "Python Sudah Bisa Kirim Email Alhamdulillah... :)"

for item in csvdata:
    name = item[0] #kolom pertama dari file text.text adalah nama yang punya email
    email = item[1] #kolom kedua adalah email. 
    print(f'Sending email to {email}')
    body = "Bismillah... Dear " + name + ", Life doesnt stop after the one we love says farewall and leaves and our sadness will never allow us to let go of our misery it is within our hands to make our days full of laughter  from ALI MAGREBI-BUYOOT ELFARH "
    subject = "Subject"
    sender(email, name_to_display, your_email, your_password, body, subject)

    #linkrefrensi
    #https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib/50212475#50212475
