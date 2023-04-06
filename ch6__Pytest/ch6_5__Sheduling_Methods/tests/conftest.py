"""
6.4 Знакомство с параметром scope в PyTest
"""

import pytest


@pytest.fixture
def set_up():
    print("\nEnter System Success")
    yield
    print("\nLogout System\n")


@pytest.fixture(scope="function")  # module - обертка для всего файла, function - обертка для каждой функции, по аналогии с работой set_up
def some():
    print("\n Начало ")
    yield
    print("\n Конец \n")
