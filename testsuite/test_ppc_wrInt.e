

int mywriteInt( int number )
{
	int div;
	int dummy;
	int started;
	
	div := 10000000;
	started := 0;
	
	while( div > 0 )
	{

		if ( div <= number || started = 1 )
		{
			dummy := writeChar( (number/div)+48 );
			while( number > div )
			{
				number := number - div;
			}
			started := 1;
		}
		div := div / 10;
	}
	return 0;
}

int tester( int axxx )
{
	axxx := 4;
	axxx := writeChar( axxx+1+48 );
	return 0;
}

int main()
{
	int d;

d := mywriteInt( 98765432-12345678 );
    d := writeChar(10);
return 0;

}
