	.file	"time.c"
	.intel_syntax noprefix
	.text
	.globl	my_time
	.type	my_time, @function
my_time:
	push	rbp
	mov	rbp, rsp
	mov	edi, 0
	call	time@PLT
	pop	rbp
	ret
	.size	my_time, .-my_time
	.ident	"GCC: (Debian 6.2.1-5) 6.2.1 20161124"
	.section	.note.GNU-stack,"",@progbits
