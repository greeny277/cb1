
int main()
{

	int[ 10 ][ 10 ][ 10 ] arr;
	int d;
	int i;
	int j;
	int k;

i := 0;
 while ( i < 10 )
 {
j := 0;
   while ( j < 10 )
   {
k := 0;
   while ( k < 10 )
   {
		 arr[ i ][ j ][ k ] := i*j*k;
k := k + 1;
   }
j := j + 1;
   }
i := i + 1;
 }
	
i := 0;
 while ( i < 10 )
 {
j := 0;
   while ( j < 10 )
   {
k := 0;
   while ( k < 10 )
   {
	d:= writeInt( arr[ i ][ j ][ k ] );
d:= writeChar( 32 );
k := k + 1;
   }
	d := writeChar( 10 );
j := j + 1;
   }
d := writeChar( 10 );
i := i + 1;
 }
	
	return 0;
 
}

