int foo(int a)
{
	return a;
}

int main()
{
	int a;
	int b;
	int c;

	a := 1;
	b := 2;
	c := 3;

	if((foo(a*3) = 1 && b != 2) || c >= 3)
	{
		c := 1;
	}

	return c;
}
