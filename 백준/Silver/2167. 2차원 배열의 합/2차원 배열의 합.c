#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int arr[301][301] = {0};
    long long prefix[301][301] = {0};

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%d", &arr[i][j]);
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] 
                         - prefix[i-1][j-1] + arr[i][j];
        }
    }

    int k;
    scanf("%d", &k);

    while (k--) {
        int i, j, x, y;
        scanf("%d %d %d %d", &i, &j, &x, &y);
        long long result = prefix[x][y] - prefix[i-1][y] 
                         - prefix[x][j-1] + prefix[i-1][j-1];
        printf("%lld\n", result);
    }

    return 0;
}
