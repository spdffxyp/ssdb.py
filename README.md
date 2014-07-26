ssdb.py
=======

Ssdb Python Client Library (threading safe).

Latest version: 0.1.0, Support Python 2.7+ and Python 3.3+

Installation
------------

```bash
$ pip install ssdb.py
```

API Reference
-------------

### Sample Usage

```python
>>> from ssdb import SSDBClient
>>> ssdb = SSDBClient(host='localhost', port=8888)
>>> ssdb.set('key', 'val')
1
>>> ssdb.get('key')
'val'
```

### Batch Commands Mode

```python
>>> ssdb.batch()
>>> ssdb.set('key1', 'val1')
>>> ssdb.set('key2', 'val2')
>>> ssdb.set('key3', 'val3')
>>> ssdb.execute()
[1, 1, 1]
```

to disable batch mode (default: False):

```python
>>> ssdb.batch(False)
```

### Built-in Exceptions

```python
class SSDBException(Exception):
    pass
```

License
-------

[LICENSE-BSD2](LICENSE-BSD2)
