	.file	"readChar.c"
	.intel_syntax noprefix
	.text
	.globl	readChar
	.type	readChar, @function
readChar:
	push	rbp
	mov	rbp, rsp
	sub	rsp, 16
	mov	QWORD PTR [rbp-8], 0
	jmp	.L4
.L5:
	lea	rax, [rbp-9]
	mov	edx, 1
	mov	rsi, rax
	mov	edi, 0
	call	read
	mov	QWORD PTR [rbp-8], rax
.L4:
	cmp	QWORD PTR [rbp-8], 1
	jne	.L5
	movzx	eax, BYTE PTR [rbp-9]
	movsx	eax, al
	leave
	ret
	.size	readChar, .-readChar
	.ident	"GCC: (Debian 4.9.2-10) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
