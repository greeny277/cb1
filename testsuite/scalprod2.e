int[10] a;
int[10] b;

int dim;

int skalarprod() {
    int sum;
    int i;
    sum := 0;
    i := 0;
    while(i < dim) {
        sum := sum + a[i] * b[i];
        i := i + 1;
    }
    return sum;
}

int main() {
    int dummy;
    dim := readInt();
    dummy := 0;
    while(dummy < dim) {
        a[dummy] := readInt();
        dummy := dummy + 1;
    }
    dummy := 0;
    while(dummy < dim) {
        b[dummy] := readInt();
        dummy := dummy + 1;
    }
    dummy := writeInt(skalarprod());
    dummy := writeChar(10);
    return 0;
}
