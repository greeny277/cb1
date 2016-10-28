int h(int a, int b, int c)
{
	int dummy;
	int tmp;

	tmp := 10000 * a + 100 * b + c;
	dummy := writeChar(104); /* h */
	dummy := writeChar(32);
	dummy := writeInt(tmp);
	dummy := writeChar(10);

	return 0;
}

int g(int a, int b, int c)
{
	int dummy;
	int tmp;

	tmp := 10000 * a + 100 * b + c;
	dummy := writeChar(103); /* g */
	dummy := writeChar(32);
	dummy := writeInt(tmp);
	dummy := writeChar(10);

	dummy := h(b, c, a);

	tmp := 10000 * a + 100 * b + c;
	dummy := writeChar(103); /* g */
	dummy := writeChar(32);
	dummy := writeInt(tmp);
	dummy := writeChar(10);

	return 0;
}

int f(int a, int b, int c)
{
	int dummy;
	int tmp;

	tmp := 10000 * a + 100 * b + c;
	dummy := writeChar(102); /* f */
	dummy := writeChar(32);
	dummy := writeInt(tmp);
	dummy := writeChar(10);

	dummy := g(b, c, a);

	tmp := 10000 * a + 100 * b + c;
	dummy := writeChar(102); /* f */
	dummy := writeChar(32);
	dummy := writeInt(tmp);
	dummy := writeChar(10);

	return 0;
}


int main()
{
	int dummy;
    int a;
    int b;
	int c;

	a := 1;
	b := 2;
	c := 3;

	dummy := f(a, b, c);
	return 0;
}
