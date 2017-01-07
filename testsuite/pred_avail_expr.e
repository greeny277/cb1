int main() {
    int i;
    int j;
    int k;
    int l;
    int m;
    int n;
    k := 0;
    j := k + 2;
    i := j + 2;
    k := j + 2;
    n := 1;
    if(i = k) {
         if(j = k + 2) {
              m := n + 2;
              l := n + 3;
         } else {
              l := n + 3;
              m := n + 2;
         }
    } else {
         m := n + 2;
    }
    return j + k;
}