int reader()
{
    int d;
    int r;
	int minus;
	int firstNumber;
	int special;

    int number;

    number := 0;
    r := 0;
    firstNumber := 0;
    minus := 0;
	special := 0;
    while ( special = 1 || firstNumber = 0 || (r >= 48 && r <= 57)) {
        r := 0;
        r := readChar();
		special := 0;
		if (r = 45 && special = 0) {
			minus := 0 - 1;
			special := 1;
		}
        if ( r >= 48 && r <= 57 ) {
			firstNumber := 1;
            number := number * 10;
            number := number + r - 48;
        }
    }
	if (minus != 0){
		number := number * minus;
	}
    return number;
}
