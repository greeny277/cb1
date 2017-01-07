/* nutzung einer undefinierten variable */

int foo() {
    int a;
    if(b = a) {
         return -1;
    }
    return 0;
}

int main() { return 0; }
