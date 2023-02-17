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

    line_num = 0

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
    increment_SP = [
        "@SP // Increment SP\n",
        "M=M+1\n",
    ]
    set_SP_to_D_reg = [
        "@SP // Set SP to D register\n",
        "A=M\n",
        "M=D\n",
    ]
    offset_address_to_D = [
        "D=M // Offset address to D\n",
        f"@{tokens[-1]}",
        "A=D+A",
        "D=M",
    ]
    get_one_from_stack = [  # value will be available in M
        "@SP // Get one from stack\n",
        "AM=M-1\n",
    ]
    get_two_from_stack = [
        "@SP // Get two from stack\n",
        "AM=M-1\n",
        "D=M\n",
        "@SP\n",
        "AM=M-1\n",
    ]
    content_of_D_to_stack = [
        "@SP // Content of D to stack\n",
        "A=M\n",
        "M=D\n",
    ]
    compare_part_one = [
        "D=M-D // Compare part one\n",
        f"@{line+13}\n",
    ]
    compare_part_two = [
        "@SP // Compare part two\n",
        "A=M\n",
        "M=0\n",
        f"@{line+16}\n",
        "0;JMP\n",
        "@SP\n",
        "A=M\n",
        "M=-1\n",
    ]
    commands = {
        "push": {
            "constant": [
                f"@{tokens[-1]} // push constant {tokens[-1]}\n",
                f"D=A\n",
                *set_SP_to_D_reg,
                *increment_SP,
            ],
            "local": [
                f"@1 // push local {tokens[-1]}\n",
                *offset_address_to_D,
                *set_SP_to_D_reg,
                *increment_SP,
            ],
            "argument": [
                f"@2 // push argument {tokens[-1]}\n",
                *offset_address_to_D,
                *set_SP_to_D_reg,
                *increment_SP,
            ],
            "this": [
                f"@3 // push this {tokens[-1]}\n",
                *offset_address_to_D,
                *set_SP_to_D_reg,
                *increment_SP,
            ],
            "that": [
                f"@4 // push that {tokens[-1]}\n",
                *offset_address_to_D,
                *set_SP_to_D_reg,
                *increment_SP,
            ],
        },
        "add": [
            *get_two_from_stack,
            "D=D+M\n",
            *content_of_D_to_stack,
            *increment_SP,
        ],
        "sub": [
            *get_two_from_stack,
            "D=M-D\n",
            *content_of_D_to_stack,
            *increment_SP,
        ],
        "and": [
            *get_two_from_stack,
            "D=D&M\n",
            *content_of_D_to_stack,
            *increment_SP,
        ],
        "or": [
            *get_two_from_stack,
            "D=D|M\n",
            *content_of_D_to_stack,
            *increment_SP,
        ],
        "not": [
            *get_one_from_stack,
            "D=!M\n",
            *content_of_D_to_stack,
            *increment_SP,
        ],
        "neg": [
            *get_one_from_stack,
            "D=-M\n",
            *content_of_D_to_stack,
            *increment_SP,
        ],
        "eq": [
            *get_two_from_stack,
            *compare_part_one,
            f"D;JEQ\n",
            *compare_part_two,
            *increment_SP,
        ],
        "lt": [
            *get_two_from_stack,
            *compare_part_one,
            f"D;JLT\n",
            *compare_part_two,
            *increment_SP,
        ],
        "gt": [
            *get_two_from_stack,
            *compare_part_one,
            f"D;JGT\n",
            *compare_part_two,
            *increment_SP,
        ],
    }

    command = commands
    i = 0
    while type(command) is dict:
        command = command[tokens[i]]
        i += 1
    return command


main()
