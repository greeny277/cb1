

int fak(int n)
{
 if(n<=1){
  return 1;
 }else{
  return n*fak(n-1);
 }
}


int main()
{

	int a;
	int d;
	
	a := readInt();
	d := writeInt( a );
	d := writeChar( 10 );
	
	d := writeInt( fak( 6 ) );
	d := writeChar( 10 );
	d := writeInt( 101 );
	d := writeChar( 10 );
	return 0;
	
}

