import argparse
from pathlib import Path
import re


def main():
    commands = {
        "push": {
            "constant": "@{} // push constant x\n"
            + "D=A\n"
            + "@SP\n"
            + "A=M\n"
            + "M=D\n"
            + "@SP\n"
            + "M=M+1\n"
        },
        "add": "@SP // add two numbers from the stack\n"
        + "AM=M-1\n"
        + "D=M\n"
        + "@SP\n"
        + "AM=M-1\n"
        + "D=D+M\n"
        + "@SP\n"
        + "A=M\n"
        + "M=D\n"
        + "@SP\n"
        + "M=M+1\n",
        "eq": "@SP // check equality of two numbers from the stack\n"
        + "AM=M-1\n"
        + "D=M\n"
        + "@SP\n"
        + "AM=M-1\n"
        + "D=D-M\n"
        + "@EQUAL\n"
        + "D;JEQ\n"
        + "@SP\n"
        + "A=M\n"
        + "M=0\n"
        + "@END\n"
        + "0;JMP\n"
        + "(EQUAL)\n"
        + "@SP\n"
        + "A=M\n"
        + "M=-1\n"
        + "(END)\n"
        + "@SP\n"
        + "M=M+1\n",
        "lt": "@SP// check equality of two numbers from the stack\n"
        + "AM=M-1\n"
        + "D=M\n"
        + "@SP\n"
        + "AM=M-1\n"
        + "D=D-M\n"
        + "@LESS_THAN\n"
        + "D;JLT\n"
        + "@SP\n"
        + "A=M\n"
        + "M=0\n"
        + "@END\n"
        + "0;JMP\n"
        + "(LESS_THAN)\n"
        + "@SP\n"
        + "A=M\n"
        + "M=-1\n"
        + "(END)\n"
        + "@SP\n"
        + "M=M+1\n",
    }

    parser = argparse.ArgumentParser()

    parser.add_argument("path")

    args = parser.parse_args()

    source = Path(args.path)

    s = open(source)
    t = open(source.with_suffix(".asm"), "w")

    for line in s:
        line = line.split("//")[0].strip()
        tokens = line.split(" ")
        if len(tokens) > 0 and tokens[0]:
            command = commands
            i = 0
            while type(command) is dict:
                command = command[tokens[i]]
                i += 1

            t.write(command.format(*tokens[i:]))


main()
