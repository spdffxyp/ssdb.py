# coding=utf8


import sys
sys.path.insert(0, '.')
import time

from ssdb import SSDBClient


c = SSDBClient()


class TestCases(object):

    def test_set(self):
        assert c.set('key', 'val') == 1

    def test_setx(self):
        assert c.setx('key', 'val', 5)
        assert c.get('key') == 'val'
        time.sleep(5.1)
        assert c.get('key') is None

    def test_get(self):
        assert c.set('key', 'val') is 1
        assert c.get('key') == 'val'

    def test_expire(self):
        assert c.set('key', 'val')
        assert c.expire('key', 3) == 1
        time.sleep(3.1)
        assert c.get('key') is None

    def test_ttl(self):
        assert c.setx('key', 'val', 5)
        assert c.ttl('key') == 5
