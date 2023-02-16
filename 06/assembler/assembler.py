import argparse
from pathlib import Path
import re


def main():
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

    s = open(source)
    t = open(source.with_suffix(".hack"), "w")

    line_number = 1
    next_variable = 16
    for line in s:
        line = line.split("//")[0]
        line = line.strip()
        if line.startswith("("):
            pass
        elif line:
            parts = line.split("@")
            if len(parts) == 2:  # this is an A instruction
                try:
                    value = int(parts[1])
                except:
                    if parts[1] in labels.keys():
                        value = labels[parts[1]]
                    elif parts[1] in symbols.keys():
                        value = symbols[parts[1]]
                    elif parts[1] in variables.keys():
                        value = variables[parts[1]]
                    else:
                        value = next_variable
                        variables[parts[1]] = value
                        next_variable += 1
                t.write(f"0{int(value):0>15b}\n")  # value.bin() => 0b0001010101
                line_number += 1
            else:  # this is a C instruction
                dest = "null"
                comp_jump = None
                comp = None
                jump = "null"
                parts = line.split("=")
                if len(parts) >= 2:
                    (dest, comp_jump) = parts[0:2]
                else:
                    comp_jump = parts[0]
                parts = comp_jump.split(";")
                if len(parts) >= 2:
                    (comp, jump) = parts[0:2]
                else:
                    comp = parts[0]

                # Combine and write the binary C command
                if (dest and comp) or (comp and jump):
                    a = "0"
                    if "M" in comp:
                        comp = comp.replace("M", "A")
                        a = "1"
                    comp = a + comp_codes[comp]
                    dest = dest_codes[dest]
                    jump = jump_codes[jump]

                    t.write(f"111{comp}{dest}{jump}\n")
                    line_number += 1

    s.close()
    t.close()


def get_labels(source):
    s = open(source)
    address = 0
    labels = {}
    valid_command = r"^[^\/]*[@=;]"
    valid_label = r"\((.+)\)"  # (LOOP)
    for line in s:
        line = line.split("//")[0]
        line = line.strip()
        command_match = re.match(valid_command, line)
        label_match = re.match(valid_label, line)
        if command_match:
            address += 1
        elif label_match:
            labels[label_match.groups(0)[0]] = address
    s.close()
    return labels


main()
