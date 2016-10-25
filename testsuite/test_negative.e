

int main()
{
    /* max:  9223372036854775807
       min: -9223372036854775808*/ 
	int a;
	int d;
	d := writeInt( 9223372036854775807 );
	d := writeChar( 10 );

    d := writeInt( 0-(9223372036854775807+1) );
	d := writeChar( 10 );
    
	d := writeInt( 0-9223372036854775807-1 );
	d := writeChar( 10 );
	
	d := writeInt( 0-922337203685477580 );
	d := writeChar( 10 );
	
	d := writeInt(  1+9223372036854775807 );
	d := writeChar( 10 );

	return 0;
	
}

