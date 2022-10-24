#include "omp.h"
#include <stdio.h>
#include "stdlib.h"
#include "iostream"
using namespace std;

int main()
{

int sum=0;
int a[2] = {1, 9};
int b[2] = {2, 3};
int i, N = 2;
#pragma omp parallel for reduction(+:sum)
for (i=0; i < N; i++)
{
sum = sum + (a[i]*b[i]);
}

return sum;
}
