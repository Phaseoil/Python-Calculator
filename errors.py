from main import ALLOWED_CHARS, OPERANTS


class ParenthesisError(Exception):
    def __init__(self, message="something went wrong with your parentheses."):
        self.message = message
        super().__init__(self.message)

class DuplicateOperatorError(Exception):
    def __init__(self, message=f"you have used two operants in conjuction, this is not a mathematical expression. usable operands are: {OPERANTS}"):
        self.message = message
        super().__init__(self.message)

class IllegalCharacterError(Exception):
    def __init__(self, message=f"you used illegal characters, legal characters are: {(ALLOWED_CHARS | {"e", "pi"}) ^ set([' '])} "):
        self.message = message
        super().__init__(self.message)
