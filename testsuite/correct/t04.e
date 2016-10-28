int main() {
	int[2] a;
	int[3] b;

	b[1] := 0;
	a[b[1]] := 2;

	return a[0];
}
