
int a;

int setA()
{
	a := 25;
	return a;
}

int b;

int setB()
{
	b := 171;
	return b;
}

int dumpBoth()
{
	int d;
	d := writeInt( a );
	d := writeChar( 10 );
	d := writeInt( b );
	d := writeChar( 10 );
	return 0;
}

int main()
{

	int d;
	
	d := setA();
	d := setB();
	d := dumpBoth();
	
	return 0;
	
}

