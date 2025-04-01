class Editor:
    def __init__(self, a):
        self.left = list(a)
        self.right = []
        
    def P(self, x):
        self.left.append(x)
        
    def L(self):
        if self.left:
            self.right.append(self.left.pop())

    def D(self):
        if self.right:
            self.left.append(self.right.pop())

    def B(self):
        if self.left:
            self.left.pop()

    def R(self):
        return self.left + self.right[::-1]


a = input()
editor = Editor(a)
n = int(input())
for _ in range(n):
    t = input()
    if t[:1] == 'P':
        editor.P(t[2:])
    elif t[:1] == 'L':
        editor.L()
    elif t[:1] == 'D':
        editor.D()
    elif t[:1] == 'B':
        editor.B()
        
print(*editor.R(),sep="")