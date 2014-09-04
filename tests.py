# coding=utf8

import sys
import time
sys.path.insert(0, '.')
import ssdb

c = ssdb.Client()

uk_cursor = time.time()


def uk(prefix='key'):
    global uk_cursor
    uk_cursor = uk_cursor + 1
    return '%s-%d' % (prefix, uk_cursor)


def test_set():
    assert c.set(uk(), 'v') == 1


def test_setx():
    key = uk()
    assert c.setx(key, 'v', 1.2) == 1
    assert c.ttl(key) <= 1.2
    time.sleep(1.2)
    assert c.exists(key) is False


def test_expire():
    key = uk()
    assert c.set(key, 'v') == 1
    assert c.expire(key, 1.2) == 1
    assert c.ttl(key) <= 1.2
    assert c.expire(uk(), 1.1) == 0


def test_ttl():
    key = uk()
    assert c.setx(key, 'v', 1.2) == 1
    assert 0 < c.ttl(key) <= 1.2


def test_setnx():
    key = uk()
    assert c.setnx(key, 'v') == 1
    assert c.setnx(key, 'v') == 0


def test_get():
    key = uk()
    assert c.set(key, 'v') == 1
    assert c.get(key) == 'v'


def test_getset():
    key = uk()
    assert c.set(key, 'v') == 1
    assert c.getset(key, 'val') == 'v'


def test_del():
    key = uk()
    assert c.set(key, 'v')
    assert c.delete(key) == 1
    assert c.exists(key) is False


def test_incr():
    key = uk()
    assert c.set(key, 1) == 1
    assert c.incr(key, 2) == 3
    assert c.get(key) == '3'


def test_getbit():
    key = uk()
    assert c.set(key, 'val') == 1
    assert c.getbit(key, 2) == 1


def test_setbit():
    key = uk()
    assert c.set(key, 'val') == 1
    assert c.setbit(key, 2, 0) == 1
    assert c.getbit(key, 'ral')


def test_exists():
    key = uk()
    assert c.set(key, 'val') == 1
    assert c.exists(key) is True
    assert c.exists(uk()) is False


def test_big_data():
    key = uk()
    val = '123456' * 65536
    assert c.set(key, val) == 1
    assert c.get(key) == val
