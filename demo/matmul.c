void matmul(int M, int N, int K,
    float A[restrict static M][K],
    float B[restrict static K][N],
    float C[restrict static M][N])
{
#pragma scop
    for (int i = 0; i < M; ++i)
        for (int j = 0; j < N; ++j) {
I:          C[i][j] = 0;
            for (int k = 0; k < K; ++k)
U:              C[i][j] = C[i][j] + A[i][k] * B[k][j];
        }
#pragma endscop
}