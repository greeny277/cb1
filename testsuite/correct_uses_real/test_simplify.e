int simplify0()
{
	return 0;
}

int simplify1()
{
	return 8.0 + (2 + 4) + 3.8;
}

int simplify2()
{
	return 8.0 + 3.8;
}

int simplify3()
{
	return 8.0 + 2;
}

int simplify4()
{
	return 2 + 2;
}

int simplify5()
{
	return 2 * (2 + 1);
}

int simplify5b()
{
	return 2 / (2 + 1);
}

int simplify6()
{
	return 2.0 * (2.0 / 1.0);
}

int simplify7()
{
	return 2.0 * (2.0 + 1);
}

int simplify8()
{
	return 2.0 / (2 + 1.0);
}

int simplify9()
{
	return 2.0 / (2 + 1);
}

int simplify10()
{
	return 2 + (2.0 + 1);
}

int simplify11()
{
	return 2 + (2 + 1.0);
}

int simplify12()
{
	return 2 / (2.0 + 1.0);
}

int main() {
    int d;
    d := writeInt(simplify0());    d := writeChar(10);
    d := writeInt(simplify1());    d := writeChar(10);
    d := writeInt(simplify2());    d := writeChar(10);
    d := writeInt(simplify3());    d := writeChar(10);
    d := writeInt(simplify4());    d := writeChar(10);
    d := writeInt(simplify5());    d := writeChar(10);
    d := writeInt(simplify5b());   d := writeChar(10);
    d := writeInt(simplify6());    d := writeChar(10);
    d := writeInt(simplify7());    d := writeChar(10);
    d := writeInt(simplify8());    d := writeChar(10);
    d := writeInt(simplify9());    d := writeChar(10);
    d := writeInt(simplify10());   d := writeChar(10);
    d := writeInt(simplify11());   d := writeChar(10);
    d := writeInt(simplify12());   d := writeChar(10);
	return 0;
}
