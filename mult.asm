// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//// Replace this comment with your code.
	// n = 1
	@n
	M=1
	// sum = 0
	@sum
	M=0
(LOOP)
	// if (n > R0) goto STOP
	@n
	D=M
	@R0
	D=D-M
	@STOP
	D;JGT
	// sum = sum + R1
	@sum
	D=M
	@R1
	D=D+M
	@sum
	M=D
	// n = n + 1
	@n
	M=M+1
	// goto LOOP
	@LOOP
	0;JMP
(STOP)
	// R2 = sum
	@sum
	D=M
	@R2
	M=D
(END)
	@END
	0;JMP
