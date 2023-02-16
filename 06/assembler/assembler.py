import argparse
from pathlib import Path
import re

valid_chars = "01DAMJGELNTQP-+!&|"


def main():
    global valid_chars

    parser = argparse.ArgumentParser()

    parser.add_argument("path")

    args = parser.parse_args()

    source = Path(args.path)

    comp_codes = {
        "0": "101010",
        "1": "111111",
        "-1": "111010",
        "D": "001100",
        "A": "110000",
        "!D": "001101",
        "!A": "110001",
        "-D": "001111",
        "-A": "110011",
        "D+1": "011111",
        "A+1": "110111",
        "D-1": "001110",
        "A-1": "110010",
        "D+A": "000010",
        "D-A": "010011",
        "A-D": "000111",
        "D&A": "000000",
        "D|A": "010101",
    }
    dest_codes = {
        "": "000",
        "null": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111",
    }
    jump_codes = {
        "": "000",
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111",
    }

    symbols = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SCREEN": 16384,
        "KBD": 24576,
    }

    variables = {}

    labels = get_labels(source)
    print(labels)

    s = open(source)
    t = open(source.with_suffix(".hack"), "w")
    line_number = 1
    next_variable = 16
    for line in s:
        line = line.strip()
        if line.startswith("//"):
            pass
        elif line.startswith("@"):
            # it's an A instruction. output is 0 + 15 bit binary address.
            token = line.strip("@")
            try:
                value = int(token)
            except:
                if token in labels.keys():
                    value = labels[token]
                elif token in symbols.keys():
                    value = symbols[token]
                elif token in variables.keys():
                    value = variables[token]
                else:
                    value = next_variable
                    variables[token] = value
                    next_variable += 1
            t.write(f"0{int(value):0>15b}\n")  # value.bin() => 0b0001010101
            line_number += 1
        else:
            tokens = {}
            token = []
            for char in line:
                if char in "01DAMJGELNTQP-+!&|":
                    token.append(char)
                elif char == "=":
                    tokens["dest"] = "".join(token)
                    token = []
                elif char == ";":
                    tokens["comp"] = "".join(token)
                    token = []
                else:
                    break
            if "comp" in tokens.keys():
                tokens["jump"] = "".join(token)
            else:
                tokens["comp"] = "".join(token)
            token = []

            if len(tokens.keys()) > 1:
                a = "0"
                if "M" in tokens["comp"]:
                    tokens["comp"] = tokens["comp"].replace("M", "A")
                    a = "1"
                comp = a + comp_codes[tokens["comp"]]
                dest = (
                    dest_codes[tokens["dest"]]
                    if "dest" in tokens.keys()
                    else dest_codes["null"]
                )
                jump = (
                    jump_codes[tokens["jump"]]
                    if "jump" in tokens.keys()
                    else jump_codes["null"]
                )
                t.write(f"111{comp}{dest}{jump}\n")
                line_number += 1

    s.close()
    t.close()


def get_labels(source):
    s = source.open()
    address = 0
    labels = {}
    valid_command = r"^[^\/]*[@=;]"
    valid_label = r"\([\D][\w\.\$\:]+\)"  # (LOOP)
    for line in s:
        if re.match(valid_command, line):
            address += 1
        if re.match(valid_label, line):
            labels[line.strip("() \n")] = address

    s.close()
    return labels


main()
