#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int score[101];
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &score[i]);
    }

    for (int i = n-2; i >= 0; i--) {
        while (score[i] >= score[i+1]) {
            score[i]--;
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}
