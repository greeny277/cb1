int[1000][1000] A;
int[1000][1000] B;
int[1000][1000] C;

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
    int i;
    int j;

    dim := readInt();

    // read A
    i := 0;
    while(i < dim) {
        j := 0;
        while(j < dim) {
            A[i][j] := readInt();
            j := j + 1;
        }
        i := i + 1;
    }

    // read B
    i := 0;
    while(i < dim) {
        j := 0;
        while(j < dim) {
            B[i][j] := readInt();
            j := j + 1;
        }
        i := i + 1;
    }
    
    dummy := matmult();

    // write C
    i := 0;
    while(i < dim) {
        j := 0;
        while(j < dim) {
            dummy := writeInt(C[i][j]);
            dummy := writeChar(32);
            j := j + 1;
        }
        dummy := writeChar(10);
        i := i + 1;
    }

    return 0;
}
