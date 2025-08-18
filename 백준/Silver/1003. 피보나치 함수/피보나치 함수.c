#include <stdio.h>

int main() {
    int t,n;
    scanf("%d", &t);
    int cnt0[41], cnt1[41];
    cnt0[0] = 1;
    cnt1[0] = 0;
    cnt0[1] = 0;
    cnt1[1] = 1;

    for(int i=2; i<=40; i++) {
        cnt0[i] = cnt0[i-1] + cnt0[i-2];
        cnt1[i] = cnt1[i-1] + cnt1[i-2];
    }

    for (int i=0; i<t; i++) {
        scanf("%d", &n);
        printf("%d %d\n", cnt0[n], cnt1[n]);
    }
    return 0;
}