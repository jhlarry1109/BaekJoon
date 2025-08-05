#include <stdio.h>

int hansu(int n) {
    if (n<100) {
        return 1;
    }
    int a = n/100;
    int b = (n/10)%10;
    int c = n%10;

    return (a-b == b-c);
}

int main() {
    int n, cnt = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        if(hansu(i)) {
            cnt++;
        }
    }

    printf("%d", cnt);
    return 0;
}