#include <stdio.h>
int max= 2147483647;
int min= (0-2147483647)-1;

int s01() { return (2147483647); }
int s02() { return ((0-2147483647)-1); }
int s03() { return (2147483647)+1; }
int s04() { return ((0-2147483647)-1)-1; }

int s05() { return (2147483647)*2/2; }
int s06() { return (2147483647)+2-2; }
int s07() { return (2147483647)-2+2; }
int s08() { return (2147483647)/2*2; }

int s09() { return ((0-2147483647)-1)*2/2; }
int s10() { return ((0-2147483647)-1)+2-2; }
int s11() { return ((0-2147483647)-1)-2+2; }
int s12() { return ((0-2147483647)-1)/2*2; }

int k01() { return max; }
int k02() { return min; }
int k03() { return max+1; }
int k04() { return min-1; }

int k05() { return max*2/2; }
int k06() { return max+2-2; }
int k07() { return max-2+2; }
int k08() { return max/2*2; }

int k09() { return min*2/2; }
int k10() { return min+2-2; }
int k11() { return min-2+2; }
int k12() { return min/2*2; }

int main() {
    int d;


    printf("%d", s01()); putchar(32); printf("%d", k01()); putchar(10);
    printf("%d", s02()); putchar(32); printf("%d", k02()); putchar(10);
    printf("%d", s03()); putchar(32); printf("%d", k03()); putchar(10);
    printf("%d", s04()); putchar(32); printf("%d", k04()); putchar(10);
    puts("");
    printf("%d", s05()); putchar(32); printf("%d", k05()); putchar(10);
    printf("%d", s06()); putchar(32); printf("%d", k06()); putchar(10);
    printf("%d", s07()); putchar(32); printf("%d", k07()); putchar(10);
    printf("%d", s08()); putchar(32); printf("%d", k08()); putchar(10);
    puts("");
    printf("%d", s09()); putchar(32); printf("%d", k09()); putchar(10);
    printf("%d", s10()); putchar(32); printf("%d", k10()); putchar(10);
    printf("%d", s11()); putchar(32); printf("%d", k11()); putchar(10);
    printf("%d", s12()); putchar(32); printf("%d", k12()); putchar(10);

	return 0;
}
