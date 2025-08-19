#include <stdio.h>

int main() {
    int n;
    int a[301];
    int d[301];
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        scanf("%d", &a[i]);
    }
    d[0] = 0;
    d[1] = a[1];
    d[2] = a[1] + a[2];
    for(int i=3; i<=n; i++) {
        d[i] = d[i-3] + a[i-1] + a[i] > d[i-2] + a[i] ? d[i-3] + a[i-1] + a[i] : d[i-2] + a[i];
    }
    printf("%d", d[n]);
    return 0;
}
