import uiautomator2 as ut2
import pytest


def init_driver(self, device_name):
    try:
        print(device_name)
        d = ut2.connect(device_name)
        d.wait_timeout = 20.0
        d.click_post_delay = 8
        return d
    except Exception as e:
        print('ddd')


def test_case1():
    assert 1 == 1
