# Stack based problems

"""
Paranthesis check
"""

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

"""
In our cafeteria scenario, a method designed to manage the cafeteria trays has been acting up. 
It's supposed to notify us when there are no more trays to remove, but it seems to be missing that step. 
Can you identify what's gone wrong and apply a fix? The comfort of our cafeteria's patrons depends on it! 
"""

class CafeteriaStack:
    def __init__(self):
        self.stack = []
    
    def add_tray(self, tray_id):
        self.stack.append(tray_id)
        print(self.stack[-1])
    
    def remove_tray(self):
        if not self.stack:  # Simplified check for an empty stack
            print("No more trays!")
            return None
        return self.stack.pop()

# Sample usage
cafeteria = CafeteriaStack()
cafeteria.add_tray("Tray_4")  
print(cafeteria.remove_tray())  
print(cafeteria.remove_tray()) 


"""
In our cafeteria scenario, we're once again looking after trays, but this time with a twist: you'll add a vital element to our tray monitoring system. 
Your task is to determine which tray will be served next without removing it from the stack, 
but this crucial bit is missing. Can you fill in the gaps to keep our cafeteria running smoothly?
"""

# Define a function to check for the next available tray without removing it
def next_tray(stack):
    # TODO: Return the top-most tray without removing it from the stack
    if stack:
        return stack[-1]
    return "No trays available."

# Initialize the stack with tray IDs
tray_stack = [1001, 1002, 1003]

# TODO: Use the `next_tray` function to check and print which tray will be served next
print(next_tray(tray_stack))

# Simulate removing a tray from the stack
tray_stack.pop()

# TODO: Use the `next_tray` function to check and print the next tray after one is removed
print(next_tray(tray_stack))



if __name__ == '__main__':
    # example1= "()[{}]"
    # if ParanthesisChk(example1):
    #     print(f"{example1} is a valid paranthesis string")
    # else:
    #     print(f"{example1} is not a valid paranthesis")
    # example2 = "([]()"
    # if ParanthesisChk(example2):
    #     print(f"{example2} is a valid paranthesis string")
    # else:
    #     print(f"{example2} is not a valid paranthesis")