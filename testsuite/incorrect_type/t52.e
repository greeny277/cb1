/* falsche nutzung einer geshadowten variable */

int [15] a;
int f() {
    int a;
    { 
        a[10] := 3;
    }
    return 0;
}

int main() { return 0; }
