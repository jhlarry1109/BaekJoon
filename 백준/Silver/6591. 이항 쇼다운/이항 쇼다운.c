#include <stdio.h>

long long com(int n, int r) {
    if (r > n/2) {
        r = n-r;
    }
    long long ans = 1;
    for (int i=1; i<=r; i++) {
        ans = ans*(n-r+i)/i;
    }
    return ans;
}

int main() {
    int a,b;
    while(1) {
        scanf("%d %d", &a, &b);
        if (a==0 && b==0) {
            break;
        }
        printf("%lld\n", com(a,b));
    }
    return 0;
}