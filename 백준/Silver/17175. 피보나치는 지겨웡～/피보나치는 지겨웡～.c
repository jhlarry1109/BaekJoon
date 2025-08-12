#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    long long count[51] = {0};
    count[0] = 1;
    count[1] = 1;

    for (int i = 2; i <= n; i++) {
        count[i] = (count[i-1] + count[i-2] + 1) % 1000000007;
    }

    printf("%lld\n", count[n]);
    return 0;
}
