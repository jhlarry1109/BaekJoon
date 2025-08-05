#include <stdio.h>

int main() {
    int t;
    int a;
    scanf("%d", &t);
    int li[1001];
    li[0] = 1;
    li[1] = 1;
    li[2] = 2;
    for(int i=0; i<t; i++) {
        scanf("%d", &a);
        for (int j=3; j<=a; j++) {
            li[j] = li[j-3] + li[j-2] + li[j-1];
        }
        printf("%d\n", li[a]);
    }
    return 0;
}