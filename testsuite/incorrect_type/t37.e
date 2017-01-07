/* funktion als variable verwendet; in vergleich */

int tester( int aa )
{
	if (aa > tester) {
		return aa;
	}
}

int main() { return 0; }
