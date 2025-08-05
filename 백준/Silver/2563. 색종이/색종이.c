#include <stdio.h>

int main() {
    int paper[100][100] = {0};
    int n, x, y;
    int ans = 0;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x, &y);
        for (int row = y; row < y + 10; row++) {
            for (int col = x; col < x + 10; col++) {
                paper[row][col] = 1;
            }
        }
    }

    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            if (paper[i][j] == 1) {
                ans++;
            }
        }
    }

    printf("%d\n", ans);
    return 0;
}
