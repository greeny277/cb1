/* verwendung von funktion als normaler variable */

int tester( int axxx )
{
	return tester(tester);
}

int main() { return 0; }
