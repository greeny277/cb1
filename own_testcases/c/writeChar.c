#include<stdio.h>

int main( int argc, char **argv ) {
	char in;
	while ( 1 ) {
		in = (char) getchar();
		fprintf( stdout, "Input char:%c\n", in );
	}
	return 0;
}
