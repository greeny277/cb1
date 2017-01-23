# python e compiler assembler
	# <ir.IRProgram object at 0x7f141e6e8198>
	.file	"reader.e"
	.intel_syntax noprefix
	.text
	.global	readInt
readInt:
	# <ir.IRFunction object at 0x7f141e6e83c8>
	push	rbp
	mov	rbp, rsp
	sub	rsp, 88
	# rax = 0
	mov	rax, 0
	# number = rax
	mov	[rbp-8], rax
	# rax = 0
	mov	rax, 0
	# r = rax
	mov	[rbp-16], rax
	# rax = 0
	mov	rax, 0
	# firstNumber = rax
	mov	[rbp-24], rax
	# rax = 0
	mov	rax, 0
	# minus = rax
	mov	[rbp-32], rax
	# rax = 0
	mov	rax, 0
	# special = rax
	mov	[rbp-40], rax
	# L1:
.L1:
	# rax = special
	mov	rax, [rbp-40]
	# rcx = 1
	mov	rcx, 1
	# CBEQ rax, rcx, L2
	cmp	rax, rcx
	je	.L2
	# L5:
.L5:
	# rax = firstNumber
	mov	rax, [rbp-24]
	# rcx = 0
	mov	rcx, 0
	# CBEQ rax, rcx, L2
	cmp	rax, rcx
	je	.L2
	# CBRA L4
	jmp	.L4
	# L4:
.L4:
	# rax = r
	mov	rax, [rbp-16]
	# rcx = 48
	mov	rcx, 48
	# CBLT rax, rcx, L3
	cmp	rax, rcx
	jl	.L3
	# L6:
.L6:
	# rax = r
	mov	rax, [rbp-16]
	# rcx = 57
	mov	rcx, 57
	# CBLE rax, rcx, L2
	cmp	rax, rcx
	jle	.L2
	# CBRA L3
	jmp	.L3
	# CBRA L3
	jmp	.L3
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
	mov	[rbp-48], rax
	# rax = $R0
	mov	rax, [rbp-48]
	# r = rax
	mov	[rbp-16], rax
	# rax = 0
	mov	rax, 0
	# special = rax
	mov	[rbp-40], rax
	# rax = r
	mov	rax, [rbp-16]
	# rcx = 45
	mov	rcx, 45
	# CBNE rax, rcx, L8
	cmp	rax, rcx
	jne	.L8
	# L10:
.L10:
	# rax = special
	mov	rax, [rbp-40]
	# rcx = 0
	mov	rcx, 0
	# CBEQ rax, rcx, L7
	cmp	rax, rcx
	je	.L7
	# CBRA L8
	jmp	.L8
	# CBRA L8
	jmp	.L8
	# L7:
.L7:
	# rax = -1
	mov	rax, -1
	# minus = rax
	mov	[rbp-32], rax
	# rax = 1
	mov	rax, 1
	# special = rax
	mov	[rbp-40], rax
	# CBRA L9
	jmp	.L9
	# L8:
.L8:
	# L9:
.L9:
	# rax = r
	mov	rax, [rbp-16]
	# rcx = 48
	mov	rcx, 48
	# CBLT rax, rcx, L12
	cmp	rax, rcx
	jl	.L12
	# L14:
.L14:
	# rax = r
	mov	rax, [rbp-16]
	# rcx = 57
	mov	rcx, 57
	# CBLE rax, rcx, L11
	cmp	rax, rcx
	jle	.L11
	# CBRA L12
	jmp	.L12
	# CBRA L12
	jmp	.L12
	# L11:
.L11:
	# rax = 1
	mov	rax, 1
	# firstNumber = rax
	mov	[rbp-24], rax
	# rax = number
	mov	rax, [rbp-8]
	# rcx = 10
	mov	rcx, 10
	# rax = rax * rcx
	imul	rax, rcx
	# $R1 = rax
	mov	[rbp-56], rax
	# rax = $R1
	mov	rax, [rbp-56]
	# number = rax
	mov	[rbp-8], rax
	# rax = number
	mov	rax, [rbp-8]
	# rcx = r
	mov	rcx, [rbp-16]
	# rax = rax + rcx
	add	rax, rcx
	# $R2 = rax
	mov	[rbp-64], rax
	# rax = $R2
	mov	rax, [rbp-64]
	# rcx = 48
	mov	rcx, 48
	# rax = rax - rcx
	sub	rax, rcx
	# $R3 = rax
	mov	[rbp-72], rax
	# rax = $R3
	mov	rax, [rbp-72]
	# number = rax
	mov	[rbp-8], rax
	# CBRA L13
	jmp	.L13
	# L12:
.L12:
	# L13:
.L13:
	# CBRA L1
	jmp	.L1
	# L3:
.L3:
	# rax = minus
	mov	rax, [rbp-32]
	# rcx = 0
	mov	rcx, 0
	# CBNE rax, rcx, L15
	cmp	rax, rcx
	jne	.L15
	# CBRA L16
	jmp	.L16
	# L15:
.L15:
	# rax = number
	mov	rax, [rbp-8]
	# rcx = minus
	mov	rcx, [rbp-32]
	# rax = rax * rcx
	imul	rax, rcx
	# $R4 = rax
	mov	[rbp-80], rax
	# rax = $R4
	mov	rax, [rbp-80]
	# number = rax
	mov	[rbp-8], rax
	# CBRA L17
	jmp	.L17
	# L16:
.L16:
	# L17:
.L17:
	# CRET number
	mov	rax, [rbp-8]
	leave
	ret
