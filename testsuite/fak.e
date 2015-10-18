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
 int dummy;
 dummy:=writeInt(fak(readInt()));
 dummy:=writeChar(10);
 return 0;
/* return fak(5);*/
}

