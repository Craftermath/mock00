import pytest
from sender import send
from settings import SENDER_EMAIL, SENDER_PASSWORD
import smtplib


def test_mail_was_sent(mocker):
    mock_smtp = mocker.patch('smtplib.SMTP')
    csv_file_path = "csv_mails.csv"

    # Call the send function
    send(csv_file_path)

    # Verify SMTP was called correctly
    mock_smtp.return_value.ehlo.assert_called()
    mock_smtp.return_value.starttls.assert_called()
    mock_smtp.return_value.login.assert_called_with(SENDER_EMAIL, SENDER_PASSWORD)
    mock_smtp.return_value.sendmail.assert_called()
    mock_smtp.return_value.quit.assert_called()
