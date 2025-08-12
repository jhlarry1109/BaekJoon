#include <stdio.h>

long long combination(int m, int n) {
    if (n > m - n) n = m - n;
    long long result = 1;

    for (int i = 1; i <= n; i++) {
        result = result * (m - i + 1) / i;
    }
    return result;
}

int main() {
    int T, N, M;
    scanf("%d", &T);

    while (T--) {
        scanf("%d %d", &N, &M);
        printf("%lld\n", combination(M, N));
    }
    return 0;
}
