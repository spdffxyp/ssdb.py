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
    assert c.get(key) == 'ral'


def test_countbit():
    key = uk()
    assert c.set(key, 'val') == 1
    assert c.countbit(key) == 8


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


def test_substr():
    key = uk()
    assert c.set(key, 'hello world') == 1
    assert c.substr(key) == 'hello world'
    assert c.substr(key, 6, 10) == 'world'


def test_strlen():
    key = uk()
    assert c.set(key, 'hello world') == 1
    assert c.strlen(key) == 11


def test_keys_scan_rscan():
    start = uk()
    a = uk()
    b = uk()
    assert c.set(a, 1) == 1
    assert c.set(b, 1) == 1
    assert c.keys(start, uk(), 2) == [a, b]
    assert c.scan(start, uk(), -1) == [a, '1', b, '1']
    assert c.rscan(uk(), start, -1) == [b, '1', a, '1']


def test_multi_set_get_del():
    k1, k2, k3 = [uk() for i in range(3)]
    assert c.multi_set(k1, 'v1', k2, 'v2', k3, 'v3') == 3
    assert c.multi_get(k1, k2, k3) == [k1, 'v1', k2, 'v2', k3, 'v3']
    assert c.multi_del(k1, k2, k3) == 3 == 3


def test_hset_hget_hincr_hexists():
    pass
