int x;
int[10] y;
int z;
int[10] y2;
int z2;

int test1() {
    int dummy;
    x := 1717986918;
    z := 1061109567;
    z2 := 1717986918;
    y[0] := 0-1;
    y[9] := 0-1;
    y2[0] := 0-1;
    y2[9] := 0-1;
    dummy := writeInt(x);
    dummy := writeChar(32);
    dummy := writeInt(y[0]);
    dummy := writeChar(32);
    dummy := writeInt(y[9]);
    dummy := writeChar(32);
    dummy := writeInt(z);
    dummy := writeChar(32);
    dummy := writeInt(y2[0]);
    dummy := writeChar(32);
    dummy := writeInt(y2[9]);
    dummy := writeChar(32);
    dummy := writeInt(z2);
    dummy := writeChar(10);
    return 0;
}

int test2child(int par1, int par2) {
    int pre;
    int[131] a1;
    int inter;
    int[7][13] a2;
    int post;
    int i;
    int j;
    par1 := 1195853639; //* 0x47474747 */
    par2 := 421075225;  //* 0x19191919 */
    pre := 1701143909; // 0x65656565  
    inter := 1448498774;  // 0x56565656
    post := 1701143909; // 0x65656565 

    i := 0; while (i < 131) {
      a1[i] := 656877351 + i; // 0x27272727
    i := i+1; }

    i := writeInt(pre);
    i := writeChar(32);
    i := writeInt(a1[0]);
    i := writeChar(32);
    i := writeInt(a1[130]);
    i := writeChar(32);
    i := writeInt(inter);
    i := writeChar(10);
    
    i := 0; while (i < 7) {
        j := 0; while (j < 13) {
            a2[i][j] := 33686018  + i * 13 + j; // 0x02020202
        j := j+1; }
    i := i+1; }

    i := writeInt(pre);
    i := writeChar(32);
    i := writeInt(a1[0]);
    i := writeChar(32);
    i := writeInt(a1[130]);
    i := writeChar(32);
    i := writeInt(inter);
    i := writeChar(10);

    i := writeInt(inter);
    i := writeChar(32);
    i := writeInt(a2[0][0]);
    i := writeChar(32);
    i := writeInt(a2[6][0]);
    i := writeChar(32);
    i := writeInt(a2[0][12]);
    i := writeChar(32);
    i := writeInt(a2[6][12]);
    i := writeChar(32);
    i := writeInt(post);
    i := writeChar(10);

    return 875836468; // 0x34343434
}

int test2() {
    int pre;
    int[131] a1;
    int inter;
    int[7][13] a2;
    int post;
    int i;
    int j;
    pre := 1717986918; // 0x66666666
    inter := 1061109567; // 0x3f3f3f3f
    post := 1717986918; // 0x66666666

    i := 0; while (i < 131) {
      a1[i] := 808464432; // 0x30303030
    i := i+1; }

    i := writeInt(pre);
    i := writeChar(32);
    i := writeInt(a1[0]);
    i := writeChar(32);
    i := writeInt(a1[130]);
    i := writeChar(32);
    i := writeInt(inter);
    i := writeChar(10);
    
    i := 0; while (i < 7) {
        j := 0; while (j < 13) {
            a2[i][j] := 1347440720; // 0x50505050
        j := j+1; }
    i := i+1; }

    i := writeInt(pre);
    i := writeChar(32);
    i := writeInt(a1[0]);
    i := writeChar(32);
    i := writeInt(a1[130]);
    i := writeChar(32);
    i := writeInt(inter);
    i := writeChar(10);

    i := writeInt(inter);
    i := writeChar(32);
    i := writeInt(a2[0][0]);
    i := writeChar(32);
    i := writeInt(a2[6][0]);
    i := writeChar(32);
    i := writeInt(a2[0][12]);
    i := writeChar(32);
    i := writeInt(a2[6][12]);
    i := writeChar(32);
    i := writeInt(post);
    i := writeChar(10);

    i := test2child(555819297, 303174162); // 0x21212121, 0x12121212

    i := writeInt(pre);
    i := writeChar(32);
    i := writeInt(a1[0]);
    i := writeChar(32);
    i := writeInt(a1[130]);
    i := writeChar(32);
    i := writeInt(inter);
    i := writeChar(10);

    i := writeInt(inter);
    i := writeChar(32);
    i := writeInt(a2[0][0]);
    i := writeChar(32);
    i := writeInt(a2[6][0]);
    i := writeChar(32);
    i := writeInt(a2[0][12]);
    i := writeChar(32);
    i := writeInt(a2[6][12]);
    i := writeChar(32);
    i := writeInt(post);
    i := writeChar(10);
    return 1;
}

int main() {
    int dummy;
    dummy := test1();
    dummy := test2();
    return 0;
}