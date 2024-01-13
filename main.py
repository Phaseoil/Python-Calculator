ALLOWED_CHARS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "%", " ")
OPERANTS = ("+", "-", "*", "%", "/")


def run():
    try:
        s = str(input("Input your equation: "))
    except TypeError as e:
        print(e)
        return
    
    s = string_format(s)

    s = s.split(" ")

    if "" in s:
        s.remove("")

    if check_for_dublicate_operants(s):
        print(f"you have used two operants in conjuction, this is not a mathematical expression. usable operands are: {OPERANTS}")
        return

    if not check_if_characters_legal(s):
        print(f"you used illegal characters, legal characters are: {ALLOWED_CHARS}")
        return
    
    print(Math(s))
            
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

def Math(s):
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

def apply_result_to_array(s, i, n):
    s[i] = n
    s.pop(i - 1)
    s.pop(i)

def string_format(s):
    s = s.replace(" ", "")

    i = 0
    while i < len(s):
        if s[i] in OPERANTS:
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