#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    long long fibo[10001] = {0};
    long long p, q;

    for (int i = 1; i <= t; i++) {
        scanf("%lld %lld", &p, &q);

        fibo[1] = 1;
        fibo[2] = 1;

        for (int j = 3; j <= p; j++) {
            fibo[j] = (fibo[j-1] + fibo[j-2]) % q;
        }

        printf("Case #%d: %lld\n", i, fibo[p] % q);
    }

    return 0;
}
