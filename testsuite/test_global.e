
int glob;
int x;

int test2()
{
glob := 24;
	 return 0;
}

int main()
{
	   
glob := 12345;
x := test2();
glob := writeInt( glob );
	 return glob;
}

