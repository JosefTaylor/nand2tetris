(LOOP)
  // Initialize the i counter
  // @200
  // @8191 //one less than the size of the screen
  @5631 //8192 - 2*1280 - 1
  D=A
  @i
  M=D
  // read the contents of keyboard memory
  @KBD
  D=M
  @drawBlackLine
  D;JGT // keyboard greater than zero
  (whileWhite)
  // if no key is pressed, write zeros to every register of the screen memory
    // Check counter
    @i
    D=M
    @LOOP
    D;JLT
    // write to the screen
    @SCREEN
    D=A
    @1280
    D=D+A
    @i
    A=D+M
    M=0
    // decrement i
    @i
    M=M-1
    @whileWhite
    0;JMP
  (drawBlackLine)
    @27 // 512/16 - 4 - 1 // how many words of pixels to write black.
    D=A
    @j
    M=D
    @i
    M=M-1
    M=M-1
  (whileBlack)
  // if a key is pressed (keyboard != 0), write 1 to every register of the screen memory
    // Check counter
    @i
    D=M
    @LOOP
    D;JLT
    // check that j is not exhausted. if so, advance i to the next black line
    @j
    D=M
    @endOfBlackLine
    D;JLT
    // write to the screen
    @SCREEN
    D=A
    @1280
    D=D+A
    @i
    A=D+M
    M=-1
    // decrement i
    @i
    M=M-1
    // decrement j
    @j
    M=M-1
    @whileBlack
    0;JMP
    (endOfBlackLine)
    @i
    M=M-1
    M=M-1
    @drawBlackLine
    0;JMP
(END)