
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
       tmp := work[i];
       tmp := opt1(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt1a(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt2(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt3(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt4(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt5(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt6(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt7(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt8(tmp);
       work[i] := tmp;
       i := i+1;
   }
   i := 0;
   while(i < sz) {
       int tmp;
       tmp := work[i];
       tmp := opt9(tmp);
       work[i] := tmp;
       i := i+1;
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