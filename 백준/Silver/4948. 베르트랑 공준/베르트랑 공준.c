#include <stdio.h>

int main() {
    int li[1000000] = {0};
    for (int i=2; i<=123456; i++) {
        if (li[i] == 0) {
            for(int j=i*2; j<=123456*2; j+=i) {
                li[j] = 1;
            }
        }
    }
    int a;
    int cnt;
    while(1) {
        cnt = 0;
        scanf("%d", &a);
        if (a==0) {
            break;
        }
        for(int i=a+1; i<=a*2; i++) {
            if(li[i] == 0) {
                cnt++;
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}