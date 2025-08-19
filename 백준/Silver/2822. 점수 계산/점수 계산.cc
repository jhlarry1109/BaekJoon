#include <stdio.h>

int main() {
    int score[8];
    int idx[8];
    for (int i = 0; i < 8; i++) {
        scanf("%d", &score[i]);
        idx[i] = i + 1;
    }

    for (int i = 0; i < 7; i++) {
        for (int j = i + 1; j < 8; j++) {
            if (score[i] < score[j]) {
                int tmp = score[i];
                score[i] = score[j];
                score[j] = tmp;

                tmp = idx[i];
                idx[i] = idx[j];
                idx[j] = tmp;
            }
        }
    }

    int total = 0;
    int topIdx[5];
    for (int i = 0; i < 5; i++) {
        total += score[i];
        topIdx[i] = idx[i];
    }

    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 5; j++) {
            if (topIdx[i] > topIdx[j]) {
                int tmp = topIdx[i];
                topIdx[i] = topIdx[j];
                topIdx[j] = tmp;
            }
        }
    }

    printf("%d\n", total);
    for (int i = 0; i < 5; i++) {
        printf("%d ", topIdx[i]);
    }
    return 0;
}
