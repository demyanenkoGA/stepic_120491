import pytest


@pytest.fixture
def set_up():
    print("Enter System Success")


def test_sending_mail_1():
    print("<Send Mail 1>")


def test_sending_mail_2():
    print("<Send Mail 2>")


# > pytest
# > pytest -s -v

