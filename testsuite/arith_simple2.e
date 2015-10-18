
int opt1(int x) {
    return 2*x; // shift
}

int opt1a(int x) {
    return x*2; // shift
}

int opt2(int x) {
    return x+1; // inc
}

int opt3(int x) {
    return x / 2; // shift
}

int opt4(int x) {
    return x / 16; // shift
}

int opt5(int x) {
    return x * 16; // shift
}

int opt6(int x) {
    return 5*x; // lea
}

int opt7(int x) {
    return 10*x; // lea + shift - or is imul faster?
}

int opt8(int x) {
    return x-1; // dec
}

int opt9(int x) {
    return 0-x; // neg
}

int sz;
int[10000000] work;

int reset() {
    int x;
    x := 0;
    while(x < sz) {
        work[x] := x;
        x := x+1;
    }
    return 0;
}

int run() {
   int i;
   i := 0;
   while(i < sz) {
       int tmp;
       int tmp1;
       int tmp1a;
       int tmp2;
       int tmp3;
       int tmp4;
       int tmp5;
       int tmp6;
       int tmp7;
       int tmp8;
       int tmp9;
       tmp := work[i];
       tmp1  := opt1(tmp);
       tmp1a := opt1a(tmp);
       tmp2  := opt2(tmp);
       tmp3  := opt3(tmp);
       tmp4  := opt4(tmp);
       tmp5  := opt5(tmp);
       tmp6  := opt6(tmp);
       tmp7  := opt7(tmp);
       tmp8  := opt8(tmp);
       tmp9  := opt9(tmp);
       tmp := tmp1 + tmp2 + tmp3 + tmp4 + tmp5 + tmp6 + tmp7 + tmp8 + tmp9 + tmp1a;
       work[i] := tmp;
       i := i + 1;
   }
   return 0;
}

int mod(int xx) {
     int y;
     y := xx  / 1073741824 ;
     return xx - y * 1073741824;
}

int main() {
   int i;
   int dummy;
   int stime;
   int xx;
   int printtime;
   printtime := 0;
   sz := 10000000;

   stime := time();
   dummy := reset();
   stime := time() - stime;
   if(printtime = 1) {
       dummy:=writeChar(62);
       dummy:=writeChar(62);
       dummy:=writeChar(32);
       dummy := writeInt(stime);
       dummy:=writeChar(109);
       dummy:=writeChar(115);
       dummy := writeChar(10);
   }

   stime := time();
   dummy := run();
   stime := time() - stime;
   if(printtime = 1) {
       dummy:=writeChar(62);
       dummy:=writeChar(62);
       dummy:=writeChar(32);
       dummy := writeInt(stime);
       dummy:=writeChar(109);
       dummy:=writeChar(115);
       dummy := writeChar(10);
   }

   stime := time();
   i := 0;
   xx := 0;
   while(i < sz) { // output loop s.th. gcc doesn't throw everything away
       xx := mod(xx + work[i]);
       i := i+1;
   }
   stime := time() - stime;
   if(printtime = 1) {
       dummy:=writeChar(62);
       dummy:=writeChar(62);
       dummy:=writeChar(32);
       dummy := writeInt(stime);
       dummy:=writeChar(109);
       dummy:=writeChar(115);
       dummy := writeChar(10);
   }

   dummy := writeInt(xx);
   dummy := writeChar(10);
   return 0;
}