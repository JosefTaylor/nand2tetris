import argparse
from pathlib import Path

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

#user_symbols = get_symbols(source)

s = open(source)
t = open(source.with_suffix(".hack"), "w")
for line in s:
    line = line.strip()
    if line.startswith("//"):
        pass
    elif line.startswith("@"):
        # it's an A instruction. output is 0 + 15 bit binary address.
        token = line.strip("@")
        #value = symbols[token] if token in symbols.keys() else int(token)
        t.write(f"0{int(token):0>15b}\n")
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

s.close()
t.close()

def get_symbols(source):
  symbols = {
      "SP": 0,
      "LCL": 1,
      "ARG": 2,
      "THIS": 3,
      "THAT": 4,
      "SCREEN": 16384,
      "KBD": 24576,
  }
  s = source.open()
  for line in s:
    if 