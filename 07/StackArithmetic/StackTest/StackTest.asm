@17 // push constant 17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17 // push constant 17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check equality of two numbers from the stack
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@28 // EQUAL
D;JEQ
@SP
A=M
M=0
@31 // END
0;JMP
@SP // EQUAL
A=M
M=-1
@SP // END
M=M+1
@17 // push constant 17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16 // push constant 16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check equality of two numbers from the stack
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@60 // EQUAL
D;JEQ
@SP
A=M
M=0
@63 // END
0;JMP
@SP // EQUAL
A=M
M=-1
@SP // END
M=M+1
@16 // push constant 16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17 // push constant 17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check equality of two numbers from the stack
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@92 // EQUAL
D;JEQ
@SP
A=M
M=0
@95 // END
0;JMP
@SP // EQUAL
A=M
M=-1
@SP // END
M=M+1
@892 // push constant 892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891 // push constant 891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check that the number at SP-2 < number at SP-1
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@124 // LESS_THAN
D;JLT
@SP
A=M
M=0
@127 // END
0;JMP
@SP // LESS_THAN
A=M
M=-1
@SP // END
M=M+1
@891 // push constant 891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892 // push constant 892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check that the number at SP-2 < number at SP-1
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@156 // LESS_THAN
D;JLT
@SP
A=M
M=0
@159 // END
0;JMP
@SP // LESS_THAN
A=M
M=-1
@SP // END
M=M+1
@891 // push constant 891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891 // push constant 891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check that the number at SP-2 < number at SP-1
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@188 // LESS_THAN
D;JLT
@SP
A=M
M=0
@191 // END
0;JMP
@SP // LESS_THAN
A=M
M=-1
@SP // END
M=M+1
@32767 // push constant 32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766 // push constant 32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check that the number at SP-2 > number at SP-1
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@220 // GREATER_THAN
D;JGT
@SP
A=M
M=0
@223 //END
0;JMP
@SP // GREATER_THAN
A=M
M=-1
@SP // END
M=M+1
@32766 // push constant 32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767 // push constant 32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check that the number at SP-2 > number at SP-1
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@252 // GREATER_THAN
D;JGT
@SP
A=M
M=0
@255 //END
0;JMP
@SP // GREATER_THAN
A=M
M=-1
@SP // END
M=M+1
@32766 // push constant 32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766 // push constant 32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // check that the number at SP-2 > number at SP-1
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@284 // GREATER_THAN
D;JGT
@SP
A=M
M=0
@287 //END
0;JMP
@SP // GREATER_THAN
A=M
M=-1
@SP // END
M=M+1
@57 // push constant 57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31 // push constant 31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53 // push constant 53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // add two numbers from the stack
AM=M-1
D=M
@SP
AM=M-1
D=D+M
@SP
A=M
M=D
@SP
M=M+1
@112 // push constant 112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // subtract two numbers from the stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP
A=M
M=D
@SP
M=M+1
@SP // negate the last number from the stack
AM=M-1
D=-M
@SP
A=M
M=D
@SP
M=M+1
@SP // AND two numbers from the stack
AM=M-1
D=M
@SP
AM=M-1
D=D&M
@SP
A=M
M=D
@SP
M=M+1
@82 // push constant 82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // OR two numbers from the stack
AM=M-1
D=M
@SP
AM=M-1
D=D|M
@SP
A=M
M=D
@SP
M=M+1
@SP // NOT the last number from the stack
AM=M-1
D=!M
@SP
A=M
M=D
@SP
M=M+1
