float inner(int n, float A[], float B[]) {
        float prod;
S:      prod = 0;
L:      for (int i = 0; i < n; i++)
T:          prod += A[i] * B[i];
        return prod;
}