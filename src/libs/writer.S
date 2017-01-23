	.file	"writer.c"
	.intel_syntax noprefix
	.section	.rodata
.LC0:
	.string	"%ld"
	.text
	.globl	writeInt
	.type	writeInt, @function
writeInt:
	push	rbp
	mov	rbp, rsp
	sub	rsp, 32
	mov	QWORD PTR [rbp-24], rdi
	mov	rax, QWORD PTR [rbp-24]
	mov	rsi, rax
	mov	edi, OFFSET FLAT:.LC0
	mov	eax, 0
	call	printf
	mov	rax, QWORD PTR stdout[rip]
	mov	rdi, rax
	call	fflush
	mov	DWORD PTR [rbp-4], 1
	jmp	.L2
.L3:
	add	DWORD PTR [rbp-4], 1
.L2:
	mov	rcx, QWORD PTR [rbp-24]
	movabs	rdx, 7378697629483820647
	mov	rax, rcx
	imul	rdx
	sar	rdx, 2
	mov	rax, rcx
	sar	rax, 63
	sub	rdx, rax
	mov	rax, rdx
	mov	QWORD PTR [rbp-24], rax
	cmp	QWORD PTR [rbp-24], 0
	jne	.L3
	mov	eax, DWORD PTR [rbp-4]
	leave
	ret
	.size	writeInt, .-writeInt
	.ident	"GCC: (Debian 4.9.2-10) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
