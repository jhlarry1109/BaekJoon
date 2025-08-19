#include <stdio.h>

int main() {
    int n;
    long long d[91];
    d[1] = 1;
    d[2] = 1;
    scanf("%d", &n);
    for(int i=3; i<=n; i++) {
        d[i] = d[i-1] + d[i-2];
    }
    printf("%lld", d[n]);
    return 0;
}
