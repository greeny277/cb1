

int main()
{

	int a;
	int b;
	real f;
    
    a := 2;
    b := 3;
	
	while ( ( a = 1 && b = 2 ) || ( b = 2 ) )
	{
		a := 1;
	}

	if ( a = b )
	{
		return a+b;
	}
	

	if ( a < b )
	{
		a := a * 2;
		return a;
	} else {
		b := b * 2;
		return b;
	}
	
	
}
	
