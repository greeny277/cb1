
int tester( int arg0, int arg1 )
{
	if ( arg0 >= arg1 )	{
		return 1;
	} else {
		return 0;
	}
}

int wt( int arg0 )
{
	int b;
	while( arg0 >= 0 ) {
		b := writeInt( arg0 );
		b := writeChar( 10 );
		arg0 := arg0 - 1;
	}
	return 0;
}

int main()
{
	int a;


	a := writeInt( 123456 );
	a := writeChar( 10 );

	a := 4+4;
	a := writeInt( a );
	a := writeChar( 10 );

	a := 4*4;
	a := writeInt( a );
	a := writeChar( 10 );

	a := 4-2;
	a := writeInt( a );
	a := writeChar( 10 );

	a := 8/4;
	a := writeInt( a );
	a := writeChar( 10 );

	a := writeChar( 45 );
	a := writeChar( 10 );

	a := writeInt( tester( 5, 4 ) );
	a := writeChar( 10 );

	a := writeInt( tester( 4, 5 ) );
	a := writeChar( 10 );

	a := writeChar( 45 );
	a := writeChar( 45 );
	a := writeChar( 45 );
	a := writeChar( 10 );

	a := wt( 5 );

	return a;
}

