from stack import Stack


def parens_tester_non_stack(parens):
    open_count = 0
    for paren in parens:
        if paren == '(':
            open_count += 1
        elif paren == ')':
            open_count -= 1
        if open_count < 0:
            return -1
    if open_count > 0:
        return 1
    return 0


def next_value(stack):
    try:
        val = stack.pop()
    except AttributeError:
        return None
    return val


def parens_tester(parens=''):
    init_stack = Stack()
    for char in parens:
        if char == '(':
            init_stack.push(char)
        elif char == ')':
            if not next_value(init_stack):
                return -1
    if next_value(init_stack):
        return 1
    return 0
