int[12][2] argsave;

int twelveArgs(int a00, int a01, int a02, int a03, int a04, int a05, 
               int a06, int a07, int a08, int a09, int a10, int a11) {
             
    argsave[ 0][0] := a00;
    argsave[ 1][0] := a01;
    argsave[ 2][0] := a02;
    argsave[ 3][0] := a03;
    argsave[ 4][0] := a04;
    argsave[ 5][0] := a05;
    argsave[ 6][0] := a06;
    argsave[ 7][0] := a07;
    argsave[ 8][0] := a08;
    argsave[ 9][0] := a09;
    argsave[10][0] := a10;
    argsave[11][0] := a11; 

    a00 := 131000 +  0;
    a01 := 131000 +  1;
    a02 := 131000 +  2;
    a03 := 131000 +  3;
    a04 := 131000 +  4;
    a05 := 131000 +  5;
    a06 := 131000 +  6;
    a07 := 131000 +  7;
    a08 := 131000 +  8;
    a09 := 131000 +  9;
    a10 := 131000 + 10;
    a11 := 131000 + 11;

    argsave[ 0][1] := a00;
    argsave[ 1][1] := a01;
    argsave[ 2][1] := a02;
    argsave[ 3][1] := a03;
    argsave[ 4][1] := a04;
    argsave[ 5][1] := a05;
    argsave[ 6][1] := a06;
    argsave[ 7][1] := a07;
    argsave[ 8][1] := a08;
    argsave[ 9][1] := a09;
    argsave[10][1] := a10;
    argsave[11][1] := a11;

    return 0;
}

int main() {
    int dummy;
    int i;
    int j;
    i := 0;
    while(i < 12) {
        j := 0; 
        while (j < 2) {
            argsave[i][j] := 0;
            j := j+1;
        }
        i := i+1;
    }
    dummy := twelveArgs(121000 +  0,
    	                121000 +  1,
		                121000 +  2,
		                121000 +  3,
		                121000 +  4,
		                121000 +  5,
		                121000 +  6,
		                121000 +  7,
		                121000 +  8,
		                121000 +  9,
		                121000 + 10,
		                121000 + 11);
    i := 0;
    while(i < 12) {
        j := 0; 
        while (j < 2) {
            dummy := writeInt(argsave[i][j]);
            dummy := writeChar(32);
            j := j+1;
        }
        dummy := writeChar(10);
        i := i+1;
    }
    return 41;
}