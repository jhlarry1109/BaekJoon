#include <stdio.h>

int main() {
    int a,b;
    int temp;
    scanf("%d %d", &a, &b);
    int x = a;
    int y = b;
    while (b != 0) {
        temp = a;
        a = b;
        b = temp%b;
    }
    printf("%lld", (long long)x*y/a);
    return 0;
}