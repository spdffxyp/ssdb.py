# coding=utf8


import sys
sys.path.insert(0, '.')
import time
import random

from ssdb import SSDBClient


c = SSDBClient()

############# helper functions #######################


def rand_key():
    return 'key' + str(random.randint(10000, 99999))


############# test cases #############################


class TestCases(object):

    def setUp(self):
        # clear keys, all hashes, all zsets, all queues
        keys = c.keys('', '', -1)
        for key in keys:
            c.delete(key)

        hashes = c.hlist('', '', -1)
        for hash in hashes:
            c.hclear(hash)

        zsets = c.zlist('', '', -1)
        for zset in zsets:
            c.zclear(zset)

        queues = c.qlist('', '', -1)
        for queue in queues:
            c.qclear(queue)

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
        key = rand_key()
        assert c.setnx(key, 'val') == 1
        assert c.setnx(key, 'val') == 0

    def test_getset(self):
        assert c.set('key', 'val') == 1
        assert c.getset('key', 'newval') == 'val'

    def test_delete(self):
        assert c.set('key', 'val') == 1
        assert c.delete('key') == 1
        assert c.delete('key-not-exist' + str(random.randint(1000, 9999))) == 1

    def test_incr(self):
        assert c.set('key', 1) == 1
        assert c.incr('key', 2) == 3

    def test_exists(self):
        assert c.exists(rand_key()) is False
        assert c.set('key', 'val') == 1
        assert c.exists('key') is True

    def test_getbit(self):
        assert c.set('key', 'val') == 1
        assert c.getbit('key', 2) == 1
        assert c.getbit(rand_key(), 1) == 0

    def test_setbit(self):
        assert c.set('key', 'val') == 1
        assert c.setbit('key', 2, 0) == 1
        assert c.getbit('key', 2) == 0

        key = rand_key()
        assert c.setbit(key, 1, 1) == 0
        assert c.setbit(key, 1, 1) == 1

    def test_countbit(self):
        assert c.set('key', 'val')
        assert c.countbit('key') == 8

    def test_substr(self):
        assert c.set('key', 'some string')
        assert c.substr('key', 0, 4) == 'some'
        assert c.substr('key', 0, -1) == 'some strin'
        assert c.substr('key') == 'some string'

    def test_strlen(self):
        assert c.set('key', 'val')
        assert c.strlen('key') == 3

    def test_keys(self):
        assert c.set('key1', 'val1')
        assert c.set('key2', 'val2')
        assert c.keys('', '', -1) == ['key1', 'key2']

    def test_scan(self):
        assert c.set('key1', 'val1')
        assert c.set('key2', 'val2')
        assert c.scan('', '', 2) == ['key1', 'val1', 'key2', 'val2']

    def test_rscan(self):
        assert c.set('key1', 'val1')
        assert c.set('key2', 'val2')
        assert c.rscan('', '', 2) == ['key2', 'val2', 'key1', 'val1']

    def test_multi_set(self):
        assert c.multi_set('key1', 'val1', 'key2', 'val2') == 2
        assert c.keys('', '', -1) == ['key1', 'key2']
        assert c.get('key1') == 'val1'
        assert c.get('key2') == 'val2'

    def test_multi_get(self):
        assert c.multi_set('key1', 'val1', 'key2', 'val2') == 2
        assert c.multi_get('key1', 'key2') == ['key1', 'val1', 'key2', 'val2']
