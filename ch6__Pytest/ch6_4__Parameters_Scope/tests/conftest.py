"""
6.4 Знакомство с параметром scope в PyTest
"""

import pytest


@pytest.fixture
def set_up():
    print("Enter System Success")
    yield
    print("Logout System\n")


@pytest.fixture(scope="function")  # module - обертка для всего файла, function - обертка для каждой функции, по аналогии с работой set_up
def some():
    print(" Начало ")
    yield
    print(" Конец \n")
