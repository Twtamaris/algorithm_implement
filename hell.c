#include <stdio.h>

int sum_of_digits(long long int num) {
    int sum = 0;
    while (num != 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int contains_zero(long long int num) {
    while (num != 0) {
        if (num % 10 == 0) {
            return 1;
        }
        num /= 10;
    }
    return 0;
}

void calculate(int total_sum, long long int calculation) {
    int count = 0;
    for (long long int i = 1; i <= calculation; i++) {
        if (contains_zero(i)) {
            continue;
        }
        if (sum_of_digits(i) == total_sum) {
            count++;
            printf("%d\n", count);
        
        }
    }
    printf("%d\n", count);
}

int main() {
    calculate(32, 111111111111);
    return 0;
}
