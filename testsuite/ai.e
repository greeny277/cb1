int[10] a;

int f(int x,int y,int z)
{
 return a[2]*x+y*z;
}

int g()
{
 return f(1,2,3);
}

int main()
{
 int dummy;
 a[2]:=3;
 dummy:=writeInt(g());
 dummy:=writeChar(10);
 return 0;
}

