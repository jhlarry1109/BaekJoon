#include <stdio.h>

int d(int n) {
    int sum = n;
    while(n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int li[10001] = {0};

    for (int i = 1; i <= 10000; i++) {
        int num = d(i);
        if (num <= 10000) {
            li[num] = 1;
        }
    }

    for (int i = 1; i <= 10000; i++) {
        if (li[i] == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}
