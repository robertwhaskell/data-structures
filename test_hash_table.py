import pytest
from hash_table import Hash_Table


@pytest.fixture(scope='function')
def empty_hash():
    h = Hash_Table()
    return h


@pytest.fixture(scope='function')
def populated_hash():
    h = Hash_Table()
    h.set('pear', 'pear')
    h.set('orange', 'orange')
    h.set('apple', 'apple')
    return h


def test_hash_init_empty():
    h = Hash_Table()
    assert h.hash_table == [None] * 10


def test_hash_init_with_table_size():
    h = Hash_Table(1024)
    assert len(h.hash_table) == 1024


def test_get(populated_hash):
    assert populated_hash.get('pear') == 'pear'


def test_set(empty_hash):
    empty_hash.set('plum', 'plum')
    assert empty_hash.get('plum') == 'plum'


def test_hash(empty_hash):
    assert empty_hash.hash('abc') == 294 % len(empty_hash.hash_table)


def test_bucket_exists_in_case_of_collision(populated_hash):
    populated_hash.set('elppa', 'elppa')
    key_hash = populated_hash.hash('elppa')
    assert populated_hash.hash_table[key_hash] == ['apple', 'elppa']


def test_set_accepts_only_strings(empty_hash):
    with pytest.raises(TypeError):
        empty_hash.set(5, 5)
    with pytest.raises(TypeError):
        empty_hash.set(['hello'], ['hello'])
    with pytest.raises(TypeError):
        empty_hash.set({'hello': 'hello'},{'hello': 'hello'})


def test_set_accepts_only_matching_key_value_pairs(empty_hash):
    with pytest.raises(TypeError):
        empty_hash("doesn't", "match")


def test_get_with_huge_hash():
    h = Hash_Table(1024)
    wordlist = [line.strip() for line in open('/usr/share/dict/words')]

    for word in wordlist:
        h.set(word, word)

    for word in wordlist:
        assert word == h.get(word)
