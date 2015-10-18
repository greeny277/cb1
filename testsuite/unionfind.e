/* simple union find implementation. */

int [10] parent;

int reset() {
    int i;
    i := 0;
    while(i < 10){
        parent[i] := i;
        i := i + 1;
    }
    return 0;
}

int printParent() {
    int i; int dummy;
    dummy := writeChar(91);
    i := 0;
    while(i < 10){
        dummy := writeInt(parent[i]);
        dummy := writeChar(32);
        i := i + 1;
    }
    dummy := writeChar(93);
    dummy := writeChar(10);
    return 0;
}

int find(int i) {
    if(parent[parent[i]] != parent[i]) {
        parent[i] := find(parent[i]);
    }
    return parent[i];
}

int union(int i, int j) {
    parent[find(i)] := find(j);
    return find(j);
}

int main() {
    int dummy;
    dummy := reset();
    while(1=1) {
        int inChar;
        dummy := printParent();
        inChar := readChar();
        if(inChar = 113) { // 'q'
            return 0;
        }
        if(inChar = 114) { // 'r'
            dummy := reset();
            dummy := readChar();
        } else { if(inChar = 117) { // 'u'
            int i; int j;
            dummy := readChar();
            i := readInt();
            j := readInt();
            i := union(i, j);
            dummy := writeInt(i);
            dummy := writeChar(10);
        } else { if(inChar = 102) { // 'f'
            int i;
            i := readInt();
            i := find(i);
            dummy := writeInt(i);
            dummy := writeChar(10);             
        } } }
    }
    return 0;
}
