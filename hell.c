#include <stdio.h>

int main() {
    int x = 303578353;
    int y = 24778;
    printf("ERC pairs between %d and %d are:\n", x, y);
    int count = 0;k
    for (int a = 1; a <= x; a++) {
        for (int b = 1; b <= (a < y ? a : y); b++) {
            if (a%b == 0) {
                continue;
            }
            else if (a == (b+1)*(a/b)) {
                count++;
                printf("%d\n", count);
            }
        }
    }
    printf("Total ERC pairs: %d\n", count);
    return 0;
}

