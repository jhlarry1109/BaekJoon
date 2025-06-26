class Matrix:
    def __init__(self, data):
        self.data = [row[:] for row in data]
        self.n = len(data)
        self.m = len(data[0])

    def matmul(self, other):
        return Matrix([
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.m)) for j in range(other.m)]
            for i in range(self.n)
        ])

    def scalar_mul(self, k):
        return Matrix([[x * k for x in row] for row in self.data])

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(self.n)] for i in range(self.m)])

    def minor(self, i, j):
        return Matrix([
            [self.data[r][c] for c in range(self.m) if c != j]
            for r in range(self.n) if r != i
        ])

    def determinant(self):
        if self.n == 1:
            return self.data[0][0]
        if self.n == 2:
            a, b = self.data[0]
            c, d = self.data[1]
            return a * d - b * c
        return sum(((-1) ** j) * self.data[0][j] * self.minor(0, j).determinant()
                   for j in range(self.m))

    def cofactor(self):
        return Matrix([
            [((-1) ** (i + j)) * self.minor(i, j).determinant()
             for j in range(self.m)]
            for i in range(self.n)
        ])

    def adjugate(self):
        return self.cofactor().transpose()

    def inverse(self):
        det = self.determinant()
        return self.adjugate().scalar_mul(1 / det)


n = int(input())
A_data = []
b_data = []

for _ in range(n):
    row = list(map(int, input().split()))
    A_data.append(row[:-1])
    b_data.append([row[-1]])

A = Matrix(A_data)
b = Matrix(b_data)

x = A.inverse().matmul(b)

for row in x.data:
    print(round(row[0]), end=' ')
