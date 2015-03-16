import pytest
from hash_table import Hash_Table


@pytest.fixture(scope='function')
def empty_hash():
    h = Hash_Table()
    return h


@pytest.fixture(scope='function')
def populated_hash():
    h = Hash_Table()
    h.set('pear_key', 'pear_val')
    h.set('orange_key', 'orange_val')
    h.set('apple_key', 'apple_val')
    return h


def test_hash_init_empty():
    h = Hash_Table()
    assert h.hash_table == [None] * 10


def test_hash_init_with_table_size():
    h = Hash_Table(1024)
    assert len(h.hash_table) == 1024


def test_get(populated_hash):
    assert populated_hash.get('pear_key') == 'pear_val'


def test_set(empty_hash):
    empty_hash.set('plum_key', 'plum_val')
    assert empty_hash.get('plum_key') == 'plum_val'


def test_hash(empty_hash):
    assert empty_hash.hash('abc') == 294 % len(empty_hash.hash_table)


def test_bucket_exists_in_case_of_collision(populated_hash):
    populated_hash.set('elppa_key', 'elppa_val')
    key_hash = populated_hash.hash('elppa_key')
    assert populated_hash.hash_table[key_hash] == [('apple_key', 'apple_val'), ('elppa_key', 'elppa_val')]


def test_set_accepts_only_strings(empty_hash):
    with pytest.raises(TypeError):
        empty_hash.set(5, 5)
    with pytest.raises(TypeError):
        empty_hash.set(['hello'], ['hello'])
    with pytest.raises(TypeError):
        empty_hash.set({'hello': 'hello'},{'hello': 'hello'})


def test_set_overwrites_duplicate_keys(populated_hash):
    assert populated_hash.get('apple_key') == 'apple_val'
    populated_hash.set('apple_key', 'new_apple_val')
    assert populated_hash.get('apple_key') == 'new_apple_val'


# def test_get_with_huge_hash():
#     h = Hash_Table(1024)
#     wordlist = [line.strip() for line in open('/usr/share/dict/words')]

#     for word in wordlist:
#         h.set(word, word)

#     for word in wordlist:
#         assert word == h.get(word)
