// push constant x
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant x
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// add two numbers from the stack
@SP
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
