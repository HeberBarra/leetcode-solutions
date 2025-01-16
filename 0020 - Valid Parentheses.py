def verify_parentheses(s: str) -> bool:
    if len(s) < 2 or len(s) % 2 != 0:
        return False

    pars = []

    for i in range(len(s)):

        if s[i] in '([{':
            pars.append(s[i])
            continue

        if len(pars) == 0:
            return False

        if s[i] == ')' and pars[-1] == '(':
            pars.pop()
        elif s[i] == ']' and pars[-1] == '[':
            pars.pop()
        elif s[i] == '}' and pars[-1] == '{':
            pars.pop()
        else:
            pars.append(s[i])

    return len(pars) == 0


if __name__ == '__main__':
    print(verify_parentheses('))'))
    print(verify_parentheses('{{'))
    print(verify_parentheses('(]'))
    print(verify_parentheses('[]'))
