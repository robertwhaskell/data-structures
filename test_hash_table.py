import pytest
from hash_table import Hash_Table

@pytest.fixture(scope='function')
def empty_hash():
    h = Hash_Table()
    return h


@pytest.fixture(scope='function')
def populated_hash():
    h = Hash_Table()
    h.set('pearkey', 'pear')
    h.set('orangekey', 'orange')
    h.set('applekey', 'applekey')
    return h


def test_hash_init_empty():
    h = Hash_Table()
    assert h.hash_table == [None]


def test_hash_init_with_table_size():
    h = Hash_Table(1024)
    assert len(h.hash_table) == 1024


def test_get(populated_hash):
    assert populated_hash.get('pearkey') == 'pear'


def test_set(empty_hash):
    empty_hash.set('plumkey', 'plum')
    assert empty_hash.get('plumkey') == 'plum'


def test_hash(empty_hash):
    assert empty_hash.hash('abc') == 294 % len(empty_hash.hash_table)
