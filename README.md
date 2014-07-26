ssdb.py
=======

Ssdb Python Client Library (threading safe), SSDB is a fast nosql database, an alternative to redis (https://github.com/ideawu/ssdb).

Latest version: 0.1.1

Support **Python 2.6+ or Python 3.3+**

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

### Returns

1. If response status is `"ok"`, return value request.
2. If response status is `"not_found"`, return `None`.
3. If response status is `"client_error"` or other(errors), raise `SSDBException`.

### Built-in Exceptions

```python
class SSDBException(Exception):
    pass
```

Documentation
--------------

Detail docs for this module can be found at https://github.com/hit9/ssdb.api.docs

License
-------

[LICENSE-BSD2](LICENSE-BSD2)
