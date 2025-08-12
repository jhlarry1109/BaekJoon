#include <stdio.h>

int main() {
    long long fibo[117] = {0};
    fibo[1] = 1;
    fibo[2] = 1;
    fibo[3] = 1;
    for(int i=4; i<= 116; i++) {
        fibo[i] = fibo[i-1] + fibo[i-3];
    }
    
    int n;
    scanf("%d", &n);

    printf("%lld", fibo[n]);
    
    return 0;
}
