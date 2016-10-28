
int f( int a, int b )
{
       int x;
       x:=writeInt(a);
       x:=writeChar(32);
       x:=writeInt(b);
       x:=writeChar(10);
	   return 0;
}

int f2()
{
       int x;
       x:=writeChar(102);
       x:=writeChar(50);
       x:=writeChar(10);
	   return 1;
}

int main()
{
	   int a;
a := f2();
a := f( 2, 4 );
a := f( 1, 2 );
   return a;
}

