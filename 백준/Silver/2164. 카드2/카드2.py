from collections import deque

class Card:
    def __init__(self, n):
        self.a = deque(range(1, n + 1))

    def find(self):
        while len(self.a) > 1:
            self.a.popleft()
            self.a.append(self.a.popleft())
        return self.a[0]

n = int(input())
card = Card(n)
print(card.find())