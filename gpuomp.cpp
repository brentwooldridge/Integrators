#include "omp.h"
#include <stdio.h>
#include "stdlib.h"






#define N 1200
int main(){
int i;
#pragma omp parallel private (i)
{
#pragma omp for schedule (static,2) ordered
for( i= 0; i<=N; i++){
#pragma omp ordered
#pragma omp target map(tofrom:i)
{ printf("Threads %d i= %d\n", omp_get_num_threads(),i); }
}
}
}
