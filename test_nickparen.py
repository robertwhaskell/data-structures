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


def test_no_parentheses():
    from nickparen import check_parentheses
    assert check_parentheses(u"foo") == 0


def test_symbols_string_unicode():
    from nickparen import check_parentheses
    assert check_parentheses(u"@!%^'(&^$*") == 1


def test_symbols_string_bytestring():
    from nickparen import check_parentheses
    assert check_parentheses("!#@$&^*)") == -1


def test_multiple_words():
    from nickparen import check_parentheses
    assert check_parentheses(u"checking multiple words(with parentheses) to"
        "make my mind feel better") == 0
