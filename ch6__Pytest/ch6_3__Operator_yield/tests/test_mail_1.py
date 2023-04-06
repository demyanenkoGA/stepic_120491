"""
6.3 Условный оператор yield
"""
import pytest


@pytest.fixture
def set_up():
    print("Enter System Success")
    yield
    print("Logout System\n")


def test_sending_mail_1(set_up):
    print("<Send Mail 1>")


def test_sending_mail_2(set_up):
    print("<Send Mail 2>")


# > pytest
# > pytest -s -v

