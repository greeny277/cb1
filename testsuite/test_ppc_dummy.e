
int glob;
int globber;

int[10] arr;

int yyy()
{
int d;
d := writeInt( glob );
d := writeChar( 10 );
d := writeInt( globber );
d := writeChar( 10 );
 return 0;
}


int xxx()
{
int r;
 glob := 1234;
 globber := 25;
 r := yyy();
 return 0;
}

int arrTest()
{
int d;
int r;
r := 0;
while ( r < 10 )
{
	arr[r] := r;
	d := writeInt( r );
	d := writeChar( 45 );
	d := arr[ 9-r ];
	d := writeInt( arr[r] );
	d := writeChar( 10 );
	r := r + 1;
}

	d := writeChar( 10 );
	d := writeChar( 45 );
	d := writeChar( 10 );
	d := writeChar( 10 );


r := 0;
while ( r < 10 )
{
d := writeInt( r );
	d := writeChar( 45 );
	d := writeInt( arr[r] );
	d := writeChar( 10 );
	r := r + 1;
}
return 0;
}

int main()
{
 int d;

 d := arrTest();
 
 return 0;
}

