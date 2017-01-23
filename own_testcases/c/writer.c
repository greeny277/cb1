#include <inttypes.h>
#include <unistd.h>
#include <stdio.h>

int writeInt(int64_t value) {
	int64_t old = value;
	unsigned int ret=1;
	while (value/=10) ret++;
	if(old < 0) {
		ret++;
	}
	char number[ret];
	sprintf(number, "%lld", old);
	write(1, &number, ret);
	return ret;
}

