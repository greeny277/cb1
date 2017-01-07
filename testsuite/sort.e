
int[10] in;

int exchange(int x, int y)
{
  int t;
  t:=in[x];
  in[x]:=in[y];
  in[y]:=t;
  return 0;
}

int partition(int a, int i, int j)
{
  int v;
  int k;
  int d;
  j:=j+1;
  k := i;
  v := in[a+k];
  while (i < j) {
    i:=i+1; while (in[a+i] < v) {i:=i+1;}
    j:=j-1; while (in[a+j] > v) {j:=j-1;}
    if (i < j){ d:=exchange(a+i, a+j);}
  }
  d:=exchange(a+k,a+j);
  return j;
}

int quick(int a, int lb, int ub)
{
  int k;
  int d;
  if (lb >= ub){
    return 0;
  }
  k := partition(a, lb, ub);
  d:=quick(a, lb, k - 1);
  d:=quick(a, k + 1, ub);
  return 0;
}

int main() {
  int i;
  int d;

  in[0]:=10;
  in[1]:=32;
  in[2]:=0-1;
  in[3]:=567;
  in[4]:=3;
  in[5]:=18;
  in[6]:=1;
  in[7]:=0-51;
  in[8]:=789;
  in[9]:=0;

  i:=0;
  while (i<10){
    d:=writeInt(in[i]);
    d:=writeChar(32);
    i:=i+1;
  }
  d:=writeChar(10);

  d:=quick(0,0,9);

  i:=0;
  while (i<10){
    d:=writeInt(in[i]);
    d:=writeChar(32);
    i:=i+1;
  }
  d:=writeChar(10);
  return 0;
}



