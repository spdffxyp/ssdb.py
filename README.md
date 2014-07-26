ssdb.py
=======

Ssdb Python Client Library (threading safe).

Latest version: 0.1.0, Support Python 2.7+ and Python 3.3+

Installation
------------

```bash
$ pip install ssdb.py
```

API Reference (Redis-py like)
-----------------------------

### Sample Usage

```python
>>> from ssdb import SSDBClient
>>> ssdb = SSDBClient(host='localhost', port=8888)
>>> ssdb.set('key', 'val')
1
>>> ssdb.get('key')
'val'
```

### Pipline

```python
>>> ssdb = SSDBClient()
>>> with ssdb.pipeline() as pipe:
...   pipe.set('k1', 'v1')
...   pipe.set('k2', 'v2')
...   pipe.multi_get('k1', 'k2')
...   pipe.execute()
...
[1, 1, ['k1', 'v1', 'k2', 'v2']]
```

### Built-in Exceptions

```python
class SSDBException(Exception):
    pass
```

License
-------

[LICENSE-BSD2](LICENSE-BSD2)
