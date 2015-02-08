def check_parentheses(self, string_to_test):
    if not isinstance(unicode, string_to_test):
        raise TypeError
    else:
        count = 0
        for c in string_to_test:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return -1
