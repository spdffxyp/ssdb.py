ssdb.py
=======

Ssdb Python Client Library (threading local), SSDB is a fast nosql database, an alternative to redis (https://github.com/ideawu/ssdb).

Latest version: v0.1.5 ![](https://travis-ci.org/hit9/ssdb.py.svg)

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
>>> import ssdb
>>> c = ssdb.Client()
>>> c.set('key', 'val')
1
>>> c.get('key')
'val'
```

### Pipeline

```python
>>> with c.pipeline() as pipe:
...   pipe.set('k1', 'v1')
...   pipe.set('k2', 'v2')
...   pipe.multi_get('k1', 'k2')
...   pipe.execute()
...
[1, 1, ['k1', 'v1', 'k2', 'v2']]
```

### Returns

1. If response status is `"ok"`, return the data.
2. If response status is `"not_found"`, return `None`.
3. If response status is `"client_error"` or other(errors), raise `SSDBException`.


### Built-in Exceptions

```python
class SSDBException(Exception):
    pass
```

Types
-----

The data type each command returns can be found in [ssdb.py](ssdb.py) `commands`.

**Note:** zset scores will be cast to int from v0.1.5.

Documentation
--------------

Detail docs for this module can be found at https://github.com/hit9/ssdb.api.docs

License
-------

[LICENSE-BSD2](LICENSE-BSD2)
