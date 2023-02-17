@17 // push constant 17
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@17 // push constant 17
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@27
D;JEQ
@SP // Compare part two
A=M
M=0
@30
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@17 // push constant 17
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@16 // push constant 16
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@59
D;JEQ
@SP // Compare part two
A=M
M=0
@62
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@16 // push constant 16
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@17 // push constant 17
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@91
D;JEQ
@SP // Compare part two
A=M
M=0
@94
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@892 // push constant 892
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@891 // push constant 891
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@123
D;JLT
@SP // Compare part two
A=M
M=0
@126
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@891 // push constant 891
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@892 // push constant 892
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@155
D;JLT
@SP // Compare part two
A=M
M=0
@158
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@891 // push constant 891
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@891 // push constant 891
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@187
D;JLT
@SP // Compare part two
A=M
M=0
@190
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@32767 // push constant 32767
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@32766 // push constant 32766
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@219
D;JGT
@SP // Compare part two
A=M
M=0
@222
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@32766 // push constant 32766
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@32767 // push constant 32767
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@251
D;JGT
@SP // Compare part two
A=M
M=0
@254
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@32766 // push constant 32766
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@32766 // push constant 32766
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D // Compare part one
@283
D;JGT
@SP // Compare part two
A=M
M=0
@286
0;JMP
@SP
A=M
M=-1
@SP // Increment SP
M=M+1
@57 // push constant 57
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@31 // push constant 31
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@53 // push constant 53
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=D+M
@SP // Content of D to stack
A=M
M=D
@SP // Increment SP
M=M+1
@112 // push constant 112
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP // Content of D to stack
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get one from stack
AM=M-1
D=-M
@SP // Content of D to stack
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=D&M
@SP // Content of D to stack
A=M
M=D
@SP // Increment SP
M=M+1
@82 // push constant 82
D=A
@SP // Set SP to D register
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get two from stack
AM=M-1
D=M
@SP
AM=M-1
D=D|M
@SP // Content of D to stack
A=M
M=D
@SP // Increment SP
M=M+1
@SP // Get one from stack
AM=M-1
D=!M
@SP // Content of D to stack
A=M
M=D
@SP // Increment SP
M=M+1
