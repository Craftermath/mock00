# test_sender.py

import pytest
from sender import send
from settings import SENDER_EMAIL, SENDER_PASSWORD
import smtplib


def test_mail_was_sent(monkeypatch, tmp_path):
    """Test send function calls SMTP methods and sends emails correctly."""
    csv_file_path = tmp_path / "csv_mails.csv"
    with open(csv_file_path, "w", newline="") as csvfile:
        csvfile.write("nome,email,coluna3,col4,col5\n")
        csvfile.write("Maria,ma@algummail.com,yes,azul,123\n")
        csvfile.write("Joana,jo@algummail.com,no,azul,234\n")
        csvfile.write("Franscisca,fran@algummail.com,yes,amarelo,345\n")

    class MockSMTP:
        def __init__(self, hostname):
            self.hostname = hostname
            self.ehlo_called = 0
            self.starttls_called = False
            self.login_called = False
            self.sendmail_called = 0
            self.quit_called = False

        def ehlo(self):
            self.ehlo_called += 1

        def starttls(self):
            self.starttls_called = True

        def login(self, email, password):
            self.login_called = True
            self.email = email
            self.password = password

        def sendmail(self, sender, recipient, message):
            self.sendmail_called += 1

        def quit(self):
            self.quit_called = True

    mock_smtp_instance = MockSMTP("smtp.meumail.com")
    monkeypatch.setattr("smtplib.SMTP", lambda hostname: mock_smtp_instance)

    send(csv_file_path=csv_file_path, hostname="smtp.meumail.com")

    assert mock_smtp_instance.ehlo_called == 2, "ehlo() was not called twice"
    assert mock_smtp_instance.starttls_called, "starttls() was not called"
    assert mock_smtp_instance.login_called, "login() was not called"
    assert mock_smtp_instance.sendmail_called == 3, "sendmail() was not called 3 times"
    assert mock_smtp_instance.quit_called, "quit() was not called"
    assert mock_smtp_instance.email == SENDER_EMAIL, "Incorrect email used for login"
    assert mock_smtp_instance.password == SENDER_PASSWORD, "Incorrect password used for login"
