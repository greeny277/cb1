

int fak(int n)
{
 if(n<=1){
  return 1;
 }else{
  return n*fak(n-1);
 }
}

int dumm()
{
  return 123;
}

int main()
{

	   int a;
	   int b;
       int x;
	   a := 1;
	   b := 3;

       x := (a+b) - (( fak( 6 ) + 2 ) * 4 + 5) + dumm();
       x := writeInt(x);
       x := writeChar(10);
	   return (a+b) - (( fak( 14 ) + 2 ) * 4 + 5) + dumm();

}

