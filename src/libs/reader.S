# python e compiler assembler
	# <ir.IRProgram object at 0x7fb5c3203c18>
	.file	"readInt.e"
	.intel_syntax noprefix
	.text
	.global	readInt
readInt:
	# <ir.IRFunction object at 0x7fb5c343bcf8>
	push	rbp
	mov	rbp, rsp
	sub	rsp, 56
	# rax = 0
	mov	rax, 0
	# number = rax
	mov	[rbp-8], rax
	# rax = 0
	mov	rax, 0
	# r = rax
	mov	[rbp-16], rax
	# L1:
.L1:
	# rax = r
	mov	rax, [rbp-16]
	# rcx = 10
	mov	rcx, 10
	# CBNE rax, rcx, L2
	cmp	rax, rcx
	jne	.L2
	# CBRA L3
	jmp	.L3
	# L2:
.L2:
	# rax = 0
	mov	rax, 0
	# r = rax
	mov	[rbp-16], rax
	# $R0 = CALL [readChar]
	call	getchar@PLT
	mov	[rbp-24], rax
	# rax = $R0
	mov	rax, [rbp-24]
	# r = rax
	mov	[rbp-16], rax
	# rax = r
	mov	rax, [rbp-16]
	# rcx = 48
	mov	rcx, 48
	# CBLT rax, rcx, L5
	cmp	rax, rcx
	jl	.L5
	# L7:
.L7:
	# rax = r
	mov	rax, [rbp-16]
	# rcx = 57
	mov	rcx, 57
	# CBLE rax, rcx, L4
	cmp	rax, rcx
	jle	.L4
	# CBRA L5
	jmp	.L5
	# CBRA L5
	jmp	.L5
	# L4:
.L4:
	# rax = number
	mov	rax, [rbp-8]
	# rcx = 10
	mov	rcx, 10
	# rax = rax * rcx
	imul	rax, rcx
	# $R1 = rax
	mov	[rbp-32], rax
	# rax = $R1
	mov	rax, [rbp-32]
	# number = rax
	mov	[rbp-8], rax
	# rax = number
	mov	rax, [rbp-8]
	# rcx = r
	mov	rcx, [rbp-16]
	# rax = rax + rcx
	add	rax, rcx
	# $R2 = rax
	mov	[rbp-40], rax
	# rax = $R2
	mov	rax, [rbp-40]
	# rcx = 48
	mov	rcx, 48
	# rax = rax - rcx
	sub	rax, rcx
	# $R3 = rax
	mov	[rbp-48], rax
	# rax = $R3
	mov	rax, [rbp-48]
	# number = rax
	mov	[rbp-8], rax
	# CBRA L6
	jmp	.L6
	# L5:
.L5:
	# L6:
.L6:
	# CBRA L1
	jmp	.L1
	# L3:
.L3:
	# CRET number
	mov	rax, [rbp-8]
	leave
	ret
