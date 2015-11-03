/* falsche nutzung einer geshadowten variable */

int a;
int f() {
    int[15] a;
    { 
        a := 3;
    }
    return 0;
}

int main() { return 0; }
