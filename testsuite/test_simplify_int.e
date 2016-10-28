int simplify0()
{
	return 0;
}

int simplify1()
{
	return 8 + (2 + 4) + 3;
}

int simplify2()
{
	return 8 + 3;
}

int simplify3()
{
	return 8 - 2;
}

int simplify4()
{
	return 2 + 2 - 3;
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
	return 2 * (2 / 1);
}

int simplify7()
{
	return 2 * (2 - 1);
}

int simplify8()
{
	return 2 / (2 - 1);
}

int simplify9()
{
	return 3 * 2 / (2 + 1);
}

int simplify10()
{
	return 2 + 2 * 1;
}

int simplify11()
{
	return 2 + (2 + 1);
}

int simplify12()
{
	return 2 * 3 / (2 + 1);
}

int max;
int min;

int s01() { return (9223372036854775807); }
int s02() { return ((0-9223372036854775807)-1); }
int s03() { return (9223372036854775807)+1; }
int s04() { return ((0-9223372036854775807)-1)-1; }
int s05() { return (9223372036854775807)*2/2; }
int s06() { return (9223372036854775807)+2-2; }
int s07() { return (9223372036854775807)-2+2; }
int s08() { return (9223372036854775807)/2*2; }
int s09() { return ((0-9223372036854775807)-1)*2/2; }
int s10() { return ((0-9223372036854775807)-1)+2-2; }
int s11() { return ((0-9223372036854775807)-1)-2+2; }
int s12() { return ((0-9223372036854775807)-1)/2*2; }

int k01() { return max; }
int k02() { return min; }
int k03() { return max+1; }
int k04() { return min-1; }
int k05() { return max*2/2; }
int k06() { return max+2-2; }
int k07() { return max-2+2; }
int k08() { return max/2*2; }
int k09() { return min*2/2; }
int k10() { return min+2-2; }
int k11() { return min-2+2; }
int k12() { return min/2*2; }


int main() {
    int d;
    max := 9223372036854775807;
    min := (0-9223372036854775807)-1;

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

    d:=writeInt(s01()); d:=writeChar(32); d:=writeInt(k01()); d:=writeChar(10);
    d:=writeInt(s02()); d:=writeChar(32); d:=writeInt(k02()); d:=writeChar(10);
    d:=writeInt(s03()); d:=writeChar(32); d:=writeInt(k03()); d:=writeChar(10);
    d:=writeInt(s04()); d:=writeChar(32); d:=writeInt(k04()); d:=writeChar(10);
    d:=writeInt(s05()); d:=writeChar(32); d:=writeInt(k05()); d:=writeChar(10);
    d:=writeInt(s06()); d:=writeChar(32); d:=writeInt(k06()); d:=writeChar(10);
    d:=writeInt(s07()); d:=writeChar(32); d:=writeInt(k07()); d:=writeChar(10);
    d:=writeInt(s08()); d:=writeChar(32); d:=writeInt(k08()); d:=writeChar(10);
    d:=writeInt(s09()); d:=writeChar(32); d:=writeInt(k09()); d:=writeChar(10);
    d:=writeInt(s10()); d:=writeChar(32); d:=writeInt(k10()); d:=writeChar(10);
    d:=writeInt(s11()); d:=writeChar(32); d:=writeInt(k11()); d:=writeChar(10);
    d:=writeInt(s12()); d:=writeChar(32); d:=writeInt(k12()); d:=writeChar(10);

	return 0;
}
