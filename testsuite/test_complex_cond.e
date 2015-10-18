	int a;
	int b;
	int c;
	int d;
	int e;
	int f;
	int g;
	int h;

int mod2(int n) {
    return n - ((n/2)*2);
}

int cond1() {
   if(     ( (a=1 && b=1) || (c=1 && d=1) ) 
        && ( (e=1 || f=1) && (g=1 || h=1) ) ){
        return 1;
    } else {
        return 0;
    }
}

int cond2() {
   if(     a=1 && b=1 && c=1 ){
        return 1;
    } else {
        return 0;
    }
}

int cond3() {
   if(     a=1 || b=1 || c=1 ){
        return 1;
    } else {
        return 0;
    }
}

int cond4() {
   if(     a=1 && b=1 || c=1 ){
        return 1;
    } else {
        return 0;
    }
}

int cond5() {
   if(     a=1 || b=1 && c=1 ){
        return 1;
    } else {
        return 0;
    }
}

int cond6() {
   if( (a=1 && b=1) || (c=1 && d=1) ){
        return 1;
    } else {
        return 0;
    }
}

int cond7() {
   if( (e=1 || f=1) && (g=1 || h=1) ){
        return 1;
    } else {
        return 0;
    }
}

int check(int n) {

    int x;
    x:=writeInt(n);
    x:=writeChar(32);
    a := mod2(n); n := n / 2; x:=writeInt(a);
    b := mod2(n); n := n / 2; x:=writeInt(b);
    c := mod2(n); n := n / 2; x:=writeInt(c);
    d := mod2(n); n := n / 2; x:=writeInt(d);
    e := mod2(n); n := n / 2; x:=writeInt(e);
    f := mod2(n); n := n / 2; x:=writeInt(f);
    g := mod2(n); n := n / 2; x:=writeInt(g);
    h := mod2(n); n := n / 2; x:=writeInt(h);

    x:=writeChar(32);
    x:=writeInt(cond1());
    x:=writeChar(32);
    x:=writeInt(cond2());
    x:=writeChar(32);
    x:=writeInt(cond3());
    x:=writeChar(32);
    x:=writeInt(cond4());
    x:=writeChar(32);
    x:=writeInt(cond5());
    x:=writeChar(32);
    x:=writeInt(cond6());
    x:=writeChar(32);
    x:=writeInt(cond7());
    x:=writeChar(10);
    return 0;
}


int main()
{
    int n;
    int dummy;
    n := 0;
    while(n <= 255) {
        dummy := check(n);
        n := n+1;
    }
    return 0;
}
	
