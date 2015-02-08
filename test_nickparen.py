def test_best_case_balanced():
    from nickparen import check_parentheses
    val = check_parentheses(u"()")
    assert val == 0
