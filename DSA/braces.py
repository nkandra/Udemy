#Method returns true or false based on the string of braces in proper format or not 
# Example: "{}([{}])" should resturn true where as "{[{(})}" should return false 
#Using stack
import pdb

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
 
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size - 1]        


def braces(arr):
    if len(arr) % 2 != 0:
        return False
    open_braces = ['(', '{', '[']
    matching_tups = [('(', ')'), ('{', '}'), ('[', ']')]
    
    s = Stack()
    for bracket in arr:
        if bracket in open_braces:
           s.push(bracket)
        else:
           if s.size()==0:
               return False
           poped_bracket = s.pop()
           if (poped_bracket, bracket) not in matching_tups:
               return False
    return s.size() == 0 

print braces("{}([{}])")
print braces("{}{}])")
print braces("{}{}([])")

