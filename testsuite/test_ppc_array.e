
int test1()
{
 int[10] i;
 int a;
 int r;
 int d;
 
 a := 2147483647;
 d := writeChar( 97 );
d := writeInt( a ); 
 d := writeChar( 10 );
 
 r := 0;
 while( r < 10 )
 {
 i[r] := r*100;
 d := writeInt( r*100 );
 d := writeChar( 45 );
 d := writeInt( i[r] );
 d := writeChar( 10 );
 r := r + 1;
 }

 d := writeChar( 97 );
d := writeInt( a ); 
 d := writeChar( 10 );
 
 r := 0;
 while( r < 10 )
 {
 d := writeInt( r*100 );
 d := writeChar( 45 );
 d := writeInt( i[r] );
 d := writeChar( 10 );
 r := r + 1;
 }

 d := writeChar( 97 );
d := writeInt( a ); 
 d := writeChar( 10 );

 
 return 0;
}

int test2()
{
int[10] arr;
int d;
arr[0] := 1049;
arr[1] := 987;
arr[2] := 1234;
d := writeInt( arr[0] );
d := writeChar( 10 );
d := writeInt( arr[1] );
d := writeChar( 10 );
d := writeInt( arr[2] );
d := writeChar( 10 );
return 4;
}

int main()
{
 int[10] i;
 int r;
 int d;
 
d := test2();
d := writeChar( 10 );
d := writeChar( 45 );
d := writeChar( 10 );
d := test1();
 
 return 0;
}

