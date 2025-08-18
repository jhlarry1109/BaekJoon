#include <stdio.h>

int main() {
    int n,k;
    scanf("%d %d", &n, &k);

    int li[10];
    for (int i = 0; i < n; i++) {
        scanf("%d", &li[i]);
    }

    int count = 0;
    for (int i = n-1; i >= 0; i--) {
        if (k == 0) break;
        if (li[i] <= k) {
            count += k / li[i];
            k %= li[i];
        }
    }

    printf("%d\n", count);
    return 0;
}
