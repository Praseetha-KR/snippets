import re


def str_to_infix(expr: str) -> list:
    return expr.split(' ')


def is_operator(token: str) -> bool:
    return token in ['+', '-', '*', '/']


def is_operand(token: str) -> bool:
    return bool(re.match(r'^[0-9\.]+$', token))


def has_high_precedence(op1: str, op2: str) -> bool:
    if op1 in ['*', '/']:
        if op2 in ['+', '-']:
            return True
    return False


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


def operate(operator: str, a: str, b: str) -> float:
    x = float(a)
    y = float(b)
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
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
