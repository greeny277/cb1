	.file	"my_exit.c"
	.intel_syntax noprefix
	.text
	.globl	my_exit
	.type	my_exit, @function
my_exit:
	push	rbp
	mov	rbp, rsp
	sub	rsp, 16
	mov	DWORD PTR [rbp-4], edi
	mov	eax, DWORD PTR [rbp-4]
	mov	edi, eax
	call	exit
	.size	my_exit, .-my_exit
	.ident	"GCC: (Debian 4.9.2-10) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
