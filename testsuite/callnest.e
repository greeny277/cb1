int f11(int x, int y, int z) {
    return x;
}
int f12(int x, int y, int z) {
    return y;
}
int f13(int x, int y, int z) {
    return z;
}

int f2(int a, int b, int c) {
    return 100*a + 10*b + c;
}

int f3(int a, int b, int c) {
    return 1000000*a + 1000*b + c;
}

int main() {
    int dummy;
    dummy := f3(f2(f11(1, 0, 0), f12(0, 2, 0), f13(0, 0, 3)),
                f2(f11(4, 0, 0), f12(0, 5, 0), f13(0, 0, 6)),
                f2(f11(7, 0, 0), f12(0, 8, 0), f13(0, 0, 9)));
    dummy := writeInt(dummy);
    dummy := writeChar(10);
    return 23;
}