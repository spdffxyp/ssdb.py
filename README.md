ssdb.py
=======

Ssdb Python Client Library (threading safe), SSDB is a fast nosql database, an alternative to redis (https://github.com/ideawu/ssdb).

Latest version: v0.1.4

- Support **Python 2.6+ or Python 3.3+**
- Support ssdb version: **SSDB 1.6.8.8+**
- UTF-8 encoding for all conversions between bytes and unicodes.

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

### Pipeline

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

### Returns

1. If response status is `"ok"`, return value request.
2. If response status is `"not_found"`, return `None`.
3. If response status is `"client_error"` or other(errors), raise `SSDBException`.

### Built-in Exceptions

```python
class SSDBException(Exception):
    pass
```

### Unicode & Bytes Issue

- In Python2:

   ```python
   >>> ssdb = SSDBClient()
   >>> ssdb.set(u'你好', u'世界')
   1
   >>> ssdb.get(u'你好')
   '\xe4\xb8\x96\xe7\x95\x8c'
   ```

- In Python3:

   ```python
   >>> ssdb = SSDBClient()
   >>> ssdb.set('你好', '世界')
   1
   >>> ssdb.get('你好', '世界')
   '世界'
   ```

In a word, all unicodes will be encoded to bytes before sending to
ssdb, and stored as bytes in ssdb, string values from ssdb perform as 
native `str` in Python.

Documentation
--------------

Detail docs for this module can be found at https://github.com/hit9/ssdb.api.docs

License
-------

[LICENSE-BSD2](LICENSE-BSD2)
