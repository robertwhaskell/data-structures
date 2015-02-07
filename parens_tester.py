from stack import Stack


def parens_tester_non_stack(parens):
    open_count = 0
    for paren in parens:
        if paren == '(':
            open_count += 1
        else:
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


def parens_tester(parens):
    init_stack = Stack()
    closed_stack = Stack()
    for paren in parens:
        init_stack.push(paren)
    while True:
        # inserts value into p variable.
        p = next_value(init_stack)
        # then, if p == ), push it into closed_stack
        if p == ')':
            closed_stack.push(p)
        # if p is == (, then check to make sure
        # that closed stack has a ). if it doesn't,
        # that means it's open, return 1.
        elif p == '(':
            if not next_value(closed_stack):
                return 1
        # if it does, continue the loop.
        # if p == None, check to see if closed_stack
        # has a value. If it does, return -1, for broken.
        elif next_value(closed_stack):
            return -1
        else:
            return 0
