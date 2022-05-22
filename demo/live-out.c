int f(int);

void g(int n, int A[const restrict static n])
{
#pragma scop
S:      A[f(0)] = 1;
T:      A[0] = 0;
#pragma endscop
}