#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int li[1001];
    li[1] = 1;
    li[2] = 3;
    for(int i=3; i<=n; i++) {
        li[i] = (li[i-2]*2 + li[i-1])%10007;
    }
    printf("%d", li[n]);
    return 0;
}