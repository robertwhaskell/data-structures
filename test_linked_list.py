import linked_list
import pytest


@pytest.fixture
def fix_populated_list(request):
    full_list = linked_list.list()
    full_list.insert(True)
    full_list.insert(500)
    full_list.insert("")
    full_list.insert("Thing")
    full_list.insert(None)
    full_list.insert(1000)
    return full_list


@pytest.fixture
def fix_empty_list(request):
    empty_list = linked_list.list()
    return empty_list


def test_Node_with_value():
    testnode = linked_list.Node(5)
    assert testnode.val == 5
    assert testnode.next is None


def test_Node_with_value_and_next():
    nextnode = linked_list.Node(5)
    testnode = linked_list.Node(6, nextnode)
    assert testnode.val == 6
    assert testnode.next == nextnode


def test_list_with_no_head():
    testlist = linked_list.list()
    assert testlist.size() == 0
    assert testlist.head is None


def test_list_with_head():
    testnode = linked_list.Node(5)
    testlist = linked_list.list(testnode)
    assert testlist.size() == 1
    assert testlist.head == testnode


def test_size_empty_list(fix_empty_list):
    assert fix_empty_list.size() == 0


def test_size_full_list(fix_populated_list):
    assert fix_populated_list.size() == 6


def test_pop_empty_list(fix_empty_list, fix_populated_list):
    with pytest.raises(ValueError):
        fix_empty_list.pop()


def test_pop_full_list(fix_populated_list):
    assert fix_populated_list.pop() == 1000
    assert fix_populated_list.size() == 5


def test_pop_to_empty_list(fix_populated_list):
    while fix_populated_list.size() > 1:
        fix_populated_list.pop()
    assert fix_populated_list.pop() is True
    with pytest.raises(ValueError):
        fix_populated_list.pop()


def test_insert_into_empty_list(fix_empty_list):
    assert fix_empty_list.size() == 0
    fix_empty_list.insert("Thingo")
    assert fix_empty_list.size() == 1
    assert fix_empty_list.pop() == "Thingo"


def test_insert_into_full_list(fix_populated_list):
    assert fix_populated_list.size() == 6
    fix_populated_list.insert("Other Thingo")
    assert fix_populated_list.size() == 7
    assert fix_populated_list.pop() == "Other Thingo"


def test_search(fix_populated_list):
    assert fix_populated_list.search(500).val == 500


def test_search_empty_list(fix_empty_list):
    assert fix_empty_list.search("Doesn't exist") is None


def test_search_not_in_list(fix_populated_list):
    assert fix_populated_list.search("doesn't exist") is None


def test_remove(fix_populated_list):
    assert fix_populated_list.size() == 6
    test_node = fix_populated_list.search(500)
    fix_populated_list.remove(test_node)
    assert fix_populated_list.search(500) is None
    assert fix_populated_list.size() == 5


def test_remove_not_in_list(fix_populated_list):
    assert fix_populated_list.remove("Doesn't Exist") is None


def test_remove_empty_list(fix_empty_list):
    assert fix_empty_list.remove(True) is None


def test_display_empty_list(fix_empty_list):
    assert fix_empty_list.display() == "()"


def test_displa_full_list(fix_populated_list):
    assert fix_populated_list.display() == ("(1000, None, 'Thing', "
        "'', 500, True)")


def test_unicode_characters(fix_empty_list):
    fix_empty_list.insert(u"J\xf6rg")
    assert fix_empty_list.display() == u"('J\xf6rg')"
