# coding=utf8


import sys
sys.path.insert(0, '.')
import time
import random

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
        assert 0 < c.ttl('key') <= 5

    def test_setnx(self):
        key = random.randint(1000, 9999)
        assert c.setnx(key, 'val') == 1
        assert c.setnx(key, 'val') == 0

    def test_getset(self):
        assert c.set('key', 'val') == 1
        assert c.getset('key', 'newval') == 'val'
