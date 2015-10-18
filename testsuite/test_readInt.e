int readIntDev2()
{

    int number;
    int curr;
    int d;
    
    number := 0;
    
    curr := readChar();
    while ( curr != 10 )
    {
        d := writeChar( 65 ); 
        d := writeChar( curr ); 
        d := writeChar( 66 ); 
        d := writeInt( number ); 
        d := writeChar( 10 );
        if ( curr >= 48 && curr <= 57 )
        {
            number := number * 10 + ( curr - 48 );
        }
        curr := readChar();  
    }
    return number;
}

int readIntDev()
{

    int number;
    int curr;
    int d;
    
    number := 0;
    
    curr := readChar();
    while ( curr != 10 )
    {
        d := writeChar( 65 ); 
        d := writeChar( curr ); 
        d := writeChar( 66 ); 
        d := writeInt( curr); 
        if ( curr >= 48 && curr <= 57 ) {
           d := writeChar( 67 );
        }
        d := writeChar( 10 );
        curr := readChar();  
    }
    return number;
}



int main2()
{
    int d;
    int r;
    d := 1;
       
    while( d != 0 ) {
        d := readIntDev();
        r := writeChar( 62 );
        d := writeInt( d );
        d := writeChar( 10 );
    }
    return 0-1;
}


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


int main()
{
    int d;
    int e;
    d := reader();
    d := writeInt( d );
    d := writeChar( 10 );
    
    d := reader();
    d := writeInt( d );
    d := writeChar( 10 );
    
    d := reader();
    d := writeInt( d );
    d := writeChar( 10 );
    
    d := reader();
    d := writeInt( d );
    d := writeChar( 10 );
    
    
    return 0;
}

