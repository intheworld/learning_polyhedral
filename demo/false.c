float f1(float);
float f2(float);

void f(int n, float A[restrict static n],
        float B[restrict static n])
{
        float t;

        for (int i = 0; i < n; ++i) {
S:              t = f1(A[i]);
T:              B[i] = f2(t);
        }
}