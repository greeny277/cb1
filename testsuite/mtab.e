int[10][10] array;

int main()
{
 int dummy;
 int x;
 int y;
 int n;
 n:=readInt();
 x:=1;
 while(x<=n){
  y:=1;
  while(y<=n){
   array[x-1][y-1]:=x*y;
   y:=y+1;
  }
  x:=x+1;
 }
 x:=1;
 while(x<=n){
  y:=1;
  while(y<=n){
   dummy:=writeInt(array[x-1][y-1]);
   dummy:=writeChar(32);
   y:=y+1;
  }
  dummy:=writeChar(10);
  x:=x+1;
 }
 return 0;  
}

