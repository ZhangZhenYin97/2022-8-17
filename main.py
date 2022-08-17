import pytest


def test_demo1():
    print('success')
    assert "Allure success!"


if __name__ == '__main__':
    pytest.main("-v,-s",[__file__])
