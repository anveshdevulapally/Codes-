class myStack:

     def __init__(self):

          self.items = []

     def isEmpty(self):
          if self.items == []:
               print("Stack is Empty")
          else:
               print("Stack is full")

         
     def push(self, item):
          self.items.append(item)
          print("Elements have been Pushed")

         
     def pop(self):
          return self.items.pop()
        
        
     def peek(self):
          return self.items[-1]
        
     def size(self):
          return len(self.items)
         
     def show(self):
          return self.items
         

s = myStack()
s.isEmpty()
s.push('1')
s.push('2')
s.isEmpty()
print("before Popping :",s.peek())
print("Element has been Popped :",s.pop())
print("After Popping :",s.peek())
print("After Popping total elements :",s.show())
print("Total Size :",s.size())
