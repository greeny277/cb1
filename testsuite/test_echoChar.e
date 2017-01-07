int main() {
    int d;
    int d2;
    int r;
    d := readChar();
    d2 := writeChar(d);
    if(d = 65) {
        d2 := writeChar(61);
        r := 1;
    } else {
        d2 := writeChar(33);
        r := 0;
    }
    d2 := writeChar(61);
    d2 := writeChar(65);
    d2 := writeChar(10);
    return r;
}
