/* falsche nutzung einer geshadowten funktion */
int foo() {
    return 13;
}

int bar(int foo) {
    int z;
    z := foo();
    return z;
}

int main() { return 0; }