class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    # Application of stack : reverse string

def reverserString(inputString):
    tempStack = Stack()
    newString = ""
    for i in range (len(inputString)):
        tempStack.push(inputString)
    for i in range(len(inputString)):
        newString += tempStack.pop()
    return newString

# Application of Stack : General balanced symbol

def matches(openSymbol, closeSymbol):
    opens = "([{"
    closer = ")]}"
    return opens.index(openSymbol) == closer.index(closeSymbol)

def perChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    return balanced and s.isEmpty()

# Application : decimal number converting into any other base

def baseConverter(decNumber, base):
    digit = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber
    newString = ""
    while not remstack.isEmpty():
        newString += digit[remstack.pop()]
    return newString

# Applicaiton : infix to postfix notation
def infixToPostfix(infixepr):
    prec = {}
    prec["**"]
    prec["*"]
    prec["/"]
    prec[""]