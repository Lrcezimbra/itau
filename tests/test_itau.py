import requests

from pyitau.main import Itau


def test_init():
    agency = '0000'
    account = '12345'
    account_digit = '6'
    password = '123456'

    itau = Itau(agency, account, account_digit, password)

    assert itau.agency == agency
    assert itau.account == account
    assert itau.account_digit == account_digit
    assert itau.password == password
    assert isinstance(itau._session, requests.Session)
