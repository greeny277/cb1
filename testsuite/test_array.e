
int test1()
{
	int f;
	int[ 10 ] arr;
	   int g;
	   int a;
	   int b;
	   int i;
	   
	   f := 25;
	   g := 125;

	   	   	b := writeInt( f );
	   	b := writeChar( 10 );
	   	b := writeInt( g );
	   	b := writeChar( 10 );
	   
	   i := 0;
	   while ( i < 10 )
	   {
	   	b := writeInt( i );
	   	b := writeChar( 10 );
	   	arr[ i ] := 10-i;
		i := i + 1;
	   }
	   i := 0;
	   while ( i < 10 )
	   {
	   	b := writeInt( arr[i] );
		b := writeChar( 10 );
		i := i + 1;
	   }

	   	   	b := writeInt( f );
	   	b := writeChar( 10 );
	   	b := writeInt( g );
	   	b := writeChar( 10 );

	   
	   return 0;
}

int test3()
{
	int a;
	int[10] arr;
	int b;
	
	arr[0] := 1;
	b := writeInt( arr[0] ); b := writeChar( 10 );
	arr[1] := 2;
	b := writeInt( arr[1] ); b := writeChar( 10 );
	arr[2] := 3;
	b := writeInt( 3 ); b := writeChar( 10 );
	arr[3] := 4;
	b := writeInt( 4 ); b := writeChar( 10 );
	arr[4] := 5;
	b := writeInt( 5 ); b := writeChar( 10 );
	
	return 0;
	
}

int test2()
{
	int a;
	int b;
	
	a := 1;
	
	return 0;
	
}

int main()
{


	int d;
	d := test1();
	d := test2();
	d := test3();

	   return 1;
 
}

