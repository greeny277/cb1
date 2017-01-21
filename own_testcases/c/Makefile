CC=gcc
CFLAGS=-pedantic -std=c99 -fno-asynchronous-unwind-tables -fno-exceptions -m64 -masm=intel -O0
SRC=$(wildcard *.c)
ASM=$(patsubst %.c,%.s,$(SRC))
BIN=$(patsubst %.c,%.out,$(SRC))

.PHONY: all clean


all: $(ASM) $(BIN)

clean:
	rm -rf $(ASM) $(BIN)


%.out: %.c
	$(CC) $(CFLAGS) -o $@ $<


%.s: %.c
	$(CC) $(CFLAGS) -S $<

