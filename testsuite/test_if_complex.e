

int main()
{

	int a;
	int b;
	int c;
	int d;
	int e;
	int f;
	int g;
	int h;

    a := 1;
    b := 1;
    c := 1;
    d := 1;
    e := 1;
    f := 1;
    g := 1;
    h := 1;

	while ( ( ( a = 1 && b = 2 )
		|| ( c = 3 && d = 4 ) )
		&& ( ( e = 5 || f = 6 )
			&& ( g = 7 || h = 8 ) ) ) 
	{
		a := ( 1 + a );
	}

    return 7;	
}
	
