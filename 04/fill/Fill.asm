// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// While running (run forever)
(LOOP)
  // Initialize the i counter
  @i
  M=0
  // read the contents of keyboard memory
  @KBD
  D=M
  @whileBlack
  D;JGT
  (whileWhite)
  // if no key is pressed, write zeros to every register of the screen memory
    // Check counter
    @i
    D=M
    @8192
    D=D-A
    @LOOP
    D;JGE
    // write to the screen
    @SCREEN
    D=A
    @i
    A=D+M
    M=0
    // increment i
    @i
    M=M+1
    @whileWhite
    0;JMP
  (whileBlack)
  // if a key is pressed (keyboard != 0), write 1 to every register of the screen memory
    // Check counter
    @i
    D=M
    @8192
    D=D-A
    @LOOP
    D;JGE
    // write to the screen
    @SCREEN
    D=A
    @i
    A=D+M
    M=-1
    // increment i
    @i
    M=M+1
    @whileBlack
    0;JMP
(END)