int srclen;
int[10000] src;
int[10000] jmp;
int[10000] data;

int searchEnd(int x) {
     int cnt;
     cnt := 0;
     while(x < srclen) {
         if(src[x] = 91) {
             cnt := cnt + 1;
         }
         if(src[x] = 93) {
             if(cnt = 0) {
                 return x;
             } else {
                 cnt := cnt - 1;
             }
         }
         x := x + 1;
     }
     cnt := exit(12);
     return 0;
}

int readInput() {
    int inch;
    srclen := 0;
    inch := readChar();
    while(inch != 11 && inch != 0 && inch != 0-1) { // ascii vertical tab
        if(srclen >= 10000) {
            inch := exit(11);
        }
        src[srclen] := inch;
        srclen := srclen + 1;
        inch := readChar();
    }
    inch := 0;
    while(inch != srclen) {
       if(src[inch] = 91) {
           int other;
           other := searchEnd(inch+1);
           jmp[other] := inch;
           jmp[inch] := other;
       }
       inch := inch + 1;
    }
    return 0;
}

int run() {
    int ip;
    int dp;
    ip := 0;
    dp := 0;
    while(ip < srclen) {
        int ins;
        ins := src[ip];
        if         (ins = 46) { // .
            int dummy;
            dummy := writeChar(data[dp]);
            ip := ip + 1;
        } else { if(ins = 44) { // ,
            data[dp] := readChar();
            ip := ip + 1;
        } else { if(ins = 60) { // <
            dp := dp - 1;
            if(dp < 0) { dp := 10000-1; }
            ip := ip + 1;
        } else { if(ins = 62) { // >
            dp := dp + 1;
            if(dp = 10000) { dp := 0; }
            ip := ip + 1;
        } else { if(ins = 43) { // +
            int tmp;
            tmp := data[dp] + 1;
            if(tmp = 256) {
                data[dp] := 0;
            } else {
                data[dp] := tmp;
            }
            ip := ip + 1;
        } else { if(ins = 45) { // -
            int tmp;
            tmp := data[dp] - 1;
            if(tmp = 0-1) {
                data[dp] := 255;
            } else {
                data[dp] := tmp;
            }
            ip := ip + 1;
        } else { if(ins = 91) { // [
            if(data[dp] = 0) {
               ip := jmp[ip] + 1;
            } else {
               ip := ip + 1;
            }
        } else { if(ins = 93) { // ]
            ip := jmp[ip];
        } else { ip := ip + 1;
        }}}}}}}}
    }
    return 0;
}

int main() {
     int dummy;
     dummy := readInput();
     dummy := run();
     return 0;
}
