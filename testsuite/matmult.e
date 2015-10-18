int[200][200] A;
int[200][200] B;
int[200][200] C;

int dim;

int matmult() {
    int i;
    int j;
    int k;
    i := 0;
    while(i < dim) {
        j := 0;
        while(j < dim) {
            C[i][j] := 0;
            k := 0;
            while (k < dim) {
                C[i][j] := C[i][j] + A[i][k] * B[k][j];
                k := k + 1;
            }
            j := j + 1;
        }
        i := i + 1;
    }
    return 0;
}

int main() {
    int dummy;
    dim := 200;
    dummy := matmult();
    return 0;
}
