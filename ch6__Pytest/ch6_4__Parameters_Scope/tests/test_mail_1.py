"""
6.4 Знакомство с параметром scope в PyTest
"""


def test_sending_mail_3(set_up, some):
    print(" <Send Mail 1> ")


def test_sending_mail_4(set_up, some):
    print(" <Send Mail 2> ")


# > pytest
# > pytest -s -v

