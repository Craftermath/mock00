import pytest
from sender.sender import send
import smtplib


def test_mail_was_sent(mocker):
    mocker.patch('smtplib.SMTP')
    sendmail_mock = mocker.patch('smtplib.SMTP.sendmail')
    send(hostname=mocker.patch)
    assert sendmail_mock.called



