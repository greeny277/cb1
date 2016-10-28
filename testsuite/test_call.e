
int printSomething( int a, int b )
{
	int d;
	
	int e;
	
	e := 65;
	while ( e < (65+26) )
	{
		d := writeChar( e );
		e := e + 1;
	}
	
	return 0;
	
}

int callPrintSomething( int c, int d )
{

	int f;
	int a;
	
	a := 0;
	while ( a < 100 )
	{
		f := printSomething( 3, 5 );
		f := writeChar( 10 );
		a := a + 1;
	}
	return 0;
}

int main()
{

	int a;
	int b;
	int c;

b := 2;

	a := 9;

	c := writeChar( 65 );
	c := writeChar( 10 );
	
	while( a != 5 )
	{
		c := writeChar( a+48 );
		c := writeChar( 10 );
		a := a - 1;
	}

	c := writeChar( 66 );
	c := writeChar( 10 );

	c := callPrintSomething( a, b );
	c := writeChar( 10 );
	
	
	return a;
	
}

