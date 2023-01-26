// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
// i = 0
@i
M=1
// R2 = 0
@R2
M=0
// while:
(LOOP)
  // if i > R1, go to endWhile
  @i
  D=M
  @R1
  D=D-M
  @END
  D;JGT // Jumps to end if D > 0 i.e. true
  // R2 += R0
  @R0
  D=M
  @R2
  M=D+M
  // i ++
  @i
  M=M+1
  // go to while
  @LOOP
  0;JMP //goes to the label in Register A (LOOP)
  // endwhile
(END)
  @END
  0;JMP //Infinite loop to end program.