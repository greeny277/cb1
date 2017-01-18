int foo(int a){
	return a;
}

int main(int argc, char **argv){
	int a;
	int b;
	int c;
	int d;

	a = 1;
	b = 2;
	c = 3;
	d = 4;

	if((foo(c) + 1) <= (a*b))
	{
		d = (a+b)*c;
	} else
	{
		d = c;
	}

	return d;
}
