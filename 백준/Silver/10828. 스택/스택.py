class Stack:
    li = []
    def push(self, a):
        self.li.append(a)
        
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.li.pop()
            
    def size(self):
        return len(self.li)
        
    def empty(self):
        if self.li:
            return 0
        else:
            return 1

    def top(self):
        if self.empty():
            return -1
        else:
            return self.li[len(self.li)-1]

n = int(input())
stack = Stack()
for _ in range(n):
    a = input()
    if a[0:4] == "push":
        stack.push(a[5:])
    elif a[0:3] == "pop":
        print(stack.pop())
    elif a[0:4] == "size":
        print(stack.size())
    elif a[0:5] == "empty":
        print(stack.empty())
    else:
        print(stack.top())