int tc;
int nev;

int f(int x) {
    nev := nev + 1;
    return x;
}

int printnev(int a, int b, int c, int ret) {
    int dummy;
    dummy := writeInt(tc);
    dummy := writeChar(58);
    dummy := writeChar(32);
    dummy := writeInt(a);
    dummy := writeChar(32);
    dummy := writeInt(b);
    dummy := writeChar(32);
    dummy := writeInt(c);
    dummy := writeChar(58);
    dummy := writeChar(32);
    dummy := writeInt(nev);
    dummy := writeChar(58);
    dummy := writeChar(32);
    dummy := writeInt(ret);
    dummy := writeChar(10);
    nev := 0;
    tc := tc + 1;
    return 0;
}

int and1(int a, int b) {
   if(f(a) = 1 && f(b) = 1) {
        return 1;
   }
   return 0;
}

int or1(int a, int b) {
   if(f(a) = 1 || f(b) = 1) {
        return 1;
   }
   return 0;
}

int andand1(int a, int b, int c) {
   if((f(a) = 1 && f(b) = 1) && f(c) = 1) {
        return 1;
   }
   return 0;
}

int andand2(int a, int b, int c) {
   if(f(a) = 1 && (f(b) = 1 && f(c) = 1)) {
        return 1;
   }
   return 0;
}

int oror1(int a, int b, int c) {
   if((f(a) = 1 || f(b) = 1) || f(c) = 1) {
        return 1;
   }
   return 0;
}

int oror2(int a, int b, int c) {
   if(f(a) = 1 || (f(b) = 1 || f(c) = 1)) {
        return 1;
   }
   return 0;
}

int andor1(int a, int b, int c) {
   if((f(a) = 1 && f(b) = 1) || f(c) = 1) {
        return 1;
   }
   return 0;
}

int andor2(int a, int b, int c) {
   if(f(a) = 1 && (f(b) = 1 || f(c) = 1)) {
        return 1;
   }
   return 0;
}

int orand1(int a, int b, int c) {
   if((f(a) = 1 || f(b) = 1) && f(c) = 1) {
        return 1;
   }
   return 0;
}

int orand2(int a, int b, int c) {
   if(f(a) = 1 || (f(b) = 1 && f(c) = 1)) {
        return 1;
   }
   return 0;
}


int doTest(int a, int b, int c) {
    int dummy;
    dummy := printnev(a, b, c, and1(a, b));
    dummy := printnev(a, b, c, or1(a, b));
    dummy := printnev(a, b, c, andand1(a, b, c));
    dummy := printnev(a, b, c, andand2(a, b, c));
    dummy := printnev(a, b, c, oror1(a, b, c));
    dummy := printnev(a, b, c, oror2(a, b, c));
    dummy := printnev(a, b, c, andor1(a, b, c));
    dummy := printnev(a, b, c, andor2(a, b, c));
    dummy := printnev(a, b, c, orand1(a, b, c));
    dummy := printnev(a, b, c, orand2(a, b, c));
    return 0;
}

int main() {
    int ninp;
    int i;
    nev := 0;
    tc := 0;
    i := 0;
    ninp := readInt();
    while(i < ninp) {
        int a;
        int b;
        int c;
        int dummy;
        a := readInt();
        b := readInt();
        c := readInt();
        dummy := doTest(a, b, c);
        i := i + 1;
    }
    return 0;
}