int exp(int a, int e) {
  int d;
  d := 1;
  while(e > 0) {
     d := d * a;
	 e := e - 1;
  }
  return d;
}

int main() {
    int dummy;
    dummy := writeInt(exp(2, 0));
    dummy := writeChar(10);
    dummy := writeInt(exp(2, 1));
    dummy := writeChar(10);
    dummy := writeInt(exp(2, 2));
    dummy := writeChar(10);
    dummy := writeInt(exp(2, 3));
    dummy := writeChar(10);
    return exp(2, 3);
}
