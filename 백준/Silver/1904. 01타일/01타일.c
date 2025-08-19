#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int d[1000001];
    d[1] = 1;
    d[2] = 2;
    for(int i=3; i<=n; i++) {
        d[i] = (d[i-2] + d[i-1])%15746;
    }
    printf("%d", d[n]);
    return 0;
}
