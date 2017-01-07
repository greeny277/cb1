int exp(int a, int e) {
  int d;
  if (e = 0) {
     return 1;
  } else {
    d := exp(a, e - 1);
    return a * d;
  }
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
