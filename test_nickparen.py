import pytest

def test_best_case_balanced():
    from nickparen import check_parentheses
    assert check_parentheses(u'()') == 0


def test_best_case_open():
    from nickparen import check_parentheses
    assert check_parentheses(u'((') == 1


def test_best_case_broken():
    from nickparen import check_parentheses
    assert check_parentheses(u')(') == -1


def test_best_case_bytestring():
    from nickparen import check_parentheses
    assert check_parentheses("()") == 0


def test_not_unicode():
    from nickparen import check_parentheses
    with pytest.raises(TypeError):
        check_parentheses(5)
