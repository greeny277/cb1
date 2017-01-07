/* verwendung von funktion als normaler variable, in expression */

int tester( int axxx )
{
	return tester(23+tester);
}

int main() { return 0; }
