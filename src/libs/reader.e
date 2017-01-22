int reader()
{
    int d;
    int r;

    int number;

    number := 0;
    r := 0;
    while ( r != 10 ) {
        r := 0;
        r := readChar();
        if ( r >= 48 && r <= 57 ) {
            number := number * 10;
            number := number + r - 48;
        }
    }
    return number;
}
