/* nutzung einer lokalen variable nach ende ihres scope */

int foo() {
    int a;
    if(5 = a) {
         int b;
         b := 7;
         return 1;
    }
    a := 7;
    return b;
}

int main() { return 0; }
