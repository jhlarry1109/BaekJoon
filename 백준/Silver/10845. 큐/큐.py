class Queue:
    li = []

    def push(self, a):
        self.li.append(a)
        
    def pop(self):
        if self.empty():
            return -1
        return self.li.pop(0)

    def size(self):
        return len(self.li)

    def empty(self):
        if self.li:
            return 0
        return 1

    def front(self):
        if self.empty():
            return -1
        return self.li[0]

    def back(self):
        if self.empty():
            return -1
        return self.li[len(self.li)-1]

queue = Queue()
n = int(input())
for _ in range(n):
    a = input()
    if a[:4] == "push":
        queue.push(a[5:])
    elif a == "pop":
        print(queue.pop())
    elif a == "size":
        print(queue.size())
    elif a == "empty":
        print(queue.empty())
    elif a == "front":
        print(queue.front())
    elif a == "back":
        print(queue.back())