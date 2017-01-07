
int x()
{
	   return 5;
}

int y( int a )
{
	return a*2;
}

real fr( real r )
{
	return r;
}

int dummy()
{
	int a;
	int b;
	real r;
	   a := 0;
	   a := 1+1;
	   a := (4*2)+5;
	   a := a+2;
	   a := 2+a;
	   a := (a*2)+5;
	   a := x();
	   a := x()*2;
	   a := y(1)*2;
	   b := 0;
	   r := 0;
	   r := 0.5;
	   r := 1+r;
	   r := 1.0+r;
	   r := r+2.0;
	   r := r+r;
	return 2+4;

}

int dummt_2()
{
	   int[ 100+2 ] arr;
	   real[ 100+1000 ] arrr;
	   int a;
	   int b;
	   real r;

	   a := 1 + 1.0;
	   a := 1.0 + 1;
	   r := 1.0 + 1;
	   r := 1 + 1.0;
	   a := a + 1.0;
	   r := r + 1;
	   r := fr( 1.0 );
	   arr[ 25 ] := 25;
	   arrr[ 25 ] := 3.0;
	   arrr[ 26 ] := 3;
	return r+2.0;
}

int main()
{

	   int[ 100 ] arr;
	   real[ 100 ] arrr;
	   int a;
	   int b;
	   real r;

	a := 5;
	b := 3;
	r := 12;
	r := a + b + r;
	r := r;
	return r;

}

