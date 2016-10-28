/* array als variable verwendet, in array; array als quelle einer zuweisung */

int tester( real aa )
{
	int [4]x;

	x[x] := x;
}

int main() { return 0; }
