# sender.py

import csv
import smtplib
from settings import SENDER_EMAIL, SENDER_PASSWORD


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


def send(csv_file_path="csv_mails.csv", hostname="smtp.meumail.com"):
    with open(csv_file_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        next(csv_reader)  # Skip the header row

        smtp = smtplib.SMTP(hostname)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)

        for row in csv_reader:
            nome, email, coluna3, col4, col5 = row
            if coluna3 == "yes":
                msg = MENSAGEM_1.format(nome, col4)
                subject = "Título do Assunto"
            else:
                msg = MENSAGEM_2.format(nome)
                subject = "Outro Título"

            email_msg = f"Subject: {subject}\n\n{msg}"
            smtp.sendmail(SENDER_EMAIL, email, email_msg)

        smtp.quit()
