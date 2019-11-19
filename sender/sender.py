# sender.py

import csv
import smtplib
from sender.settings import SENDER_EMAIL, SENDER_PASSWORD


MENSAGEM_1 = """
Olá, {}!
Essa é uma mensagem automática q personalizei para parecer simpática enquanto
aprendo mock.
Alguma outra info sua é {}

Espero que gostem,
Bjs,
Carol
"""
MENSAGEM_2 = """
Oi, {}!
Essa é outra mensagem.
Tchau!
"""
def send(hostname="smtp.meumail.com"):
    with open("sender/csv_mails.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        #next(csv_reader)


        smtp = smtplib.SMTP(hostname)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)


        for row in csv_reader:
            nome, email, coluna3, col4, col5 = row
            if coluna3 == "yes":
                msg = MENSAGEM_1.format(nome,col4)
                subject = "Título do Assunto"
            else:
                msg = MENSAGEM_2.format(nome)
                subject = "Outro Título"

        email_msg = "Subject: {} \n\n{}".format(subject,msg)
        smtp.sendmail(SENDER_EMAIL, email, email_msg)
        smtp.quit()
