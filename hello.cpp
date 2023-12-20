#include <math.h>
#include <stdio.h>

double b (int n) {
  double l = lgamma (365.0 + 1.0) - (double)n * log (365.0) - lgamma (365.0 - (double)n + 1.0);
  return exp (l);
}

int main () {
  int n = 1;
  double p = 0;
  while (p <= 0.65) {
    p = 1 - b(n);
    n++;
  }
  printf ("Number of people: %d\n", n);
  return 0;
}
