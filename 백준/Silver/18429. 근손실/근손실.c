#include <stdio.h>

int n, k;
int kit[8];
int visited[8];
int count = 0;

void dfs(int day, int weight) {
    if (day == n) {
        count++;
        return;
    }
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            int next = weight + kit[i] - k;
            if (next >= 500) {
                visited[i] = 1;
                dfs(day + 1, next);
                visited[i] = 0;
            }
        }
    }
}

int main() {
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &kit[i]);
    }
    dfs(0, 500);
    printf("%d\n", count);
    return 0;
}
