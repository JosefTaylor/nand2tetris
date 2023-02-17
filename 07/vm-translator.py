import argparse
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("path")

    args = parser.parse_args()

    source = Path(args.path)

    s = open(source)
    t = open(source.with_suffix(".asm"), "w")

    line_num = 1

    for line in s:
        line = line.split("//")[0].strip()
        tokens = line.split(" ")
        if len(tokens) > 0 and tokens[0]:
            code_lines = command(tokens, line_num)
            line_num += len(code_lines)
            t.writelines(code_lines)

    s.close()
    t.close()


def command(tokens, line):
    commands = {
        "push": {
            "constant": [
                f"@{tokens[-1]} // push constant {tokens[-1]}\n",
                f"D=A\n",
                f"@SP\n",
                f"A=M\n",
                f"M=D\n",
                f"@SP\n",
                f"M=M+1\n",
            ]
        },
        "add": [
            "@SP // add two numbers from the stack\n",
            "AM=M-1\n",
            "D=M\n",
            "@SP\n",
            "AM=M-1\n",
            "D=D+M\n",
            "@SP\n",
            "A=M\n",
            "M=D\n",
            "@SP\n",
            "M=M+1\n",
        ],
        "sub": [
            "@SP // subtract two numbers from the stack\n",
            "AM=M-1\n",
            "D=M\n",
            "@SP\n",
            "AM=M-1\n",
            "D=M-D\n",
            "@SP\n",
            "A=M\n",
            "M=D\n",
            "@SP\n",
            "M=M+1\n",
        ],
        "and": [
            "@SP // AND two numbers from the stack\n",
            "AM=M-1\n",
            "D=M\n",
            "@SP\n",
            "AM=M-1\n",
            "D=D&M\n",
            "@SP\n",
            "A=M\n",
            "M=D\n",
            "@SP\n",
            "M=M+1\n",
        ],
        "or": [
            "@SP // OR two numbers from the stack\n",
            "AM=M-1\n",
            "D=M\n",
            "@SP\n",
            "AM=M-1\n",
            "D=D|M\n",
            "@SP\n",
            "A=M\n",
            "M=D\n",
            "@SP\n",
            "M=M+1\n",
        ],
        "not": [
            "@SP // NOT the last number from the stack\n",
            "AM=M-1\n",
            "D=!M\n",
            "@SP\n",
            "A=M\n",
            "M=D\n",
            "@SP\n",
            "M=M+1\n",
        ],
        "neg": [
            "@SP // negate the last number from the stack\n",
            "AM=M-1\n",
            "D=-M\n",
            "@SP\n",
            "A=M\n",
            "M=D\n",
            "@SP\n",
            "M=M+1\n",
        ],
        "eq": [
            f"@SP // check equality of two numbers from the stack\n",
            f"AM=M-1\n",
            f"D=M\n",
            f"@SP\n",
            f"AM=M-1\n",
            f"D=D-M\n",
            f"@{line+13} // EQUAL\n",
            f"D;JEQ\n",
            f"@SP\n",
            f"A=M\n",
            f"M=0\n",
            f"@{line+16} // END\n",
            f"0;JMP\n",
            f"@SP // EQUAL\n",
            f"A=M\n",
            f"M=-1\n",
            f"@SP // END\n",
            f"M=M+1\n",
        ],
        "lt": [
            f"@SP // check that the number at SP-2 < number at SP-1\n",
            f"AM=M-1\n",
            f"D=M\n",
            f"@SP\n",
            f"AM=M-1\n",
            f"D=M-D\n",
            f"@{line+13} // LESS_THAN\n",
            f"D;JLT\n",
            f"@SP\n",
            f"A=M\n",
            f"M=0\n",
            f"@{line+16} // END\n",
            f"0;JMP\n",
            f"@SP // LESS_THAN\n",
            f"A=M\n",
            f"M=-1\n",
            f"@SP // END\n",
            f"M=M+1\n",
        ],
        "gt": [
            f"@SP // check that the number at SP-2 > number at SP-1\n",
            f"AM=M-1\n",
            f"D=M\n",
            f"@SP\n",
            f"AM=M-1\n",
            f"D=M-D\n",
            f"@{line+13} // GREATER_THAN\n",
            f"D;JGT\n",
            f"@SP\n",
            f"A=M\n",
            f"M=0\n",
            f"@{line+16} //END\n",
            f"0;JMP\n",
            f"@SP // GREATER_THAN\n",
            f"A=M\n",
            f"M=-1\n",
            f"@SP // END\n",
            f"M=M+1\n",
        ],
    }

    command = commands
    i = 0
    while type(command) is dict:
        command = command[tokens[i]]
        i += 1
    return command


main()
