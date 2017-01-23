	.file	"writer.c"
	.intel_syntax noprefix
	.section	.rodata
.LC0:
	.string	"%lld"
	.text
	.globl	writeInt
	.type	writeInt, @function
writeInt:
	push	rbp
	mov	rbp, rsp
	push	rbx
	sub	rsp, 56
	mov	QWORD PTR [rbp-56], rdi
	mov	rax, QWORD PTR [rbp-56]
	mov	QWORD PTR [rbp-32], rax
	mov	DWORD PTR [rbp-20], 1
	jmp	.L2
.L3:
	add	DWORD PTR [rbp-20], 1
.L2:
	mov	rcx, QWORD PTR [rbp-56]
	movabs	rdx, 7378697629483820647
	mov	rax, rcx
	imul	rdx
	sar	rdx, 2
	mov	rax, rcx
	sar	rax, 63
	sub	rdx, rax
	mov	rax, rdx
	mov	QWORD PTR [rbp-56], rax
	cmp	QWORD PTR [rbp-56], 0
	jne	.L3
	mov	eax, DWORD PTR [rbp-20]
	mov	rdx, rsp
	mov	rbx, rdx
	mov	edx, eax
	sub	rdx, 1
	mov	QWORD PTR [rbp-40], rdx
	mov	edx, eax
	mov	r10, rdx
	mov	r11d, 0
	mov	edx, eax
	mov	r8, rdx
	mov	r9d, 0
	mov	edx, eax
	mov	eax, 16
	sub	rax, 1
	add	rax, rdx
	mov	esi, 16
	mov	edx, 0
	div	rsi
	imul	rax, rax, 16
	sub	rsp, rax
	mov	rax, rsp
	add	rax, 0
	mov	QWORD PTR [rbp-48], rax
	mov	rax, QWORD PTR [rbp-48]
	mov	rdx, QWORD PTR [rbp-32]
	mov	esi, OFFSET FLAT:.LC0
	mov	rdi, rax
	mov	eax, 0
	call	sprintf
	mov	edx, DWORD PTR [rbp-20]
	mov	rax, QWORD PTR [rbp-48]
	mov	rsi, rax
	mov	edi, 1
	call	write
	mov	eax, DWORD PTR [rbp-20]
	mov	rsp, rbx
	mov	rbx, QWORD PTR [rbp-8]
	leave
	ret
	.size	writeInt, .-writeInt
	.ident	"GCC: (Debian 4.9.2-10) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
