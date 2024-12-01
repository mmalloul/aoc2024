# Advent Of Code 2024: Day 1
from collections import Counter


def load(file: str):
    with open(file, "r") as f:
        return f.read().strip().split("\n")


def get_lists(problems):
    list1 = []
    list2 = []

    for line in problems:
        value1, value2 = line.split()
        list1.append(int(value1))
        list2.append(int(value2))

    return sorted(list1), sorted(list2)


def part1(list1, list2):
    total = 0
    for input1, input2 in zip(list1, list2):
        total += abs(input1 - input2)
    return total


def part2(list1, list2):
    counter = Counter(list2)
    score = 0
    for number in list1:
        score += number * counter[number]
    return score


if __name__ == "__main__":
    problems = load("day1/input.txt")

    list1, list2 = get_lists(problems)

    print(f"Total difference part 1: {part1(list1, list2)}")
    print(f"Similarity score part 2: {part2(list1, list2)}")
