import re


def is_operator(token: str) -> bool:
    return token in ['+', '-', '*', '/']


def is_operand(token: str) -> bool:
    return bool(re.match(r'^[0-9\.]+$', token))


def has_high_precedence(op1: str, op2: str) -> bool:
    if op1 in ['*', '/']:
        if op2 in ['+', '-']:
            return True
    return False


def str_to_infix(expr: str) -> list:
    arr = []
    buffer = ''
    string = expr.replace(' ', '')
    for token in string:
        if is_operator(token):
            arr.append(buffer)
            arr.append(token)
            buffer = ''
            continue
        elif is_operand(token):
            buffer += token
            continue
    arr.append(buffer)
    return arr


def infix_to_postfix(infix: list) -> list:
    postfix = []
    stack = []
    for token in infix:
        if is_operand(token):
            postfix.append(token)
        elif is_operator(token):
            if not len(stack):
                stack.append(token)
            else:
                while (
                    len(stack) and not has_high_precedence(token, stack[-1])
                ):
                    top = stack.pop()
                    postfix.append(top)
                stack.append(token)
    while len(stack):
        top = stack.pop()
        postfix.append(top)
    return postfix


def has_dot(elem) -> bool:
    return '.' in str(elem)


def cast_ab(a, b) -> ():
    if has_dot(a) or has_dot(b):
        return float(a), float(b)
    return int(a), int(b)


def operate(operator: str, a: str, b: str):
    x, y = cast_ab(a, b)
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x // y
    return None


def postfix_eval(postfix):
    stack = []
    for token in postfix:
        if is_operand(token):
            stack.append(token)
        elif is_operator(token):
            a = stack.pop()
            b = stack.pop()
            result = operate(token, b, a)
            stack.append(result)
    return stack.pop()


def eval_str_expr(strexpr: str) -> float:
    infix = str_to_infix(strexpr)
    postfix = infix_to_postfix(infix)
    return postfix_eval(postfix)


# Sample execution
# result = eval_str_expr("3 + 6 / 2 - 1 * 8 + 4")
