def dup(stack):
    result = stack.pop()
    stack.append(result)
    stack.append(result)
    return stack

def swap(stack):
    oldTop = stack.pop()
    newTop = stack.pop()
    stack.append(oldTop)
    stack.append(newTop)
    return stack

def over(stack):
    oldTop = stack.pop()
    sandwich = stack.pop()
    stack.append(sandwich)
    stack.append(oldTop)
    stack.append(sandwich)
    return stack

def rot(stack):
    oldTop = stack.pop()
    oldMiddle = stack.pop()
    oldBottom = stack.pop()
    stack.append(oldMiddle)
    stack.append(oldTop)
    stack.append(oldBottom)
    return stack

def drop(stack):
    stack.pop()
    return stack

def nip(stack):
    stack = swap(stack)
    return drop(stack)

def tuck(stack):
    stack = swap(stack)
    return over(stack)

def minusRot(stack):
    stack = rot(stack)
    return rot(stack)

def twoDup(stack):
    top = stack.pop()
    bottom = stack.pop()
    stack.append(bottom)
    stack.append(top)
    stack.append(bottom)
    stack.append(top)
    return stack

def twoSwap(stack):
    oldTopTop = stack.pop()
    oldTopBottom = stack.pop()
    oldBottomTop = stack.pop()
    oldBottomBottom = stack.pop()
    stack.append(oldTopBottom)
    stack.append(oldTopTop)
    stack.append(oldBottomBottom)
    stack.append(oldBottomTop)
    return stack

def twoOver(stack):
    oldTopTop = stack.pop()
    oldTopBottom = stack.pop()
    sandwichTop = stack.pop()
    sandwichBottom = stack.pop()
    stack.append(sandwichBottom)
    stack.append(sandwichTop)
    stack.append(oldTopBottom)
    stack.append(oldTopTop)
    stack.append(sandwichBottom)
    stack.append(sandwichTop)
    return stack
