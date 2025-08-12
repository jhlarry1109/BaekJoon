 #include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long fibo[1000001] = {0};
    fibo[0] = 0;
    fibo[1] = 1;

    for (int i = 2; i <= n; i++) {
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000007;
    }

    printf("%lld", fibo[n]);
    return 0;
}
