from  errors import IllegalCharacterError, DuplicateOperatorError, ParenthesisError

#now on Github
ALLOWED_CHARS = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "%", " ", "(", ")"}
OPERANTS = {"+", "-", "*", "%", "/"}


def run():
    try:
        s = str(input("Input your equation: "))
    except TypeError as e:
        print(e)
        return

    s = string_format(s, OPERANTS ^ {"(", ")"})
    s = s.split(" ")

    for c in s:
        if c == "":
            s.remove("")

    s = solve_parantheses(s)

    if check_for_dublicate_operants(s):
        raise DuplicateOperatorError

    if not check_if_characters_legal(s):
        raise IllegalCharacterError

    print(math(s))

def solve_parantheses(s):
    if "(" in s and ")" not in s or ")" in s and "(" not in s:
        raise ParenthesisError

    while "(" and ")" in s:
        start = None
        end = None
        i = 0
        while i < len(s):
            if s[i] == "(":
                start = i
            if s[i] == ")":
                end = i
                if start is None:
                    raise ParenthesisError
                s = replace_parenthesis_with_result(s, start, end)

            i += 1

    return s

      
def check_if_characters_legal(s):
    for c in s:
        if len(c) > 1:
            for d in c:
                if d not in ALLOWED_CHARS:
                    return False
        else:
            if c not in ALLOWED_CHARS:
                return False
    return True

def math(s):
    i = 0

    while i < len(s):
        if s[i] == "%":
            n = float(s[i - 1]) % float(s[i + 1])
            apply_result_to_array(s, i, n)
            i = 0
        i += 1

    i = 0

    while i < len(s):
        if s[i] == "*":
            n = float(s[i - 1]) * float(s[i + 1])
            apply_result_to_array(s, i, n)
            i = 0
        if s[i] == "/":
            n = float(s[i - 1]) / float(s[i + 1])
            apply_result_to_array(s, i, n)
            i = 0
        i += 1

    i = 0

    while i < len(s):
        if s[i] == "+":
            n = float(s[i - 1]) + float(s[i + 1])
            apply_result_to_array(s, i, n)
            i = 0
        if s[i] == "-":
            n = float(s[i - 1]) - float(s[i + 1])
            apply_result_to_array(s, i, n)
            i = 0
        i += 1

    return s[0]

def replace_parenthesis_with_result(s, start, end):
    temp = s[start:end+1]
    print(temp)
    remove_parentheses(temp)
    print(temp)

    result = math(temp)
    print(result)
    remove_slice_from_list(s, s[start:end], start+1)
    s[start] = str(int(result))
    print(s)

    return s

def remove_slice_from_list(li, listslice, start):
    for i in range(len(listslice)):
        li.pop(start)


def remove_parentheses(s):
    i = 0
    while i < len(s):
        if s[i] == "(" or s[i] == ")":
            s.pop(i)
            i = 0
        i += 1

def apply_result_to_array(s, i, n):
    s[i] = n
    s.pop(i - 1)
    s.pop(i)

def string_format(s, l):
    s = s.replace(" ", "")

    i = 0
    while i < len(s):
        if s[i] in l:
            s = insert_space(s, i)
            s = insert_space(s, i+2)
            i += 1
        i += 1
    return s

def insert_space(string, index):
    return string[:index] + ' ' + string[index:]

def check_for_dublicate_operants(s):
    i = 0
    while i < len(s):
        if s[i] in OPERANTS:
            if s[i + 1] in OPERANTS or s[i - 1] in OPERANTS:
                return True
        i += 1
    return False


if __name__ == '__main__':
    run()
