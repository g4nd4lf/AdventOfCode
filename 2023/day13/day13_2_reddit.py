import argparse
from typing import List
import os, copy
os.chdir("./day13")

def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument("sample.txt")
    #args = parser.parse_args()

    with open("input.txt", "r") as file:
        inputs = file.read()

    print(f"part 1 solution: {part_one(inputs)}")
    print(f"part 2 solution: {part_two(inputs)}")


# Returns the number of lines above the horizontal reflection line,
# or zero if there is no horizontal reflection line. Where the reflection line
# is chosen such that there are exactly smudge_target "smudges"
def find_reflection(lines: List[str], smudge_target: int = 0) -> int:
    for split in range(len(lines) - 1):
        smudges = 0
        for i in range(split + 1):
            if split + i + 1 >= len(lines):
                continue

            row_above = lines[split - i]
            row_below = lines[split + i + 1]
            for a, b in zip(row_above, row_below):
                if a != b:
                    smudges += 1
        if smudges == smudge_target:
            return split + 1
    return 0


def part_one(inputs: str) -> int:
    input_list = [i.splitlines() for i in inputs.split("\n\n")]

    h_total = 0
    v_total = 0
    for lines in input_list:
        transpose = []
        for i in range(len(lines[0])):
            transpose.append("".join([row[i] for row in lines]))

        h_total += find_reflection(lines)
        v_total += find_reflection(transpose)

    return v_total + 100 * h_total


def part_two(inputs: str) -> int:
    input_list = [i.splitlines() for i in inputs.split("\n\n")]

    h_total = 0
    v_total = 0
    gains=[]
    for ip,lines in enumerate(input_list):
        transpose = []
        for i in range(len(lines[0])):
            transpose.append("".join([row[i] for row in lines]))
        pass
        hi_total = find_reflection(lines, 1)
        vi_total = find_reflection(transpose, 1)
        if hi_total>0:
            gains.append(hi_total*100)
        else:
            gains.append(vi_total)
        h_total += hi_total
        v_total += vi_total
        pass
    print(gains)
    return v_total + 100 * h_total


if __name__ == "__main__":
    main()