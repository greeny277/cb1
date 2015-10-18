
int f( int a )
{
	int b;
	b := 4;
	{
		int a;
		a := 0-4;
		b := a + b;
	}
	b := a + b;
	return b;
}


int main()
{

	   int a;
	   int d;
	   a := 5;
	   {
		   int a;
		   int ff;
		   a := 7;
		   ff := 7;
		   d := writeInt(ff+1000*a);
		   d := writeChar(10);
	   }
	   d := writeInt(a);
	   d := writeChar(10);
	   d := writeInt( f( a )+1000 );
	   d := writeChar(10);
	   return 0;
	   
}

