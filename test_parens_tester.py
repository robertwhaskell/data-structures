import pytest
from parens_tester import parens_tester


@pytest.fixture
def balanced_parens_stack(request):
    p = parens_tester('()()()()()((()))')
    return p


@pytest.fixture
def balanced_parens_stack_simple(request):
    p = parens_tester('()')
    return p


@pytest.fixture
def open_parens_stack(request):
    p = parens_tester('()()()()()((()))((()(')
    return p


@pytest.fixture
def open_parens_stack_simple(request):
    p = parens_tester('(')
    return p



@pytest.fixture
def broken_parens_stack(request):
    p = parens_tester('()()()()()((())))))')
    return p


@pytest.fixture
def broken_parens_stack_simple(request):
    p = parens_tester(')')
    return p


def test_balanced(balanced_parens_stack):
    assert balanced_parens_stack == 0


def test_balanced_simple(balanced_parens_stack_simple):
    assert balanced_parens_stack_simple == 0


def test_open(open_parens_stack):
    assert open_parens_stack == 1


def test_open_simple(open_parens_stack_simple):
    assert open_parens_stack_simple == 1


def test_broken(broken_parens_stack):
    assert broken_parens_stack == -1


def test_broken_simple(broken_parens_stack_simple):
    assert broken_parens_stack_simple == -1
