	.file	"writeChar.c"
	.intel_syntax noprefix
	.text
	.globl	writeChar
	.type	writeChar, @function
writeChar:
	push	rbp
	mov	rbp, rsp
	sub	rsp, 32
	mov	DWORD PTR [rbp-20], edi
	mov	QWORD PTR [rbp-8], 0
	mov	eax, DWORD PTR [rbp-20]
	mov	BYTE PTR [rbp-9], al
	jmp	.L4
.L5:
	lea	rax, [rbp-9]
	mov	edx, 1
	mov	rsi, rax
	mov	edi, 1
	call	write
	mov	QWORD PTR [rbp-8], rax
.L4:
	cmp	QWORD PTR [rbp-8], 1
	jne	.L5
	mov	rax, QWORD PTR [rbp-8]
	leave
	ret
	.size	writeChar, .-writeChar
	.ident	"GCC: (Debian 4.9.2-10) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
