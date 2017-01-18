	.file	"test_cond.c"
	.intel_syntax noprefix
	.text
	.globl	foo
	.type	foo, @function
foo:
	push	rbp
	mov	rbp, rsp
	mov	DWORD PTR [rbp-4], edi
	mov	eax, DWORD PTR [rbp-4]
	pop	rbp
	ret
	.size	foo, .-foo
	.globl	main
	.type	main, @function
main:
	push	rbp
	mov	rbp, rsp
	sub	rsp, 32
	mov	DWORD PTR [rbp-20], edi
	mov	QWORD PTR [rbp-32], rsi
	mov	DWORD PTR [rbp-8], 1
	mov	DWORD PTR [rbp-12], 2
	mov	DWORD PTR [rbp-16], -3
	mov	DWORD PTR [rbp-4], -4
	mov	eax, DWORD PTR [rbp-4]
	cdq
	idiv	DWORD PTR [rbp-16]
	mov	DWORD PTR [rbp-12], eax
	mov	eax, DWORD PTR [rbp-16]
	mov	edi, eax
	call	foo
	lea	edx, [rax+1]
	mov	eax, DWORD PTR [rbp-8]
	imul	eax, DWORD PTR [rbp-12]
	cmp	edx, eax
	jg	.L4
	mov	edx, DWORD PTR [rbp-8]
	mov	eax, DWORD PTR [rbp-12]
	add	eax, edx
	imul	eax, DWORD PTR [rbp-16]
	mov	DWORD PTR [rbp-4], eax
	jmp	.L5
.L4:
	mov	eax, DWORD PTR [rbp-16]
	mov	DWORD PTR [rbp-4], eax
.L5:
	mov	eax, DWORD PTR [rbp-4]
	leave
	ret
	.size	main, .-main
	.ident	"GCC: (Debian 4.9.2-10) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
