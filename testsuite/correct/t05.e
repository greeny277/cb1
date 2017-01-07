int main() {
	int[2] a;
	int[3] b;
	int i;
	i := 1;
	
	b[i] := 0;
	a[b[i]] := 2;

	return a[1];
}
