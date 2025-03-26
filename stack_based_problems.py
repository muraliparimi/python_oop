# Stack based problems


def ParanthesisChk(paren_string):
    paren_dict = {')' : '(', '}' : '{', ']' : '[', '>' : '<'}
    stack = []
    index = 0
    while index < len(paren_string):
        paren = paren_string[index]
        if paren in paren_dict.values():
            stack.append(paren)
        elif paren in paren_dict:
            if stack and stack[-1] == paren_dict[paren]:
                stack.pop()
            else:
                return False
        index +=1
        #print("execution in progress")
    return True if len(stack) == 0 else False

if __name__ == '__main__':
    example1= "()[{}]"
    if ParanthesisChk(example1):
        print(f"{example1} is a valid paranthesis string")
    else:
        print(f"{example1} is not a valid paranthesis")
    example2 = "([]()"
    if ParanthesisChk(example2):
        print(f"{example2} is a valid paranthesis string")
    else:
        print(f"{example2} is not a valid paranthesis")