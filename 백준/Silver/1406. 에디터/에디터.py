import sys

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
        return "".join(self.left + self.right[::-1])

a = sys.stdin.readline().strip()
editor = Editor(a)
n = int(sys.stdin.readline().strip())

for _ in range(n):
    t = sys.stdin.readline().strip()
    if t.startswith('P'):
        editor.P(t[2:])
    elif t == 'L':
        editor.L()
    elif t == 'D':
        editor.D()
    elif t == 'B':
        editor.B()

sys.stdout.write(editor.R() + "\n")