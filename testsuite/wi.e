int main()
{
 int i;
 int dummy;
 i:=2147483647;
 dummy:=writeInt(i);
 dummy:=writeChar(10);
 i:=0-i;
 dummy:=writeInt(i);
 dummy:=writeChar(10);
 i:=i-1;
 dummy:=writeInt(i);
 dummy:=writeChar(10);
 return 0;
}
 
