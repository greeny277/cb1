int cnt;


int h1(int p0, int p1, int p2, int p3, int p4, int p5, int p6, int p7) {
    int dummy;
    
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeInt(p4); dummy := writeChar(32);
    dummy := writeInt(p5); dummy := writeChar(32);
    dummy := writeInt(p6); dummy := writeChar(32);
    dummy := writeInt(p7); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 34) { cnt := cnt + 1; dummy := h1(p1, p2, p3, p4, p5, p6, p7, p0);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeInt(p4); dummy := writeChar(32);
    dummy := writeInt(p5); dummy := writeChar(32);
    dummy := writeInt(p6); dummy := writeChar(32);
    dummy := writeInt(p7); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int main() {
    int dummy;
    cnt := 0;
    dummy := h1(1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700);
    dummy := writeChar(10);
    return 0;
}

