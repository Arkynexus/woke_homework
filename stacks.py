import numpy as np

class Stack:
    def __init__(self):
        self.abc = np.empty(shape=(0))
            
    def push(self,item):
            self.abc = np.append(self.abc,item)

    def pop(self):
        if self.abc.size == 0:
            return ("Stack is empty!")
        else: 
            
            print("Pop:",self.abc[-1])
            self.abc = np.delete(self.abc,-1)

    def is_empty(self):
        if self.abc.size == 0:
            return True
        else: return False

    def peek(self):
        if self.abc.size == 0:
            return ("Stack is empty!")
        else: return (self.abc[-1])
    
    def size(self):
          return len(self.abc)

s = Stack()
s.push([1,2,3,4,5])
print("Size after push:", s.size())
print("Top element:",s.peek())

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print("Is empty?", s.is_empty())
print("Pop from empty:",s.pop())