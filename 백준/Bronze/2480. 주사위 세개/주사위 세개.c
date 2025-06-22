#include <stdio.h>

int main() {
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    if(a == b && b == c) {
        printf("%d", 10000+a*1000);
    }
    else if(a==b || b==c) {
        printf("%d", 1000+b*100);
    }
    else if(b==c || a==c) {
        printf("%d", 1000+c*100);
    }
    else {
        printf("%d", (a > b) ? ((a > c) ? a*100:c*100) : ((b > c) ? b*100:c*100));
    }
    return 0;
}