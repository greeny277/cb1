

int[ 100 ] arr2;
int rrr;

int x()
{
	   return 5;
}

int y( int a )
{
	return a*2;
}

int main()
{

	int c;
	   int a;
	   int b;
	   
	   a := 0;
	   while ( a < 100 )
	   {
	   	arr2[ a ] := a;
		c := writeInt( a );
		c := writeChar( 45 );
		c := writeInt( arr2[a] );
		c := writeChar( 10 );
		a := a + 1;
	   }

	   
   		c := writeChar( 45 );
		c := writeChar( 45 );
		c := writeChar( 45 );
		c := writeChar( 45 );
		c := writeChar( 45 );
		c := writeChar( 10 );

			   
	   a := 0;
	   while ( a < 100 )
	   {
		c := writeInt( arr2[ a ] );
		c := writeChar( 10 );
		a := a + 1;
	   }

rrr := 25;
c := writeInt( rrr );
c := writeChar( 10 );
		
	   return 0;
	   
}

