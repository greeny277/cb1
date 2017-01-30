




int main( )
{
	int [4]x;
	int d;
    d := 2;
	x[ d ] := 3;
    x[0] := 1;
    x[x[0]] := 0-1;
    x[3] := 0;
    return x[0] + x[1] + x[3] - x[2];
}
