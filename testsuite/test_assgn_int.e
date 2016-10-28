
int x()
{
	   return 5;
}

int y( int a )
{
	return a*2;
}

int globctr;

int writeA(int a) {
    int d;
    d := writeChar(97); // 'a'
    d := d + writeChar(58); // ':'
    //d := writeInt(globctr); // xx
    //d := d + writeChar(58); // ':'
    d := d + writeChar(32); // ' '
    d := d + writeInt(a);
    d := d + writeChar(10); // '\n'
    globctr := globctr + 1;
    return d;
}

int dummy()
{
	int a;
	int b;
    a := 0;             b := writeA(a);
	a := 1+1;           b := writeA(a);
	a := (4*2)+5;       b := writeA(a);
	a := a+2;           b := writeA(a);
	a := 2+a;           b := writeA(a);
	a := (a*2)+5;       b := writeA(a);
	a := x();           b := writeA(a);
	a := x()*2;         b := writeA(a);
	a := y(1)*2;        b := writeA(a);
	b := 0;
	return 2+4;
}

int dummt_2()
{
	   int a;
       int xx;
	   int[ 100+2 ] arr;
       int yy;
	   int b;
       b := 0;       

       yy := 3773773;
       xx := 3773773;
       arr[0] := 12;
       arr[101] := 12;

	   a := 1 + 2;      b := b + writeA(a);
	   a := 2 + 1;      b := b + writeA(a);
	   arr[24] := 24;   b := b + writeA(arr[24]);
	   arr[25] := 25;   b := b + writeA(arr[25]);
	   arr[25] := 3;    b := b + writeA(arr[25]);
	   arr[26] := 3;    b := b + writeA(arr[26]);
       b := b + writeA(arr[24]);
       b := b + writeA(arr[25]);
       b := b + writeA(arr[26]);

       b := b + writeA(xx);
       b := b + writeA(yy);
       b := b + writeA(arr[0]);
       b := b + writeA(arr[101]);
       return b;
}

int main()
{
	int[ 100 ] arr;
	int a;
	int b;
    
    a := dummy();
    b := writeA(a);
    a := dummt_2();
    b := writeA(a);
    b := writeA(b);

	a := 5;
	b := 3;
    
	return a+b;
}

