"""
6.2 Знакомство с ключами для запуска тестов и анализ результатов
"""
import pytest


@pytest.fixture
def set_up():
    print("Enter System Success")


def test_sending_mail_1(set_up):
    print("<Send Mail 1>")


def test_sending_mail_2(set_up):
    print("<Send Mail 2>")


# > pytest
# > pytest -s -v

