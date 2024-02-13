class Stack:
    def __init__(self):
        self.list=[]
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
# check if the stack is empty.
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    
# push method on the stack.
    def push(self,value):
        self.list.append(value)
        return "you have inserted it sucessfully"

# pop method on the stack.
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    
# peek and element from the stack.
    def peek(self):
        if self.isEmpty():
            return "no element is found on the stack"
# deleting the whole stack.
    def delete(self):
        self.list=None    
stackOne=Stack()
stackOne.push(1)
stackOne.push(3)
stackOne.push(5)
stackOne.pop()
print(stackOne)
print(stackOne.isEmpty())
print(stackOne.peek())
print(stackOne.delete())
    

        
     