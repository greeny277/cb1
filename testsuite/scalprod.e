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
    a[0] := 3;
    a[1] := 3;
    a[2] := 3;
    b[0] := 3;
    b[1] := 3;
    b[2] := 3;
    dim := 7;
    dummy := writeInt(skalarprod());
    dummy := writeChar(10);
    b[0] := 0;
    b[1] := 0;
    b[2] := 0;
    b[3] := 3;
    b[4] := 3;
    b[5] := 3;
    dummy := writeInt(skalarprod());
    dummy := writeChar(10);
    return 0;
}
