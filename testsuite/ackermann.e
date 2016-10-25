int ackermann(int m, int n) {
    int a;
    if (m = 0) {
        return n+1;
    }
    if (n = 0) {
	return ackermann(m-1, 1);
    }
    a := ackermann(m, n-1);
    return ackermann(m-1, a);
}


int
main()
{
	int dummy;

	dummy := ackermann(3, 6);
    dummy := writeInt(dummy);
    
	return 0;
}
