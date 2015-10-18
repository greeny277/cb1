
int tester()
{
	return 66;
}

int XXX()
{
	return 65;
}

int zehn()
{
	return 10;
}

int main()
{
	int d;


	
	d := 4;
	
	if ( d <= 4 )
	{
	d := writeChar( 71 );
	}

	d := 4;

	if ( d >= 4 )
	{
	d := writeChar( 72 );
	}
	
	d := writeChar( tester() );
	d := writeChar( tester() );
	d := writeChar( tester() );
	d := writeChar( tester() );
	d := writeChar( tester() );
	d := writeChar( tester() );
	d := writeChar( XXX() );
	d := writeChar( tester() );
	d := writeChar( tester()+1 );
	d := writeChar( tester()-1 );
	d := writeChar( zehn() );
	
	return 0;

}
