CC=gcc
CFLAGS=-fno-asynchronous-unwind-tables -fno-exceptions -m64 -masm=intel -O0
SRC=$(wildcard *.c)
ASM=$(patsubst %.c,%.s,$(SRC))

.PHONY: all clean


all: $(ASM)

clean:
	rm -rf $(ASM)


%.s: %.c
	$(CC) $(CFLAGS) -S $<

