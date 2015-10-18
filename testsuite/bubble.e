int[10] a;

int bubble(int n)
{
 int i;
 int j;
 i:=n-1;
 while(i>=1){
  j:=0;
  while(j<i){
   if(a[j]>a[j+1]){
    int temp;
    temp:=a[j];
    a[j]:=a[j+1];
    a[j+1]:=temp;
   }
   j:=j+1;
  }
  i:=i-1;
 }
 return 0;
}

int main()
{
 int i;
 int dummy;

 a[0]:=3;
 a[1]:=5;
 a[2]:=1;
 a[3]:=9;
 a[4]:=7;
 a[5]:=6;
 a[6]:=2;
 a[7]:=8;
 a[8]:=0;
 a[9]:=4;

 dummy:=bubble(10);

 i:=0;
 while(i<10){
  dummy:=writeInt(a[i]);
  dummy:=writeChar(32);
  i:=i+1;
 }
 dummy:=writeChar(10);
 return 0;
}

