import pytest
import send_mail


def test_mail_was_sent(mocker):
    mocker.patch('send_mail.smtplib.SMTP')
    sendmail_mock = mocker.patch('send_mail.smtplib.SMTP.sendmail')
    exec(open("send_mail.py").read())
    assert sendmail_mock.called



